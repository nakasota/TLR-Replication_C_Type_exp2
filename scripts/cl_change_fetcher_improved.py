#!/usr/bin/env python3
"""
改良版CLChangeFetcher: より正確な関数変更検出

このバージョンでは以下のアプローチを使用します：
1. CLのファイル全体をtree-sitterで分析して関数を取得
2. diff情報から変更された行の内容を取得  
3. 変更された行の内容と関数の内容を比較
4. 変更にヒットした関数をCLで変更された関数として特定
"""

import json
import re
import requests
import time
import base64
import binascii
import urllib.parse
from typing import Dict, List, Optional, Set, Tuple, Any
import logging
import tree_sitter

logger = logging.getLogger(__name__)

class SimpleRepoLoader:
    """シンプルなリポジトリローダー実装"""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = repo_path
        self.logger = logging.getLogger(__name__)
    
    def get_file_content(self, file_path: str) -> Optional[str]:
        """ファイルの内容を取得します"""
        try:
            import os
            full_path = os.path.join(self.repo_path, file_path)
            if os.path.exists(full_path):
                with open(full_path, 'r', encoding='utf-8') as f:
                    return f.read()
            return None
        except Exception as e:
            self.logger.warning(f"Error reading file {file_path}: {str(e)}")
            return None
    
    def get_all_files(self) -> List[str]:
        """リポジトリ内の全ファイルのリストを取得します"""
        try:
            import os
            all_files = []
            for root, _, files in os.walk(self.repo_path):
                for file in files:
                    if file.endswith('.go'):
                        rel_path = os.path.relpath(os.path.join(root, file), self.repo_path)
                        all_files.append(rel_path)
            return all_files
        except Exception as e:
            self.logger.warning(f"Error listing files: {str(e)}")
            return []

