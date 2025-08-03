import json
import os
import re
import shutil
import logging
from pathlib import Path
from tqdm import tqdm
from typing import Dict, List, Optional, Set, Tuple
from tree_sitter import Language, Parser
from datetime import datetime
import argparse
import glob
import requests

# Add workspace root to Python path
import sys
workspace_root = Path(__file__).parent.parent
sys.path.append(str(workspace_root))

from scripts.cl_change_fetcher import CLChangeFetcher
from scripts.cl_change_fetcher_improved import ImprovedCLChangeFetcher
from methods.baseline_v3.src.utils.go_repo_loader import GoRepoLoader

# ロガーの設定を変更（エラーのみ表示）
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class Statistics:
    def __init__(self):
        """
        統計情報を初期化します。
        """
        self.total_proposals = 0
        self.successful_proposals = 0
        self.failed_proposals = 0
        self.no_changes_proposals = 0
        self.non_go_only_proposals = 0
        self.changed_files = set()
        self.changed_functions = set()
        self.processed_cls = set()
    
    def add_changed_file(self, file_path: str) -> None:
        """
        変更されたファイルを追加します。
        """
        self.changed_files.add(file_path)
    
    def add_changed_function(self, function_path: str) -> None:
        """
        変更された関数を追加します。
        """
        self.changed_functions.add(function_path)
    
    def add_processed_cl(self, cl_number: str) -> None:
        """
        処理されたCLを追加します。
        """
        self.processed_cls.add(cl_number)
    
    def print_statistics(self) -> None:
        """
        統計情報を表示します。
        """
        print("\n📈 処理結果の統計:")
        print(f"   - 処理した提案: {self.total_proposals}個")
        print(f"   - 成功した提案: {self.successful_proposals}個")
        print(f"   - 失敗した提案: {self.failed_proposals}個")
        print(f"   - 変更なしの提案: {self.no_changes_proposals}個")
        print(f"   - Go以外のファイルのみの提案: {self.non_go_only_proposals}個")
        print(f"   - 変更されたファイル: {len(self.changed_files)}個")
        print(f"   - 変更された関数: {len(self.changed_functions)}個")
        print(f"   - 処理されたCL数: {len(self.processed_cls)}個")
    
    def to_dict(self) -> Dict:
        """
        統計情報を辞書として返します。
        """
        return {
            'total_proposals': self.total_proposals,
            'successful_proposals': self.successful_proposals,
            'failed_proposals': self.failed_proposals,
            'no_changes_proposals': self.no_changes_proposals,
            'non_go_only_proposals': self.non_go_only_proposals,
            'changed_files': list(self.changed_files),
            'changed_functions': list(self.changed_functions),
            'processed_cls': list(self.processed_cls)
        }

