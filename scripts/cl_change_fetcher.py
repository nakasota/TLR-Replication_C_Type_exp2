import re
import json
import logging
import requests
import base64
import binascii
from typing import Dict, List, Optional, Tuple, Set
from tree_sitter import Language, Parser
import urllib.parse
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'  # シンプルなフォーマットに変更
)
logger = logging.getLogger(__name__)

class CLChangeFetcher:
    """Fetches code changes from Gerrit CLs."""
    
    def __init__(self):
        """Initialize the fetcher."""
        self.logger = logging.getLogger(__name__)
        
        # Tree-sitterの初期化
        self.parser = Parser()
        self.go_language = Language('tree-sitter-build/lib/tree-sitter-go.so', 'go')
        self.parser.set_language(self.go_language)
        
        # リポジトリローダーの初期化
        from methods.baseline_v3.src.utils.go_repo_loader import GoRepoLoader
        self.repo_loader = GoRepoLoader(repo_structure_path='data/preprocess/go_repo_structure.json')
        
    def fetch_changes_from_proposal(self, proposal_content: str) -> Optional[Dict]:
        """
        提案からCLの変更を取得します。
        
        Args:
            proposal_content: 提案の内容
            
        Returns:
            CLの変更情報を含む辞書、または取得に失敗した場合はNone
        """
        try:
            # CLの番号を抽出
            cl_number = self._extract_cl_number(proposal_content)
            if not cl_number:
                logger.warning("❌ CL番号が見つかりませんでした")
                return None
            
            logger.info(f"✓ CL番号を検出: {cl_number}")
            
            # CLの情報を取得
            cl_info = self._fetch_cl_info(cl_number)
            if not cl_info:
                logger.warning(f"❌ CL {cl_number} の情報を取得できませんでした")
                return None
            
            logger.info(f"✓ CL情報を取得: {cl_info.get('subject', '')}")
            
            # 変更されたファイルの情報を取得
            files = self._fetch_file_changes(cl_number)
            if not files:
                logger.warning(f"❌ CL {cl_number} の変更ファイル情報を取得できませんでした")
                return None
            
            # 結果を返す
            return {
                'cl_number': cl_number,
                'status': cl_info.get('status', ''),
                'subject': cl_info.get('subject', ''),
                'files': files
            }
            
        except Exception as e:
            logger.error(f"❌ CLの変更取得中にエラーが発生しました: {str(e)}")
            return None
            
    def _fetch_cl_info(self, cl_number: str) -> Optional[Dict]:
        """
        CLの基本情報を取得します。
        
        Args:
            cl_number: CL番号
            
        Returns:
            CLの情報を含む辞書、または取得に失敗した場合はNone
        """
        try:
            # Try different Gerrit API endpoints
            gerrit_endpoints = [
                f"https://go-review.googlesource.com/changes/{cl_number}",
                f"https://go-review.googlesource.com/changes/go~{cl_number}"
            ]
            
            for endpoint in gerrit_endpoints:
                try:
                    response = requests.get(endpoint)
                    if response.status_code == 200:
                        # Remove the ")]}'" prefix if present
                        text = response.text
                        if text.startswith(")]}'"):
                            text = text[4:]
                        
                        # Parse JSON response
                        data = json.loads(text)
                        return data
                except Exception as e:
                    self.logger.error(f"APIエンドポイントへのアクセスに失敗しました: {str(e)}")
                    continue
            
            return None
            
        except Exception as e:
            self.logger.error(f"CL情報の取得に失敗しました: {str(e)}")
            return None
            
    def _fetch_file_changes(self, cl_number: str) -> Optional[Dict]:
        """
        CLで変更されたファイルの情報を取得します。
        
        Args:
            cl_number: CL番号
            
        Returns:
            変更されたファイルの情報を含む辞書、または取得に失敗した場合はNone
        """
        try:
            # Try different Gerrit API endpoints
            gerrit_endpoints = [
                f"https://go-review.googlesource.com/changes/{cl_number}/revisions/current/files",
                f"https://go-review.googlesource.com/changes/go~{cl_number}/revisions/current/files"
            ]
            
            last_error = None
            for endpoint in gerrit_endpoints:
                try:
                    response = requests.get(endpoint)
                    if response.status_code == 200:
                        # Remove the ")]}'" prefix if present
                        text = response.text
                        if text.startswith(")]}'"):
                            text = text[4:]
                        
                        try:
                            # Parse JSON response
                            files_data = json.loads(text)
                        except json.JSONDecodeError as je:
                            last_error = f"JSONデコードエラー: {str(je)}"
                            continue
                        
                        # 各ファイルの変更情報を取得
                        files = {}
                        for file_path, file_info in files_data.items():
                            if file_path == '/COMMIT_MSG':
                                continue
                            
                            # Goファイルのみを処理
                            if not file_path.endswith('.go'):
                                continue
                            
                            # 現在のリポジトリのファイル内容を取得
                            repo_content = self.repo_loader.get_file_content(file_path)
                            if not repo_content:
                                logger.debug(f"  ⚠️ スキップ: {file_path} (現在のリポジトリの内容を取得できません)")
                                continue
                            
                            # 現在のリポジトリのファイルから関数を抽出
                            repo_functions = self._extract_functions_from_source(repo_content)
                            if not repo_functions:
                                logger.debug(f"  ⚠️ スキップ: {file_path} (現在のリポジトリから関数を抽出できません)")
                                continue
                            
                            # Gerrit APIからdiff情報を取得
                            diff_info = self._get_file_diff(cl_number, file_path)
                            if not diff_info:
                                logger.debug(f"  ⚠️ スキップ: {file_path} (diff情報を取得できません)")
                                continue
                            
                            # diffから変更された関数名を抽出
                            changed_functions = self._extract_functions_from_diff(diff_info, repo_content, repo_functions)
                            if not changed_functions:
                                logger.debug(f"  ⚠️ スキップ: {file_path} (diffから関数を抽出できません)")
                                continue
                            
                            # 変更された関数のうち、現在のリポジトリに存在するものを特定
                            modified_functions = []
                            for func_name in changed_functions:
                                if func_name in repo_functions:
                                    modified_functions.append(func_name)
                                    logger.info(f"  ✓ 変更を検出: {func_name} (現在のリポジトリに存在)")
                                else:
                                    logger.debug(f"  ⚠️ スキップ: {func_name} (現在のリポジトリに存在しません)")
                            
                            files[file_path] = {
                                'status': file_info.get('status', ''),
                                'lines_inserted': file_info.get('lines_inserted', 0),
                                'lines_deleted': file_info.get('lines_deleted', 0),
                                'modified_functions': modified_functions
                            }
                        
                        return files
                    else:
                        last_error = f"HTTPエラー {response.status_code}"
                except requests.exceptions.RequestException as e:
                    last_error = f"リクエストエラー: {str(e)}"
                    continue
            
            if last_error:
                logger.warning(f"❌ CL {cl_number} の変更ファイル情報を取得できませんでした - {last_error}")
            return None
            
        except Exception as e:
            logger.error(f"❌ ファイル変更情報の取得に失敗しました: {str(e)}")
            return None

    def _get_file_diff(self, cl_number: str, file_path: str) -> Optional[Dict]:
        """
        指定されたCLとファイルパスに対応するdiff情報を取得します。
        
        Args:
            cl_number: CL番号
            file_path: ファイルパス
            
        Returns:
            diff情報の辞書（changed_lines: 変更された行番号のセット、diff_content: diff内容のリスト）
        """
        gerrit_endpoints = [
            f"https://go-review.googlesource.com/changes/{cl_number}/revisions/current/files/{urllib.parse.quote_plus(file_path)}/diff",
            f"https://go-review.googlesource.com/changes/go~{cl_number}/revisions/current/files/{urllib.parse.quote_plus(file_path)}/diff"
        ]
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; GoProposalAnalyzer/1.0)',
            'Accept': 'application/json',
        }
        
        for endpoint in gerrit_endpoints:
            try:
                response = requests.get(endpoint, headers=headers, timeout=30)
                if response.status_code == 200:
                    text = response.text
                    if text.startswith(")]}'"):
                        text = text[4:]
                    
                    try:
                        diff_data = json.loads(text)
                        # diff内容から変更された行番号と内容を抽出
                        changed_lines = set()
                        diff_content = []
                        
                        if 'content' in diff_data:
                            for content_item in diff_data['content']:
                                if 'ab' in content_item:  # 変更された行
                                    a_val = content_item.get('a', 0)
                                    start_line = (a_val if isinstance(a_val, int) else 0) + 1  # 1-based line numbers
                                    ab_content = content_item['ab']
                                    # 'ab'がリストの場合のみ処理
                                    if isinstance(ab_content, list):
                                        for i, line_content in enumerate(ab_content):
                                            line_no = start_line + i
                                            changed_lines.add(line_no)
                                            diff_content.append(line_content)
                                    else:
                                        # 'ab'が文字列や整数の場合
                                        changed_lines.add(start_line)
                                        if isinstance(ab_content, str):
                                            diff_content.append(ab_content)
                                elif 'b' in content_item:  # 追加された行
                                    a_val = content_item.get('a', 0)
                                    start_line = (a_val if isinstance(a_val, int) else 0) + 1
                                    b_content = content_item['b']
                                    # 'b'がリストの場合のみ処理
                                    if isinstance(b_content, list):
                                        for i, line_content in enumerate(b_content):
                                            line_no = start_line + i
                                            changed_lines.add(line_no)
                                            diff_content.append(line_content)
                                    else:
                                        # 'b'が文字列や整数の場合
                                        changed_lines.add(start_line)
                                        if isinstance(b_content, str):
                                            diff_content.append(b_content)
                                elif 'a' in content_item:  # 削除された行の場合は対応する行番号を記録
                                    a_val = content_item.get('a', 0)
                                    start_line = (a_val if isinstance(a_val, int) else 0) + 1
                                    a_content = content_item.get('a', [])
                                    # 'a'が整数の場合（行番号）、リストの場合（削除された行の内容）どちらも対応
                                    if isinstance(a_content, int):
                                        # 単一の削除行
                                        changed_lines.add(start_line)
                                    elif isinstance(a_content, list):
                                        # 複数の削除行
                                        end_line = start_line + len(a_content)
                                        for line_no in range(start_line, end_line):
                                            changed_lines.add(line_no)
                        
                        return {
                            'changed_lines': changed_lines,
                            'diff_content': diff_content
                        }
                    except json.JSONDecodeError:
                        continue
                elif response.status_code == 404:
                    break
            except requests.exceptions.RequestException:
                continue
        
        return None

    def get_file_content(self, cl_number: str, file_path: str) -> Optional[str]:
        """
        指定されたCLとファイルパスに対応するファイルの内容を取得します。
        
        Args:
            cl_number: CL番号
            file_path: ファイルパス
            
        Returns:
            ファイルの内容（取得に失敗した場合はNone）
        """
        # まず、現在のリポジトリから取得を試みる
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except (FileNotFoundError, IOError):
            pass
        
        # 次に、Gerrit APIから取得を試みる
        gerrit_endpoints = [
            f"https://go-review.googlesource.com/changes/{cl_number}/revisions/current/files/{urllib.parse.quote_plus(file_path)}/content",
            f"https://go-review.googlesource.com/changes/go~{cl_number}/revisions/current/files/{urllib.parse.quote_plus(file_path)}/content"
        ]
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; GoProposalAnalyzer/1.0)',
            'Accept': 'text/plain',
        }
        
        max_retries = 3
        retry_delay = 1  # seconds
        
        # Gerrit APIから取得を試みる
        for endpoint in gerrit_endpoints:
            for attempt in range(max_retries):
                try:
                    response = requests.get(endpoint, headers=headers, timeout=30)
                    if response.status_code == 200:
                        content = response.text
                        if self._is_base64(content):
                            try:
                                decoded = base64.b64decode(content).decode('utf-8')
                                return decoded
                            except (binascii.Error, UnicodeDecodeError) as e:
                                logger.warning(f"Base64デコードエラー: {str(e)}")
                                continue
                        return content
                    elif response.status_code == 404:
                        # 404の場合は次のエンドポイントを試す
                        break
                    elif response.status_code == 429:  # Rate limit
                        # レート制限の場合は長めに待機
                        time.sleep(retry_delay * 5)
                        continue
                    else:
                        # その他のエラーの場合はリトライ
                        time.sleep(retry_delay)
                        continue
                except requests.exceptions.Timeout:
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                        continue
                except requests.exceptions.RequestException as e:
                    logger.warning(f"Gerrit APIからの取得に失敗 ({attempt + 1}/{max_retries}): {str(e)}")
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                        continue
        
        # 最後に、GitHubから取得を試みる
        github_endpoints = [
            f"https://raw.githubusercontent.com/golang/go/HEAD/src/{file_path}",  # 最新版
            f"https://raw.githubusercontent.com/golang/go/master/src/{file_path}",  # master
            f"https://raw.githubusercontent.com/golang/go/main/src/{file_path}",    # main
        ]
        
        for endpoint in github_endpoints:
            for attempt in range(max_retries):
                try:
                    response = requests.get(endpoint, headers=headers, timeout=30)
                    if response.status_code == 200:
                        return response.text
                    elif response.status_code == 404:
                        # 404の場合は次のエンドポイントを試す
                        break
                    elif response.status_code == 429:  # Rate limit
                        # レート制限の場合は長めに待機
                        time.sleep(retry_delay * 5)
                        continue
                    else:
                        # その他のエラーの場合はリトライ
                        time.sleep(retry_delay)
                        continue
                except requests.exceptions.Timeout:
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                        continue
                except requests.exceptions.RequestException as e:
                    logger.warning(f"GitHubからの取得に失敗 ({attempt + 1}/{max_retries}): {str(e)}")
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                        continue
        
        return None
            
    def _is_base64(self, content: str) -> bool:
        """文字列がbase64エンコードされているかを判定します"""
        if not content:
            return False
        try:
            # base64文字セットのみを含むかチェック
            return bool(re.match(r'^[A-Za-z0-9+/]*={0,2}$', content))
        except TypeError:
            return False
            
    def _extract_functions_from_source(self, source_code: str) -> Dict[str, Tuple[int, int]]:
        """
        ソースコードから関数の情報を抽出します。
        
        Args:
            source_code: ソースコードの文字列
            
        Returns:
            関数名をキー、(開始行, 終了行)をバリューとする辞書
        """
        try:
            # Tree-sitterを使用して関数を抽出
            tree = self.parser.parse(source_code.encode())
            functions = {}
            
            # 関数を検索（関数宣言とメソッド宣言の両方を一度に取得）
            query_str = """
                (function_declaration) @function
                (method_declaration) @method
            """
            query = self.go_language.query(query_str)
            
            # クエリの実行
            captures = query.captures(tree.root_node)
            
            # 関数情報を収集
            current_func = None
            for node, _ in captures:
                try:
                    # 関数/メソッド名を取得
                    name_node = node.child_by_field_name("name")
                    if not name_node:
                        continue
                        
                    func_name = name_node.text.decode('utf-8')
                    
                    # メソッドの場合はレシーバー型を取得
                    if node.type == "method_declaration":
                        receiver_node = node.child_by_field_name("receiver")
                        if receiver_node:
                            type_node = receiver_node.child_by_field_name("type")
                            if type_node:
                                receiver_type = type_node.text.decode('utf-8').strip('*')
                                func_name = f"{receiver_type}.{func_name}"
                    
                    # 関数の種類に応じてプレフィックスを追加
                    if func_name.startswith("Test"):
                        func_name = f"test.{func_name}"
                    elif func_name.startswith("Benchmark"):
                        func_name = f"benchmark.{func_name}"
                    elif func_name.startswith("Example"):
                        func_name = f"example.{func_name}"
                    
                    # 関数の位置情報を取得（前後のコメントや空行も含める）
                    start_line = node.start_point[0] + 1  # 0-based to 1-based
                    end_line = node.end_point[0] + 1      # 0-based to 1-based
                    
                    # 前のコメントを含める
                    prev_node = node.prev_sibling
                    while prev_node and prev_node.type in ["comment", "empty_statement"]:
                        start_line = prev_node.start_point[0] + 1
                        prev_node = prev_node.prev_sibling
                    
                    # 後ろの空行を含める
                    next_node = node.next_sibling
                    while next_node and next_node.type == "empty_statement":
                        end_line = next_node.end_point[0] + 1
                        next_node = next_node.next_sibling
                    
                    functions[func_name] = (start_line, end_line)
                    current_func = func_name
                    logger.debug(f"Found function/method: {func_name} ({start_line}-{end_line})")
                    
                except Exception as inner_e:
                    logger.warning(f"Error processing function {current_func if current_func else 'unknown'}: {str(inner_e)}")
                    continue
            
            return functions
            
        except Exception as e:
            logger.error(f"Error in _extract_functions: {str(e)}")
            return {}

    def _extract_functions_from_diff(self, diff_info: Dict, repo_content: str, repo_functions: Dict[str, Tuple[int, int]]) -> Set[str]:
        """
        diff情報から変更された関数を特定します。
        
        Args:
            diff_info: diff情報（changed_lines: 変更された行番号のセット、diff_content: diff内容のリスト）
            repo_content: 現在のリポジトリのファイル内容
            repo_functions: 現在のリポジトリの関数情報 {関数名: (開始行, 終了行)}
            
        Returns:
            変更された関数名のセット
        """
        try:
            changed_lines = diff_info.get('changed_lines', set())
            diff_content = diff_info.get('diff_content', [])
            
            if not changed_lines and not diff_content:
                return set()
            
            changed_functions = set()
            
            # 方法1: diffの内容から直接関数名を抽出
            functions_in_diff = self._extract_function_names_from_content(diff_content)
            logger.debug(f"Functions found in diff content: {functions_in_diff}")
            
            # 方法2: 変更された行番号から関数を特定
            functions_by_line_numbers = set()
            for func_name, (start_line, end_line) in repo_functions.items():
                # 関数の範囲内に変更された行があるかチェック
                for changed_line in changed_lines:
                    if start_line <= changed_line <= end_line:
                        functions_by_line_numbers.add(func_name)
                        logger.debug(f"Function {func_name} changed by line number (line {changed_line} in range {start_line}-{end_line})")
                        break
            
            # 両方の方法で検出された関数を統合
            changed_functions = functions_in_diff.union(functions_by_line_numbers)
            
            # 現在のリポジトリに存在する関数のみをフィルタリング
            valid_changed_functions = set()
            for func_name in changed_functions:
                if func_name in repo_functions:
                    valid_changed_functions.add(func_name)
                else:
                    # 部分マッチを試す（プレフィックスなしの関数名で検索）
                    base_func_name = func_name
                    if '.' in func_name:
                        base_func_name = func_name.split('.')[-1]
                    
                    for repo_func_name in repo_functions.keys():
                        if repo_func_name.endswith(base_func_name):
                            valid_changed_functions.add(repo_func_name)
                            logger.debug(f"Matched {func_name} to existing function {repo_func_name}")
                            break
            
            return valid_changed_functions
            
        except Exception as e:
            logger.error(f"Error extracting functions from diff: {str(e)}")
            return set()

    def _extract_function_names_from_content(self, diff_content: List[str]) -> Set[str]:
        """
        diff内容から関数名を抽出します（tree-sitterを使用）。
        
        Args:
            diff_content: diff内容の行のリスト
            
        Returns:
            抽出された関数名のセット
        """
        try:
            if not diff_content:
                return set()
            
            # diff内容を結合してソースコードとして扱う
            combined_content = '\n'.join(diff_content)
            
            # tree-sitterを使って関数を抽出
            try:
                tree = self.parser.parse(combined_content.encode())
                functions = set()
                
                # 関数を検索（関数宣言とメソッド宣言の両方）
                query_str = """
                    (function_declaration) @function
                    (method_declaration) @method
                """
                query = self.go_language.query(query_str)
                
                # クエリの実行
                captures = query.captures(tree.root_node)
                
                for node, _ in captures:
                    try:
                        # 関数/メソッド名を取得
                        name_node = node.child_by_field_name("name")
                        if not name_node:
                            continue
                            
                        func_name = name_node.text.decode('utf-8')
                        
                        # メソッドの場合はレシーバー型を取得
                        if node.type == "method_declaration":
                            receiver_node = node.child_by_field_name("receiver")
                            if receiver_node:
                                type_node = receiver_node.child_by_field_name("type")
                                if type_node:
                                    receiver_type = type_node.text.decode('utf-8').strip('*')
                                    func_name = f"{receiver_type}.{func_name}"
                        
                        # 関数の種類に応じてプレフィックスを追加
                        if func_name.startswith("Test"):
                            func_name = f"test.{func_name}"
                        elif func_name.startswith("Benchmark"):
                            func_name = f"benchmark.{func_name}"
                        elif func_name.startswith("Example"):
                            func_name = f"example.{func_name}"
                        
                        functions.add(func_name)
                        logger.debug(f"Found function in diff: {func_name}")
                        
                    except Exception as inner_e:
                        logger.warning(f"Error processing function in diff: {str(inner_e)}")
                        continue
                
                return functions
                
            except Exception as tree_e:
                logger.warning(f"Tree-sitter parsing failed, falling back to regex: {str(tree_e)}")
                # tree-sitterでの解析に失敗した場合は正規表現にフォールバック
                return self._extract_function_names_regex(diff_content)
                
        except Exception as e:
            logger.error(f"Error extracting function names from diff content: {str(e)}")
            return set()

    def _extract_function_names_regex(self, diff_content: List[str]) -> Set[str]:
        """
        正規表現を使ってdiff内容から関数名を抽出します（フォールバック用）。
        
        Args:
            diff_content: diff内容の行のリスト
            
        Returns:
            抽出された関数名のセット
        """
        try:
            patterns = [
                r'func\s+([A-Za-z0-9_]+)\s*\(',  # 通常の関数
                r'func\s*\([^)]*\*?([A-Za-z0-9_]+)\)\s*([A-Za-z0-9_]+)\s*\(',  # メソッド
                r'func\s+Test([A-Za-z0-9_]+)\s*\(',  # テスト関数
                r'func\s+Benchmark([A-Za-z0-9_]+)\s*\(',  # ベンチマーク関数
                r'func\s+Example([A-Za-z0-9_]+)\s*\('  # 例示関数
            ]
            
            extracted_functions = set()
            
            for line in diff_content:
                line = line.strip()
                if not line or not line.startswith('func'):
                    continue
                    
                for pattern in patterns:
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        if len(match.groups()) == 1:
                            func_name = match.group(1)
                        elif len(match.groups()) == 2:
                            # メソッドの場合
                            receiver = match.group(1).strip().strip('*')
                            func_name = f"{receiver}.{match.group(2)}"
                        else:
                            continue
                            
                        # テスト関数などの場合はプレフィックスを追加
                        if 'Test' in pattern:
                            func_name = f"test.{func_name}"
                        elif 'Benchmark' in pattern:
                            func_name = f"benchmark.{func_name}"
                        elif 'Example' in pattern:
                            func_name = f"example.{func_name}"
                            
                        extracted_functions.add(func_name)
                        logger.debug(f"Found function in diff (regex): {func_name}")
            
            return extracted_functions
            
        except Exception as e:
            logger.error(f"Error in regex function extraction: {str(e)}")
            return set()

    def _extract_cl_number(self, proposal_content: str) -> Optional[str]:
        """
        提案の内容からCL番号とURLを抽出します。
        
        Args:
            proposal_content: 提案の内容
            
        Returns:
            CL番号、または見つからなかった場合はNone
        """
        try:
            # 文字列の前処理
            # 1. 改行を空白に置換
            # 2. 連続する空白を1つに
            # 3. 両端の空白を削除
            content = proposal_content
            
            # デバッグ用：入力内容の確認
            self.logger.debug(f"Original content length: {len(proposal_content)}")
            self.logger.debug(f"Original content (first 200 chars): {repr(proposal_content[:200])}")
            
            # 1. Gerrit URLからの抽出
            url_patterns = [
                r'Change\s+https?://go\.dev/cl/(\d+)',                            # Change https://go.dev/cl/形式
                r'https://go-review\.googlesource\.com/c/(?:go|tools)/\+/(\d+)',  # 新形式（サブプロジェクト対応）
                r'https://go-review\.googlesource\.com/c/(?:go/\+/)?(\d+)',       # 新形式
                r'(?:https://)?go\.dev/cl/(\d+)',                                 # go.dev形式（httpsありなし両方）
                r'(?:https://)?golang\.org/cl/(\d+)',                            # 短縮形式（httpsありなし両方）
                r'https://codereview\.go\.dev/(\d+)',                             # 古い形式
            ]
            
            for pattern in url_patterns:
                url_match = re.search(pattern, content, re.MULTILINE | re.DOTALL | re.IGNORECASE)
                if url_match:
                    self.logger.debug(f"Found CL with pattern '{pattern}': {url_match.group(1)}")
                    self.logger.debug(f"Match span: {url_match.span()}")
                    return url_match.group(1)
                else:
                    self.logger.debug(f"No match for pattern: {pattern}")
                    # パターンが見つからない場合、その部分の文字列を詳しく調べる
                    if 'go.dev/cl/' in content:
                        pos = content.find('go.dev/cl/')
                        self.logger.debug(f"Found 'go.dev/cl/' at position {pos}")
                        self.logger.debug(f"Surrounding context: {repr(content[max(0, pos-20):min(len(content), pos+40)])}")
            
            # 2. テキスト形式からの抽出（URLが見つからない場合のフォールバック）
            text_patterns = [
                r'(?:^|\s)CL[:\s]+(\d+)',         # "CL 12345" or "CL: 12345"
                r'(?:^|\s)cl/(\d+)',              # "cl/12345"
                r'\[CL (\d+)\]',                  # [CL 12345]
                r'Change-Id: I[a-f0-9]+',         # Gerrit Change-ID
            ]
            
            for pattern in text_patterns:
                text_match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE | re.DOTALL)
                if text_match and len(text_match.groups()) > 0:
                    self.logger.debug(f"Found CL with text pattern '{pattern}': {text_match.group(1)}")
                    self.logger.debug(f"Match span: {text_match.span()}")
                    return text_match.group(1)
                else:
                    self.logger.debug(f"No match for text pattern: {pattern}")
            
            self.logger.debug("No CL number found in content")
            return None
            
        except Exception as e:
            self.logger.error(f"CL番号の抽出に失敗しました: {str(e)}")
            self.logger.error(f"Exception details: {repr(e)}")
            return None

    def extract_cl_links(self, proposal_content: str, comments: Optional[List[Dict]] = None) -> Set[str]:
        """
        プロポーザルの内容とコメントからCL番号を抽出します。
        
        Args:
            proposal_content: プロポーザルの内容
            comments: GitHubコメントのリスト（オプション）
            
        Returns:
            抽出されたCL番号のセット
        """
        all_cl_ids = set()
        
        # プロポーザル本文からの抽出
        cl_id = self._extract_cl_number(proposal_content)
        if cl_id:
            all_cl_ids.add(cl_id)
        
        # コメントからの抽出
        if comments:
            for comment in comments:
                body = comment.get('body', '')
                if body:
                    cl_id = self._extract_cl_number(body)
                    if cl_id:
                        all_cl_ids.add(cl_id)
        
        return all_cl_ids 

    def _normalize_function_content(self, content: str) -> str:
        """
        関数の内容を正規化します。
        - 空白を正規化
        - コメントを削除
        - 空行を削除
        
        Args:
            content: 関数の内容
            
        Returns:
            正規化された関数の内容
        """
        # 行ごとに処理
        normalized_lines = []
        for line in content.splitlines():
            # 行をトリム
            line = line.strip()
            
            # 空行をスキップ
            if not line:
                continue
                
            # コメントをスキップ
            if line.startswith('//') or line.startswith('/*') or line.endswith('*/'):
                continue
                
            # インラインコメントを削除
            if '//' in line:
                line = line[:line.index('//')].strip()
                
            # 空白を正規化（連続する空白を1つに）
            line = ' '.join(line.split())
            
            if line:  # 正規化後も内容がある行のみ追加
                normalized_lines.append(line)
                
        return '\n'.join(normalized_lines)

    def _is_function_modified(self, cl_content: str, repo_content: str, cl_range: Tuple[int, int], repo_range: Tuple[int, int]) -> bool:
        """
        関数が変更されているかを判定します。
        
        Args:
            cl_content: CLのファイル内容
            repo_content: 現在のリポジトリのファイル内容
            cl_range: CLでの関数の行範囲 (開始行, 終了行)
            repo_range: リポジトリでの関数の行範囲 (開始行, 終了行)
            
        Returns:
            変更されている場合はTrue、そうでない場合はFalse
        """
        # 関数の内容を取得
        cl_start, cl_end = cl_range
        repo_start, repo_end = repo_range
        
        cl_func_content = '\n'.join(cl_content.splitlines()[cl_start-1:cl_end])
        repo_func_content = '\n'.join(repo_content.splitlines()[repo_start-1:repo_end])
        
        # 内容を正規化
        normalized_cl = self._normalize_function_content(cl_func_content)
        normalized_repo = self._normalize_function_content(repo_func_content)
        
        # 正規化後の内容を比較
        return normalized_cl != normalized_repo 