class ImprovedCLChangeFetcher:
    def __init__(self, repo_loader=None):
        """
        Initialize the improved CL change fetcher.
        
        Args:
            repo_loader: Repository loader instance for accessing current repository content
        """
        self.repo_loader = repo_loader
        self.logger = logging.getLogger(__name__)
        
        # Initialize tree-sitter parser
        self.go_language = None
        self.parser = None
        self._initialize_tree_sitter()

    def _initialize_tree_sitter(self):
        """tree-sitterパーサーを初期化します。"""
        try:
            import os
            # パーサーのパスを検索
            possible_paths = [
                'tree-sitter-build/tree-sitter-go/src/parser.so',
                'tree-sitter-build/lib/tree-sitter-go.so',
                'tree-sitter-build/tree-sitter-go/libtree-sitter-go.so',
                'tree-sitter-build/tree-sitter-go/parser.so',
                os.path.join(os.path.dirname(__file__), '../tree-sitter-build/tree-sitter-go/src/parser.so'),
                os.path.join(os.path.dirname(__file__), '../tree-sitter-build/lib/tree-sitter-go.so')
            ]
            
            parser_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    parser_path = path
                    break
            
            if not parser_path:
                raise RuntimeError("Could not find tree-sitter-go parser in any expected location. Please ensure the parser is built correctly.")
            
            from tree_sitter import Language
            self.go_language = Language(parser_path, 'go')
            self.parser = tree_sitter.Parser()
            self.parser.set_language(self.go_language)
            logger.info(f"✓ tree-sitter Go parser loaded from {parser_path}")
        
        except ImportError as e:
            logger.error(f"tree-sitter module not found: {str(e)}")
            logger.error("Please install tree-sitter: pip install tree-sitter")
            raise
        except RuntimeError as e:
            logger.error(f"tree-sitter-go parser not found: {str(e)}")
            logger.error("Please build the parser using the build script in tree-sitter-build/")
            raise
        except Exception as e:
            logger.error(f"tree-sitter initialization failed: {str(e)}")
            raise

    def extract_changed_functions_advanced(self, cl_number: str, file_path: str) -> Set[str]:
        """
        新しいアプローチで変更された関数を抽出します。
        
        フロー:
        1. CLから変更されたファイルとディレクトリパスを取得
        2. diff情報から実際の変更内容を取得
        3. 変更されたファイルをtree-sitterで解析して関数を抽出
        4. diff変更内容と関数内容をマッチングして変更された関数を特定
        5. 現在のリポジトリでディレクトリパスの存在確認
        6. 該当ディレクトリ内のファイルで関数名の一致確認
        
        Args:
            cl_number: CL番号
            file_path: ファイルパス
            
        Returns:
            変更された関数名のセット（現在のリポジトリに存在する関数のみ）
        """
        try:
            self.logger.info(f"Processing {file_path} with advanced approach...")
            
            # CLの基本情報を取得
            cl_info = self._get_cl_info(cl_number)
            if not cl_info:
                self.logger.warning(f"Failed to get CL info for {cl_number}")
                return set()
            
            # ファイル変更情報を取得
            file_changes = self._get_file_changes(cl_number)
            if not file_changes:
                self.logger.warning(f"Failed to get file changes for {cl_number}")
                return set()
            
            # ファイルパスを正規化（src/プレフィックスを除去）
            normalized_file_path = file_path
            if normalized_file_path.startswith('src/'):
                normalized_file_path = normalized_file_path[4:]
            
            # ディレクトリパスを取得
            directory_path = '/'.join(normalized_file_path.split('/')[:-1]) if '/' in normalized_file_path else ''
            self.logger.info(f"  📂 正規化ファイルパス: {normalized_file_path}")
            self.logger.info(f"  📂 ディレクトリパス: {directory_path}")
            
            # 2. diff情報から変更内容を取得
            diff_info = self._get_file_diff_content(cl_number, file_path)
            if not diff_info or not diff_info.get('changed_line_contents'):
                self.logger.warning(f"  ⚠️ スキップ: {file_path} (diff情報を取得できません)")
                return set()
            
            self.logger.info(f"  📊 変更行数: {len(diff_info.get('changed_line_contents', set()))}")
            self.logger.info(f"  📊 変更内容サンプル: {list(diff_info.get('changed_line_contents', set()))[:3]}")
            
            # 3. CLのファイル内容を取得してtree-sitterで解析
            cl_content = self._get_cl_file_content(cl_number, file_path)
            if not cl_content:
                self.logger.warning(f"  ⚠️ スキップ: {file_path} (CLの内容を取得できません)")
                return set()
            
            cl_functions = self._extract_functions_from_source(cl_content)
            if not cl_functions:
                self.logger.warning(f"  ⚠️ スキップ: {file_path} (CLから関数を抽出できません)")
                return set()
            
            self.logger.info(f"  📊 CL内関数数: {len(cl_functions)}")
            self.logger.info(f"  📊 CL内関数サンプル: {list(cl_functions.keys())[:3]}")
            
            # 4. diff変更内容と関数内容をマッチングして変更された関数を特定
            changed_functions_in_cl = self._find_changed_functions_by_content_matching(
                cl_content, cl_functions, diff_info
            )
            
            self.logger.info(f"  📊 CL内で変更された関数数: {len(changed_functions_in_cl)}")
            if changed_functions_in_cl:
                self.logger.info(f"  📊 変更された関数: {changed_functions_in_cl}")
            
            if not changed_functions_in_cl:
                self.logger.warning(f"  ⚠️ スキップ: {file_path} (変更された関数が見つかりません)")
                return set()
            
            # 5. 現在のリポジトリでディレクトリパスの存在確認
            if not self.repo_loader:
                self.logger.warning(f"  ⚠️ スキップ: {file_path} (repo_loaderが設定されていません)")
                return set()
            
            # ディレクトリ内のファイル一覧を取得（正規化されたパスを使用）
            directory_files = self._get_files_in_directory(directory_path)
            if not directory_files:
                self.logger.warning(f"  ⚠️ スキップ: {directory_path} (現在のリポジトリにディレクトリが存在しません)")
                return set()
            
            self.logger.info(f"  📊 ディレクトリ内ファイル数: {len(directory_files)}")
            self.logger.info(f"  📊 ディレクトリ内ファイルサンプル: {directory_files[:3]}")
            
            # 6. 該当ディレクトリ内のファイルで関数名の一致確認
            validated_functions = self._validate_functions_in_current_repo(
                changed_functions_in_cl, directory_files, normalized_file_path
            )
            
            self.logger.info(f"  ✨ 最終的に検出された関数: {len(validated_functions)}個")
            if validated_functions:
                self.logger.info(f"  ✨ 検出された関数: {validated_functions}")
            
            return validated_functions
            
        except Exception as e:
            self.logger.error(f"Error in advanced function extraction for {file_path}: {str(e)}")
            import traceback
            self.logger.error(traceback.format_exc())
            return set()
    
    def _get_files_in_directory(self, directory_path: str) -> List[str]:
        """
        現在のリポジトリの指定されたディレクトリ内のGoファイル一覧を取得します。
        
        Args:
            directory_path: ディレクトリパス
            
        Returns:
            ディレクトリ内のGoファイルパスのリスト
        """
        try:
            if not self.repo_loader:
                return []
            
            # リポジトリローダーから該当ディレクトリのファイル一覧を取得
            all_files = self.repo_loader.get_all_files()
            
            # 指定されたディレクトリ内のGoファイルをフィルタリング
            directory_files = []
            for file_path in all_files:
                file_dir = '/'.join(file_path.split('/')[:-1]) if '/' in file_path else ''
                if file_dir == directory_path and file_path.endswith('.go'):
                    directory_files.append(file_path)
            
            self.logger.debug(f"  📁 ディレクトリ {directory_path} 内のGoファイル: {len(directory_files)}個")
            return directory_files
            
        except Exception as e:
            self.logger.warning(f"Error getting files in directory {directory_path}: {str(e)}")
            return []
    
    def _validate_functions_in_current_repo(self, changed_functions: Set[str], 
                                          directory_files: List[str], 
                                          original_file_path: str) -> Set[str]:
        """
        現在のリポジトリ内で変更された関数の存在を確認します。
        ファイルパスと関数名の完全一致のみを確認します。
        
        Args:
            changed_functions: CLで変更された関数名のセット
            directory_files: 確認対象のディレクトリ内ファイルリスト
            original_file_path: 元のファイルパス
            
        Returns:
            現在のリポジトリに存在する関数名のセット
        """
        try:
            if not self.repo_loader:
                self.logger.warning("repo_loader is not available")
                return set()
                
            validated_functions = set()
            
            # 元のファイルパスが現在のリポジトリに存在するかチェック
            original_file_content = self.repo_loader.get_file_content(original_file_path)
            if original_file_content:
                self.logger.debug(f"  📄 元ファイル {original_file_path} が現在のリポジトリに存在")
                original_functions = self._extract_functions_from_source(original_file_content)
                
                # 関数名の完全一致をチェック
                for func_name in changed_functions:
                    if func_name in original_functions:
                        validated_functions.add(func_name)
                        self.logger.info(f"  ✓ 変更を検出: {func_name} (元ファイル内で確認)")
            else:
                self.logger.debug(f"  ⚠️ 元ファイル {original_file_path} が現在のリポジトリに存在しません")
            
            return validated_functions
            
        except Exception as e:
            self.logger.error(f"Error validating functions in current repo: {str(e)}")
            return set()
    
    def _get_cl_file_content(self, cl_number: str, file_path: str) -> Optional[str]:
        """
        CLのファイル内容を取得します。
        
        Args:
            cl_number: CL番号
            file_path: ファイルパス
            
        Returns:
            ファイルの内容、または取得に失敗した場合はNone
        """
        # Gerrit APIのエンドポイント
        gerrit_endpoints = [
            f"https://go-review.googlesource.com/changes/{cl_number}/revisions/current/files/{urllib.parse.quote_plus(file_path)}/content",
            f"https://go-review.googlesource.com/changes/go~{cl_number}/revisions/current/files/{urllib.parse.quote_plus(file_path)}/content"
        ]
        
        headers = {'Accept': 'text/plain'}
        max_retries = 3  # 最大リトライ回数
        retry_delay = 2  # 基本リトライ待機時間（秒）
        
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
                                self.logger.warning(f"Base64デコードエラー: {str(e)}")
                                continue
                        return content
                    elif response.status_code == 404:
                        # 404の場合は次のエンドポイントを試す
                        break
                    elif response.status_code == 429:  # レート制限
                        # レート制限の場合は長めに待機
                        wait_time = retry_delay * (5 ** attempt)  # 指数バックオフ
                        self.logger.warning(f"レート制限に達しました。{wait_time}秒待機します。")
                        time.sleep(wait_time)
                        continue
                    else:
                        # その他のエラーの場合はリトライ
                        wait_time = retry_delay * (2 ** attempt)  # 指数バックオフ
                        self.logger.warning(f"APIリクエストエラー（ステータスコード: {response.status_code}）。{wait_time}秒後にリトライします。")
                        time.sleep(wait_time)
                        continue
                except requests.exceptions.Timeout:
                    wait_time = retry_delay * (2 ** attempt)
                    self.logger.warning(f"タイムアウトが発生しました。{wait_time}秒後にリトライします。")
                    if attempt < max_retries - 1:
                        time.sleep(wait_time)
                        continue
                except requests.exceptions.RequestException as e:
                    wait_time = retry_delay * (2 ** attempt)
                    self.logger.warning(f"リクエストエラーが発生しました（{attempt + 1}/{max_retries}）: {str(e)}")
                    if attempt < max_retries - 1:
                        time.sleep(wait_time)
                        continue
        
        return None

    def _get_file_diff_content(self, cl_number: str, file_path: str) -> Optional[Dict]:
        """
        diff情報から変更された行の内容を取得します。
        
        Returns:
            {
                'changed_line_contents': Set[str],  # 変更された行の内容のセット
                'added_line_contents': Set[str],    # 追加された行の内容のセット
                'deleted_line_contents': Set[str]   # 削除された行の内容のセット
            }
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
                        
                        changed_line_contents = set()
                        added_line_contents = set()
                        deleted_line_contents = set()
                        
                        # Gerrit diff形式の解析
                        if 'content' in diff_data:
                            for content_item in diff_data['content']:
                                # 追加された行の内容 (右側の変更)
                                if 'b' in content_item:
                                    for line_content in content_item['b']:
                                        line_stripped = line_content.strip()
                                        if line_stripped:  # 空行を除外
                                            added_line_contents.add(line_stripped)
                                            changed_line_contents.add(line_stripped)
                                
                                # 削除された行の内容 (左側の変更)
                                if 'a' in content_item:
                                    for line_content in content_item['a']:
                                        line_stripped = line_content.strip()
                                        if line_stripped:  # 空行を除外
                                            deleted_line_contents.add(line_stripped)
                                            changed_line_contents.add(line_stripped)
                                
                                # 変更なしの行（コンテキスト）は除外
                                # 'ab'は両側に存在する行なので、変更されていない
                        
                        self.logger.debug(f"Diff analysis for {file_path}: "
                                   f"added={len(added_line_contents)}, "
                                   f"deleted={len(deleted_line_contents)}, "
                                   f"total_changed={len(changed_line_contents)}")
                        
                        return {
                            'changed_line_contents': changed_line_contents,
                            'added_line_contents': added_line_contents,
                            'deleted_line_contents': deleted_line_contents
                        }
                    except json.JSONDecodeError as e:
                        self.logger.warning(f"JSON decode error for {endpoint}: {str(e)}")
                        continue
                elif response.status_code == 404:
                    self.logger.debug(f"Diff not found for {file_path} in CL {cl_number}")
                    break
                else:
                    self.logger.warning(f"Unexpected status code {response.status_code} for {endpoint}")
            except requests.exceptions.RequestException as e:
                self.logger.warning(f"Request failed for {endpoint}: {str(e)}")
                continue
        
        # Fallback: GitHub APIを使用してdiff情報を取得
        return self._get_github_diff_content(cl_number, file_path)
    
    def _get_github_diff_content(self, cl_number: str, file_path: str) -> Optional[Dict]:
        """
        GitHub APIを使用してdiff情報を取得します（フォールバック）。
        """
        try:
            # GitHubのcommit APIを使用
            github_url = f"https://api.github.com/repos/golang/go/commits"
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; GoProposalAnalyzer/1.0)',
                'Accept': 'application/vnd.github.v3+json',
            }
            
            # CL番号からcommit hashを検索（簡略化）
            # 実際の実装では、CL番号とcommit hashのマッピングが必要
            
            # 直接的なdiff取得を試行
            raw_github_url = f"https://raw.githubusercontent.com/golang/go/HEAD/{file_path}"
            response = requests.get(raw_github_url, headers=headers, timeout=30)
            
            if response.status_code == 200:
                # 現在のファイル内容を取得できた場合、
                # 簡単な行ベースの比較を行う
                current_content = response.text
                
                # CLの内容と比較
                cl_content = self._get_cl_file_content(cl_number, file_path)
                if cl_content:
                    return self._compare_file_contents(current_content, cl_content)
            
        except Exception as e:
            self.logger.warning(f"GitHub fallback failed: {str(e)}")
        
        return None
    
    def _compare_file_contents(self, content1: str, content2: str) -> Dict:
        """
        2つのファイル内容を比較してdiff情報を生成します。
        """
        try:
            lines1 = content1.splitlines()
            lines2 = content2.splitlines()
            
            added_line_contents = set()
            deleted_line_contents = set()
            changed_line_contents = set()
            
            # 簡単なdiff実装
            lines1_set = set(line.strip() for line in lines1 if line.strip())
            lines2_set = set(line.strip() for line in lines2 if line.strip())
            
            # 追加された行
            for line in lines2_set - lines1_set:
                added_line_contents.add(line)
                changed_line_contents.add(line)
            
            # 削除された行
            for line in lines1_set - lines2_set:
                deleted_line_contents.add(line)
                changed_line_contents.add(line)
            
            return {
                'changed_line_contents': changed_line_contents,
                'added_line_contents': added_line_contents,
                'deleted_line_contents': deleted_line_contents
            }
            
        except Exception as e:
            self.logger.error(f"Error comparing file contents: {str(e)}")
            return {
                'changed_line_contents': set(),
                'added_line_contents': set(),
                'deleted_line_contents': set()
            }

    def _find_changed_functions_by_content_matching(self, cl_content: str, cl_functions: Dict[str, Tuple[int, int]], diff_info: Dict) -> Set[str]:
        """
        diff情報と関数の内容を比較して、変更された関数を特定します。
        1. 変更された行が関数内に存在するかを確認
        2. 関数の内容全体が変更されているかを確認
        
        Args:
            cl_content: CLのファイル内容
            cl_functions: CLのファイル内の関数情報（関数名 -> (開始行, 終了行)）
            diff_info: diff情報
            
        Returns:
            変更された関数名のセット
        """
        try:
            changed_functions = set()
            changed_lines = diff_info.get('changed_line_contents', set())
            
            # 各関数について変更を確認
            for func_name, (start_line, end_line) in cl_functions.items():
                # 関数の内容を取得
                func_lines = cl_content.splitlines()[start_line - 1:end_line]
                func_content = set(line.strip() for line in func_lines if line.strip())
                
                # 1. 変更された行が関数内に存在するかを確認
                for changed_line in changed_lines:
                    if changed_line.strip() in func_content:
                        changed_functions.add(func_name)
                        self.logger.debug(f"  ✓ 関数内の行変更を検出: {func_name}")
                        break
                
                # 2. 関数の内容全体が変更されているかを確認
                if func_name not in changed_functions:  # まだ変更として検出されていない場合
                    func_content_str = '\n'.join(func_lines)
                    if func_content_str in changed_lines:
                        changed_functions.add(func_name)
                        self.logger.debug(f"  ✓ 関数の内容変更を検出: {func_name}")
            
            return changed_functions
            
        except Exception as e:
            self.logger.error(f"Error in content matching: {str(e)}")
            return set()

    def _extract_functions_from_source(self, source_code: str) -> Dict[str, Tuple[int, int]]:
        """
        ソースコードから関数の情報を抽出します（tree-sitterを使用）。
        """
        try:
            if not self.parser or not self.go_language:
                self.logger.error("Tree-sitter parser not available")
                return {}
            
            tree = self.parser.parse(source_code.encode('utf-8'))
            functions = {}
            
            def visit_node(node):
                if node.type == 'function_declaration':
                    # 関数名を取得
                    name_node = self._find_child_by_type(node, 'identifier')
                    if name_node:
                        func_name = source_code[name_node.start_byte:name_node.end_byte]
                        start_line = node.start_point[0] + 1
                        end_line = node.end_point[0] + 1
                        functions[func_name] = (start_line, end_line)
                        self.logger.debug(f"Found function: {func_name} ({start_line}-{end_line})")
                
                elif node.type == 'method_declaration':
                    # メソッド名を取得
                    name_node = self._find_child_by_type(node, 'field_identifier')
                    if name_node:
                        method_name = source_code[name_node.start_byte:name_node.end_byte]
                        start_line = node.start_point[0] + 1
                        end_line = node.end_point[0] + 1
                        functions[method_name] = (start_line, end_line)
                        self.logger.debug(f"Found method: {method_name} ({start_line}-{end_line})")
                
                # 子ノードを再帰的に処理
                for child in node.children:
                    visit_node(child)
            
            visit_node(tree.root_node)
            return functions
            
        except Exception as e:
            self.logger.error(f"Error in function extraction: {str(e)}")
            return {}
    
    def _find_child_by_type(self, node, node_type: str):
        """指定されたタイプの最初の子ノードを検索"""
        for child in node.children:
            if child.type == node_type:
                return child
        return None

    def fetch_changes_from_proposal(self, proposal_content: str) -> Optional[Dict]:
        """
        提案からCLの変更を取得します（従来のCLChangeFetcherとの互換性のため）
        """
        try:
            # 従来のCLChangeFetcherを使って基本情報を取得
            from scripts.cl_change_fetcher import CLChangeFetcher
            legacy_fetcher = CLChangeFetcher()
            
            # 基本的なCL情報を取得
            basic_changes = legacy_fetcher.fetch_changes_from_proposal(proposal_content)
            if not basic_changes:
                self.logger.warning("基本的なCL情報を取得できませんでした")
                return None
            
            cl_number = basic_changes.get('cl_number', '')
            self.logger.info(f"🔍 CL {cl_number} の改良版解析を開始")
            
            # 改良版アプローチで関数変更を検出
            enhanced_changes = basic_changes.copy()
            files = basic_changes.get('files', {})
            
            total_files = len([f for f in files.keys() if f.endswith('.go')])
            processed_files = 0
            total_functions_detected = 0
            
            self.logger.info(f"📂 処理対象Goファイル: {total_files}個")
            
            for file_path, file_info in files.items():
                if file_path.endswith('.go'):
                    self.logger.info(f"🔄 改良版アプローチで処理中: {file_path}")
                    
                    # 新しいアプローチで関数変更を検出
                    changed_functions = self.extract_changed_functions_advanced(
                        cl_number, file_path
                    )
                    
                    # 結果を更新
                    enhanced_changes['files'][file_path]['modified_functions'] = list(changed_functions)
                    
                    processed_files += 1
                    function_count = len(changed_functions)
                    total_functions_detected += function_count
                    
                    if function_count > 0:
                        self.logger.info(f"  ✅ {file_path}: {function_count}個の関数変更を検出")
                        # 関数名を表示（最大5個まで）
                        func_names = list(changed_functions)[:5]
                        self.logger.info(f"    関数: {', '.join(func_names)}" + 
                                  (f" (+{function_count-5}個)" if function_count > 5 else ""))
                    else:
                        self.logger.info(f"  ⚪ {file_path}: 関数変更なし")
            
            # 統計情報を出力
            self.logger.info(f"📊 CL {cl_number} 解析完了:")
            self.logger.info(f"  - 処理ファイル数: {processed_files}/{total_files}")
            self.logger.info(f"  - 検出関数数: {total_functions_detected}個")
            
            # メタデータを追加
            enhanced_changes['analysis_metadata'] = {
                'processed_files': processed_files,
                'total_go_files': total_files,
                'total_functions_detected': total_functions_detected,
                'analysis_method': 'improved_content_matching'
            }
            
            return enhanced_changes
            
        except Exception as e:
            self.logger.error(f"Error in fetch_changes_from_proposal: {str(e)}")
            return None

    def _is_base64(self, content: str) -> bool:
        """文字列がbase64エンコードされているかを判定します"""
        if not content:
            return False
        try:
            return bool(re.match(r'^[A-Za-z0-9+/]*={0,2}$', content))
        except TypeError:
            return False

    def _get_cl_info(self, cl_number: str) -> Optional[Dict[str, Any]]:
        """
        CLの基本情報を取得します。
        複数のエンドポイントを試し、アーカイブされたCLにも対応します。
        
        Args:
            cl_number: CL番号
            
        Returns:
            CL情報を含む辞書、または取得に失敗した場合はNone
        """
        endpoints = [
            # 標準的なエンドポイント
            f"https://go-review.googlesource.com/changes/{cl_number}",
            f"https://go-review.googlesource.com/changes/go~{cl_number}",
            # アーカイブされたCL用のエンドポイント
            f"https://go-review.googlesource.com/changes/{cl_number}?o=ALL_REVISIONS",
            f"https://go-review.googlesource.com/changes/go~{cl_number}?o=ALL_REVISIONS",
            # 古いCL用のエンドポイント
            f"https://go-review.googlesource.com/changes/{cl_number}?o=ALL_REVISIONS&o=DETAILED_ACCOUNTS",
            f"https://go-review.googlesource.com/changes/go~{cl_number}?o=ALL_REVISIONS&o=DETAILED_ACCOUNTS"
        ]
        
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'CLChangeFetcher/1.0'
        }
        
        max_retries = 5
        initial_retry_delay = 2
        max_retry_delay = 60
        
        for endpoint in endpoints:
            self.logger.info(f"🔍 Trying endpoint for CL info: {endpoint}")
            
            for attempt in range(max_retries):
                try:
                    retry_delay = min(initial_retry_delay * (2 ** attempt), max_retry_delay)
                    
                    response = requests.get(endpoint, headers=headers, timeout=30)
                    self.logger.debug(f"Response status: {response.status_code}")
                    
                    if response.status_code == 200:
                        content = response.text
                        if content.startswith(")]}'"):
                            content = content[4:]
                        try:
                            data = json.loads(content)
                            if data:
                                # CLの状態をチェック
                                status = data.get('status', '')
                                if status == 'ABANDONED':
                                    self.logger.warning(f"CL {cl_number} is abandoned")
                                elif status == 'MERGED':
                                    self.logger.info(f"CL {cl_number} is merged")
                                
                                self.logger.info(f"✅ Successfully fetched CL info from {endpoint}")
                                self.logger.info(f"CL Subject: {data.get('subject', 'N/A')}")
                                return data
                            else:
                                self.logger.warning(f"Empty response from {endpoint}")
                        except json.JSONDecodeError as je:
                            self.logger.warning(f"Invalid JSON response from {endpoint}: {str(je)}")
                            self.logger.debug(f"Response content: {content[:200]}...")
                    
                    elif response.status_code == 404:
                        self.logger.info(f"CL not found at {endpoint}")
                        break
                    
                    elif response.status_code == 429:
                        retry_after = int(response.headers.get('Retry-After', retry_delay))
                        self.logger.warning(f"Rate limit hit. Waiting {retry_after} seconds...")
                        time.sleep(retry_after)
                        continue
                    
                    elif response.status_code == 401:
                        self.logger.warning(f"Authentication required for {endpoint}")
                        break
                    
                    elif response.status_code == 410:
                        self.logger.warning(f"CL is gone (possibly archived) at {endpoint}")
                        continue
                    
                    else:
                        self.logger.warning(f"Unexpected status code {response.status_code} from {endpoint}")
                        if attempt < max_retries - 1:
                            self.logger.info(f"Retrying in {retry_delay} seconds...")
                            time.sleep(retry_delay)
                        continue
                
                except requests.exceptions.Timeout:
                    self.logger.warning(f"Timeout accessing {endpoint}")
                    if attempt < max_retries - 1:
                        self.logger.info(f"Retrying in {retry_delay} seconds...")
                        time.sleep(retry_delay)
                    continue
                
                except requests.exceptions.RequestException as e:
                    self.logger.warning(f"Network error accessing {endpoint}: {str(e)}")
                    if attempt < max_retries - 1:
                        self.logger.info(f"Retrying in {retry_delay} seconds...")
                        time.sleep(retry_delay)
                    continue
        
        self.logger.error(f"❌ Failed to fetch CL info for {cl_number} from all endpoints")
        return None

    def _get_file_changes(self, cl_number: str) -> Optional[Dict[str, Any]]:
        """
        CLのファイル変更情報を取得します。
        複数のエンドポイントを試し、アーカイブされたCLにも対応します。
        
        Args:
            cl_number: CL番号
            
        Returns:
            ファイル変更情報を含む辞書、または取得に失敗した場合はNone
        """
        endpoints = [
            # 標準的なエンドポイント
            f"https://go-review.googlesource.com/changes/{cl_number}/revisions/current/files",
            f"https://go-review.googlesource.com/changes/go~{cl_number}/revisions/current/files",
            # アーカイブされたCL用のエンドポイント
            f"https://go-review.googlesource.com/changes/{cl_number}/revisions/current/files?o=ALL_FILES",
            f"https://go-review.googlesource.com/changes/go~{cl_number}/revisions/current/files?o=ALL_FILES",
            # 古いCL用のエンドポイント
            f"https://go-review.googlesource.com/changes/{cl_number}/revisions/1/files",
            f"https://go-review.googlesource.com/changes/go~{cl_number}/revisions/1/files"
        ]
        
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'CLChangeFetcher/1.0'
        }
        
        max_retries = 5  # リトライ回数を増やす
        initial_retry_delay = 2
        max_retry_delay = 60  # 最大待機時間を60秒に設定
        
        for endpoint in endpoints:
            self.logger.info(f"🔍 Trying endpoint: {endpoint}")
            
            for attempt in range(max_retries):
                try:
                    # 指数バックオフによる待機時間の計算
                    retry_delay = min(initial_retry_delay * (2 ** attempt), max_retry_delay)
                    
                    response = requests.get(endpoint, headers=headers, timeout=30)
                    self.logger.debug(f"Response status: {response.status_code}")
                    
                    if response.status_code == 200:
                        # Gerrit APIは)]}'で始まるレスポンスを返すため、それを除去
                        content = response.text
                        if content.startswith(")]}'"):
                            content = content[4:]
                        try:
                            data = json.loads(content)
                            if data:
                                self.logger.info(f"✅ Successfully fetched file changes from {endpoint}")
                                return data
                            else:
                                self.logger.warning(f"Empty response from {endpoint}")
                        except json.JSONDecodeError as je:
                            self.logger.warning(f"Invalid JSON response from {endpoint}: {str(je)}")
                            self.logger.debug(f"Response content: {content[:200]}...")
                    
                    elif response.status_code == 404:
                        self.logger.info(f"CL not found at {endpoint}")
                        break  # 次のエンドポイントを試す
                    
                    elif response.status_code == 429:  # レート制限
                        retry_after = int(response.headers.get('Retry-After', retry_delay))
                        self.logger.warning(f"Rate limit hit. Waiting {retry_after} seconds...")
                        time.sleep(retry_after)
                        continue
                    
                    elif response.status_code == 401:
                        self.logger.warning(f"Authentication required for {endpoint}")
                        break  # 認証が必要な場合は次のエンドポイントを試す
                    
                    elif response.status_code == 410:
                        self.logger.warning(f"CL is gone (possibly archived) at {endpoint}")
                        continue  # アーカイブされている可能性があるので次のエンドポイントを試す
                    
                    else:
                        self.logger.warning(f"Unexpected status code {response.status_code} from {endpoint}")
                        if attempt < max_retries - 1:
                            self.logger.info(f"Retrying in {retry_delay} seconds...")
                            time.sleep(retry_delay)
                        continue
                
                except requests.exceptions.Timeout:
                    self.logger.warning(f"Timeout accessing {endpoint}")
                    if attempt < max_retries - 1:
                        self.logger.info(f"Retrying in {retry_delay} seconds...")
                        time.sleep(retry_delay)
                    continue
                
                except requests.exceptions.RequestException as e:
                    self.logger.warning(f"Network error accessing {endpoint}: {str(e)}")
                    if attempt < max_retries - 1:
                        self.logger.info(f"Retrying in {retry_delay} seconds...")
                        time.sleep(retry_delay)
                    continue
        
        self.logger.error(f"❌ Failed to fetch file changes for CL {cl_number} from all endpoints")
        return None

if __name__ == '__main__':
    # ロギングの設定
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # テスト用のCL番号とファイルパス
    test_cl = "458335"  # 以前成功したCLを使用
    test_file = "src/runtime/exec_freebsd.go"
    
    # リポジトリローダーとフェッチャーの初期化
    repo_loader = SimpleRepoLoader(".")
    fetcher = ImprovedCLChangeFetcher(repo_loader)
    
    # 変更された関数を取得
    changed_functions = fetcher.extract_changed_functions_advanced(test_cl, test_file)
    
    # 結果を表示
    print("\n=== 検出された変更関数 ===")
    for func in sorted(changed_functions):
        print(f"✓ {func}") 