class GroundTruthAnalyzer:
    def __init__(self, use_improved_approach: bool = False):
        """
        Ground Truth解析器を初期化します。
        
        Args:
            use_improved_approach: 改良版アプローチを使用するかどうか
        """
        self.use_improved_approach = use_improved_approach
        self.parser = None
        self.repo_loader = GoRepoLoader(repo_structure_path=str(workspace_root / 'data/preprocess/go_repo_structure.json'))
        
        # CLFetcherの初期化を確実に行う
        if use_improved_approach:
            self.initialize_tree_sitter()
            self.cl_fetcher = ImprovedCLChangeFetcher(repo_loader=self.repo_loader)
        else:
            self.cl_fetcher = CLChangeFetcher()
            
    def initialize_tree_sitter(self):
        """
        Tree-sitterを初期化します。
        """
        if self.parser is not None:
            return
            
        # Tree-sitterの初期化
        GO_LANGUAGE = Language('tree-sitter-build/tree-sitter-go/src/parser.so', 'go')
        self.parser = Parser()
        self.parser.set_language(GO_LANGUAGE)
        print("✓ tree-sitter Go parser loaded from tree-sitter-build/tree-sitter-go/src/parser.so")
        
        print("✓ Tree-sitterの初期化完了")
        print("✓ Goリポジトリデータの読み込み完了\n")

    def process_proposal(self, proposal_path: str) -> Dict:
        """
        提案から変更された関数の情報を抽出します。
        - CLのコード変更が現在のリポジトリに残っていない場合は許容します
        - 関数が現在のリポジトリに存在しない場合も許容します
        """
        try:
            # 提案の内容を読み込む
            with open(proposal_path, 'r') as f:
                proposal_content = f.read()
            
            # CLの変更を取得
            changes = self.cl_fetcher.fetch_changes_from_proposal(proposal_content)
            if not changes:
                print(f"⚠️  {os.path.basename(proposal_path)}: CLの変更を取得できませんでした")
                return {
                    'proposal_file': proposal_path,
                    'error': 'no_cl_changes',
                    'modified_files': [],
                    'directory_level_changes': [],
                    'file_level_changes': [],
                    'function_level_changes': []
                }
            
            # CLの基本情報を取得
            cl_number = changes.get('cl_number')
            if not cl_number:
                print(f"⚠️  {os.path.basename(proposal_path)}: CL番号が見つかりませんでした")
                return {
                    'proposal_file': proposal_path,
                    'error': 'no_cl_number',
                    'modified_files': [],
                    'directory_level_changes': [],
                    'file_level_changes': [],
                    'function_level_changes': []
                }
            
            print(f"📝 {os.path.basename(proposal_path)} (CL {cl_number})")
            
            # 変更されたファイルと関数の情報を収集
            files = changes.get('files', {})
            dir_changes = set()
            file_changes = set()
            function_changes = []
            
            for file_path, file_info in files.items():
                if not file_path.endswith('.go'):
                    print(f"   ℹ️  {file_path}: Goファイルではないためスキップします")
                    continue
                
                # ディレクトリレベルの変更を追加
                dir_path = '/'.join(file_path.split('/')[:-1])
                dir_changes.add(dir_path)
                
                # ファイルレベルの変更を追加
                file_changes.add(file_path)
                
                # ソースコードを取得（失敗しても続行）
                source_code = self.repo_loader.get_file_content(file_path)
                if not source_code:
                    print(f"   ℹ️  {file_path}: 現在のリポジトリにファイルが存在しません（許容）")
                    continue
                
                # 変更された関数の情報を取得
                modified_functions = file_info.get('modified_functions', [])
                if not modified_functions:
                    print(f"   ℹ️  {file_path}: 変更された関数はありません")
                    continue
                
                print(f"   ✓ {file_path}: {len(modified_functions)}個の関数を処理")
                
                # 関数の詳細情報を抽出
                functions = self._extract_functions_from_source(source_code)
                
                for func_name in modified_functions:
                    if func_name in functions:
                        start_line, end_line = functions[func_name]
                        function_changes.append([
                            int(cl_number),
                            file_path,
                            func_name,
                            start_line,
                            end_line
                        ])
                    else:
                        print(f"   ℹ️  {file_path}: 関数 {func_name} は現在のリポジトリに存在しません（許容）")
            
            return {
                'proposal_file': proposal_path,
                'cl_number': cl_number,
                'status': changes.get('status'),
                'subject': changes.get('subject'),
                'modified_files': list(files.keys()),
                'directory_level_changes': list(dir_changes),
                'file_level_changes': list(file_changes),
                'function_level_changes': function_changes
            }
            
        except Exception as e:
            print(f"❌ {os.path.basename(proposal_path)}: エラーが発生しました: {str(e)}")
            return {
                'proposal_file': proposal_path,
                'error': str(e),
                'modified_files': [],
                'directory_level_changes': [],
                'file_level_changes': [],
                'function_level_changes': []
            }

    def _extract_functions_from_source(self, source_code: str) -> Dict[str, Tuple[int, int]]:
        """
        ソースコードから関数名と行番号の情報を抽出します。
        
        Returns:
            Dict[str, Tuple[int, int]]: 関数名をキーとし、(開始行, 終了行)のタプルを値とする辞書
        """
        if self.use_improved_approach:
            return self.cl_fetcher._extract_functions_from_source(source_code)
        else:
            return self.cl_fetcher._extract_functions_from_source(source_code)

    def save_ground_truth(self, results: List[Dict], output_dir: str):
        """
        ground truthを3つの異なるレベル（関数、ファイル、ディレクトリ）で保存します。
        """
        print("\n📊 Ground Truthの保存中...")
        os.makedirs(output_dir, exist_ok=True)
        
        # 処理結果の統計を計算
        total_proposals = len(results)
        successful_proposals = len([r for r in results if not 'error' in r])
        failed_proposals = len([r for r in results if 'error' in r])
        total_files = sum(len(r.get('modified_files', [])) for r in results)
        total_functions = sum(len(r.get('function_level_changes', [])) for r in results)
        
        # 統計情報を追加
        ground_truth = {
            'statistics': {
                'total_proposals': total_proposals,
                'successful_proposals': successful_proposals,
                'failed_proposals': failed_proposals,
                'total_modified_files': total_files,
                'total_modified_functions': total_functions
            },
            'results': results
        }
        
        # 詳細なground truthを保存
        detailed_path = os.path.join(output_dir, 'detailed_ground_truth.json')
        with open(detailed_path, 'w') as f:
            json.dump(ground_truth, f, indent=2)
        print(f"✓ 詳細なGround Truth: {detailed_path}")
        
        # ファイルレベルのground truthを保存
        file_level = {
            'statistics': ground_truth['statistics'],
            'results': [{
                'proposal_file': r['proposal_file'],
                'cl_number': r.get('cl_number'),
                'status': r.get('status'),
                'subject': r.get('subject'),
                'file_level_changes': r.get('file_level_changes', [])
            } for r in results]
        }
        file_level_path = os.path.join(output_dir, 'file_level_ground_truth.json')
        with open(file_level_path, 'w') as f:
            json.dump(file_level, f, indent=2)
        print(f"✓ ファイルレベルGround Truth: {file_level_path}")
        
        # ディレクトリレベルのground truthを保存
        dir_level = {
            'statistics': ground_truth['statistics'],
            'results': [{
                'proposal_file': r['proposal_file'],
                'cl_number': r.get('cl_number'),
                'status': r.get('status'),
                'subject': r.get('subject'),
                'directory_level_changes': r.get('directory_level_changes', [])
            } for r in results]
        }
        dir_level_path = os.path.join(output_dir, 'directory_level_ground_truth.json')
        with open(dir_level_path, 'w') as f:
            json.dump(dir_level, f, indent=2)
        print(f"✓ ディレクトリレベルGround Truth: {dir_level_path}")
        
        print(f"\n📈 処理結果の統計:")
        print(f"   - 処理した提案: {total_proposals}個")
        print(f"   - 成功した提案: {successful_proposals}個")
        print(f"   - 失敗した提案: {failed_proposals}個")
        print(f"   - 変更されたファイル: {total_files}個")
        print(f"   - 変更された関数: {total_functions}個")
        
        print("\n✨ Ground Truthの生成が完了しました！")

def process_proposal(proposal_file: str, stats: Statistics) -> Dict:
    """
    提案を処理し、変更された関数の情報を抽出します。
    
    Args:
        proposal_file: 提案ファイルのパス
        stats: 統計情報
        
    Returns:
        解析結果を含む辞書
    """
    global analyzer
    result = analyzer.process_proposal(proposal_file)
    
    # 統計情報を更新
    if not 'error' in result:
        # ファイルレベルの変更を追加
        for file_path in result.get('file_level_changes', []):
            stats.add_changed_file(file_path)
        
        # 関数レベルの変更を追加
        for func_info in result.get('function_level_changes', []):
            stats.add_changed_function(f"{func_info['file_path']}:{func_info['function_name']}")
        
        # CLを追加
        if 'cl_number' in result:
            stats.add_processed_cl(result['cl_number'])
    
    return result

def extract_cl_numbers(file_path: str) -> List[str]:
    """
    提案ファイルからCL番号を抽出します。
    
    Args:
        file_path: 提案ファイルのパス
        
    Returns:
        CL番号のリスト
    """
    cl_numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # CL番号を検索
        matches = re.finditer(r'CL[^\d]*(\d+)', content)
        for match in matches:
            cl_numbers.append(match.group(1))
            
    except Exception as e:
        print(f"⚠️ CL番号の抽出中にエラー: {str(e)}")
        
    return cl_numbers

def save_ground_truth(output_dir: str, stats: Statistics, results: List[str]) -> None:
    """
    Ground Truthを保存します。
    
    Args:
        output_dir: 出力ディレクトリ
        stats: 統計情報
        results: 成功した提案のリスト
    """
    global analyzer
    
    print("\n📊 Ground Truthの保存中...")
    
    # 成功した提案のみを処理
    successful_results = []
    for proposal_file in results:
        result = analyzer.process_proposal(proposal_file)
        if not 'error' in result:
            successful_results.append(result)
    
    # 詳細なGround Truthを保存
    detailed_ground_truth_path = os.path.join(output_dir, 'detailed_ground_truth.json')
    with open(detailed_ground_truth_path, 'w') as f:
        json.dump(successful_results, f, indent=2, ensure_ascii=False)
    print(f"✓ 詳細なGround Truth: {detailed_ground_truth_path}")
    
    # ファイルレベルのGround Truthを保存
    file_level_ground_truth = []
    for result in successful_results:
        file_level_ground_truth.extend(result.get('file_level_changes', []))
    
    file_level_ground_truth_path = os.path.join(output_dir, 'file_level_ground_truth.json')
    with open(file_level_ground_truth_path, 'w') as f:
        json.dump(list(set(file_level_ground_truth)), f, indent=2, ensure_ascii=False)
    print(f"✓ ファイルレベルGround Truth: {file_level_ground_truth_path}")
    
    # ディレクトリレベルのGround Truthを保存
    directory_level_ground_truth = []
    for result in successful_results:
        directory_level_ground_truth.extend(result.get('directory_level_changes', []))
    
    directory_level_ground_truth_path = os.path.join(output_dir, 'directory_level_ground_truth.json')
    with open(directory_level_ground_truth_path, 'w') as f:
        json.dump(list(set(directory_level_ground_truth)), f, indent=2, ensure_ascii=False)
    print(f"✓ ディレクトリレベルGround Truth: {directory_level_ground_truth_path}")

def fetch_cl_info(cl_number: str) -> Optional[Dict]:
    """
    CLの基本情報を取得します。
    
    Args:
        cl_number: CL番号
        
    Returns:
        CLの情報を含む辞書、または取得失敗時はNone
    """
    url = f"https://go-review.googlesource.com/changes/{cl_number}"
    print(f"🔍 Trying endpoint for CL info: {url}")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 最初の行（)]}' を削除）
            data = response.text.split('\n', 1)[1]
            cl_info = json.loads(data)
            print(f"✅ Successfully fetched CL info from {url}")
            if cl_info.get('status') == 'MERGED':
                print("CL", cl_number, "is merged")
            return cl_info
    except Exception as e:
        print(f"⚠️ Failed to fetch CL info: {str(e)}")
    
    return None

def fetch_cl_changes(cl_number: str) -> Optional[Dict]:
    """
    CLの変更内容を取得します。
    
    Args:
        cl_number: CL番号
        
    Returns:
        CLの変更情報を含む辞書、または取得失敗時はNone
    """
    url = f"https://go-review.googlesource.com/changes/{cl_number}/revisions/current/files"
    print(f"🔍 Trying endpoint: {url}")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 最初の行（)]}' を削除）
            data = response.text.split('\n', 1)[1]
            changes = json.loads(data)
            print(f"✅ Successfully fetched file changes from {url}")
            return changes
    except Exception as e:
        print(f"⚠️ Failed to fetch CL changes: {str(e)}")
    
    return None

def analyze_cl_changes(cl_number: str, cl_info: Dict, cl_changes: Dict, proposal_name: str) -> Dict:
    """
    CLの変更を解析します。
    
    Args:
        cl_number: CL番号
        cl_info: CLの基本情報
        cl_changes: CLの変更情報
        proposal_name: 提案ファイル名
        
    Returns:
        解析結果を含む辞書
    """
    print(f"🔍 CL {cl_number} の改良版解析を開始")
    
    # Goファイルのみを抽出
    go_files = [f for f in cl_changes.keys() if f.endswith('.go')]
    print(f"📂 処理対象Goファイル: {len(go_files)}個")
    
    result = {
        'cl_number': cl_number,
        'subject': cl_info.get('subject', ''),
        'modified_files': [],
        'file_level_changes': [],  # ファイルレベルの変更
        'function_level_changes': [],  # 関数レベルの変更
        'directory_level_changes': set()  # ディレクトリレベルの変更
    }
    
    for file_path in go_files:
        print(f"🔄 改良版アプローチで処理中: {file_path}")
        print(f"Processing {file_path} with advanced approach...")
        
        file_info = cl_changes[file_path]
        normalized_path = file_path.lstrip('/')
        directory = os.path.dirname(normalized_path)
        
        # ファイルの変更情報を収集
        file_result = {
            'file_path': normalized_path,
            'directory': directory,
            'lines_changed': file_info.get('lines_inserted', 0) + file_info.get('lines_deleted', 0),
            'content_sample': file_info.get('content', [])[:3],  # 最初の3行をサンプルとして保存
            'functions': []
        }
        
        # 関数の変更を解析
        try:
            current_content = fetch_current_file_content(normalized_path)
            if current_content:
                functions = analyze_functions(current_content)
                file_result['functions'] = functions
                print(f"  ✓ {file_path}: {len(functions)}個の関数を処理")
                
                # ファイルレベルの変更を追加
                result['file_level_changes'].append(normalized_path)
                
                # ディレクトリレベルの変更を追加
                result['directory_level_changes'].add(directory)
                
                # 関数レベルの変更を追加
                for func_name in functions:
                    result['function_level_changes'].append({
                        'file_path': normalized_path,
                        'function_name': func_name
                    })
            else:
                print(f"⚠️ {file_path}: 現在のファイル内容を取得できませんでした")
                continue
        except Exception as e:
            print(f"⚠️ {file_path}: 関数解析中にエラー: {str(e)}")
            continue
            
        if file_result['functions']:
            result['modified_files'].append(file_result)
        else:
            print(f"  ⚪ {file_path}: 関数変更なし")
            
    # setをリストに変換
    result['directory_level_changes'] = list(result['directory_level_changes'])
            
    print(f"📊 CL {cl_number} 解析完了:")
    print(f"  - 処理ファイル数: {len(result['modified_files'])}/{len(go_files)}")
    print(f"  - 検出関数数: {sum(len(f['functions']) for f in result['modified_files'])}個")
    
    return result

def fetch_current_file_content(file_path: str) -> Optional[str]:
    """
    現在のリポジトリからファイルの内容を取得します。
    
    Args:
        file_path: ファイルパス
        
    Returns:
        ファイルの内容、または取得失敗時はNone
    """
    # src/を除去（もしあれば）
    normalized_path = file_path.replace('src/', '', 1)
    url = f"https://raw.githubusercontent.com/golang/go/HEAD/src/{normalized_path}"
    print(f"Trying to fetch from: {url}")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception:
        pass
        
    return None

def analyze_functions(content: str) -> List[str]:
    """
    ファイル内の関数を解析します。
    
    Args:
        content: ファイルの内容
        
    Returns:
        検出された関数名のリスト
    """
    functions = []
    # 簡単な正規表現で関数を検出（より正確な解析には tree-sitter を使用）
    pattern = r'func\s+(\([^)]+\)\s+)?([A-Za-z0-9_]+)'
    matches = re.finditer(pattern, content)
    for match in matches:
        func_name = match.group(2)
        if func_name:
            functions.append(func_name)
            print(f"  ✓ 変更を検出: {func_name} (現在のリポジトリに存在)")
            
    return functions

def main():
    parser = argparse.ArgumentParser(description='CLの変更を解析してGround Truthを生成します')
    parser.add_argument('--test-proposals-dir', required=True, help='テスト用提案のディレクトリ')
    parser.add_argument('--output-dir', required=True, help='出力ディレクトリ')
    args = parser.parse_args()
    
    # 出力ディレクトリを作成
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Tree-sitterの初期化（一度だけ）
    print("🔧 初期化中（改良版アプローチを使用）...")
    global analyzer
    analyzer = GroundTruthAnalyzer(use_improved_approach=True)
    
    # 提案ファイルを取得（README.mdを除外）
    proposal_files = [f for f in glob.glob(os.path.join(args.test_proposals_dir, '*.md'))
                     if not f.endswith('README.md')]
    
    print(f"🔍 {len(proposal_files)}個の提案を処理します...")
    print("-" * 50)
    
    # 統計情報の初期化
    stats = Statistics()
    stats.total_proposals = len(proposal_files)
    
    # 結果を保存するためのリスト
    results = []
    
    try:
        for proposal_file in tqdm(proposal_files, desc="Processing proposals", ncols=100):
            result = analyzer.process_proposal(proposal_file)
            results.append(result)
            
            if 'error' in result:
                stats.failed_proposals += 1
            else:
                stats.successful_proposals += 1
                
    except KeyboardInterrupt:
        print("\n\n⚠️ 処理が中断されました。これまでの結果を保存します...")
    finally:
        # 結果を保存
        analyzer.save_ground_truth(results, args.output_dir)
        print("\n✨ Ground Truthの生成が完了しました！")
        stats.print_statistics()

if __name__ == '__main__':
    main() 