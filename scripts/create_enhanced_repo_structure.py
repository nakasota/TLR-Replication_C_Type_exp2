#!/usr/bin/env python3

import json
import os
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Union
from tree_sitter import Language, Parser
from tqdm import tqdm

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EnhancedRepoStructureBuilder:
    def __init__(self):
        """Initialize the builder with Tree-sitter."""
        self.parser = Parser()
        self.language = Language('tree-sitter-build/lib/tree-sitter-go.so', 'go')
        self.parser.set_language(self.language)
        
        # 結果を格納する辞書
        self.repo_structure = {}
        
    def _extract_functions(self, source_code: str) -> Dict[str, Tuple[int, int, str]]:
        """
        ソースコードから関数の情報を抽出します。
        
        Args:
            source_code: ソースコードの文字列
            
        Returns:
            関数名をキー、(開始行, 終了行, 関数の内容)をバリューとする辞書
        """
        try:
            # Tree-sitterを使用して関数を抽出
            tree = self.parser.parse(source_code.encode())
            functions = {}
            
            # 関数定義を検索
            query = self.language.query('''
                (function_declaration
                    name: (identifier) @func_name) @function
                    
                (method_declaration
                    name: (field_identifier) @method_name) @method
            ''')
            
            # クエリの実行
            captures = query.captures(tree.root_node)
            
            # 関数情報を収集
            for node, capture_name in captures:
                if capture_name in ('func_name', 'method_name'):
                    func_name = node.text.decode('utf-8')
                    func_node = node.parent
                    
                    # 行番号は0-basedなので1を加える
                    start_line = func_node.start_point[0] + 1
                    end_line = func_node.end_point[0] + 1
                    
                    # 関数の内容を取得
                    lines = source_code.split('\n')
                    func_content = '\n'.join(lines[start_line-1:end_line])
                    
                    functions[func_name] = (start_line, end_line, func_content)
            
            return functions
            
        except Exception as e:
            logger.error(f"Error in _extract_functions: {e}")
            return {}
            
    def process_file(self, file_path: str, repo_root: str) -> None:
        """
        ファイルを処理し、内容と関数情報を抽出します。
        
        Args:
            file_path: ファイルパス
            repo_root: リポジトリのルートディレクトリ
        """
        try:
            # ファイルの完全パスを取得
            full_path = os.path.join(repo_root, file_path)
            
            # ファイルが存在しない場合はスキップ
            if not os.path.exists(full_path):
                logger.warning(f"File does not exist: {full_path}")
                return
            
            # ファイルの内容を読み込む
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 関数情報を抽出
            functions = self._extract_functions(content)
            
            # 結果を保存
            self.repo_structure[file_path] = {
                'content': content,
                'functions': {
                    name: {
                        'start_line': info[0],
                        'end_line': info[1],
                        'content': info[2]
                    }
                    for name, info in functions.items()
                }
            }
            
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {e}")
            
    def build_structure(self, input_file: str, repo_root: str, output_file: str) -> None:
        """
        リポジトリ構造を構築し、JSONファイルに保存します。
        
        Args:
            input_file: 入力のgo_repo_structure.jsonのパス
            repo_root: リポジトリのルートディレクトリ
            output_file: 出力のenhanced_repo_structure.jsonのパス
        """
        try:
            # 既存の構造を読み込む
            with open(input_file, 'r') as f:
                existing_structure = json.load(f)
            
            # 各ファイルを処理
            logger.info(f"Processing {len(existing_structure)} files...")
            for file_path in tqdm(existing_structure.keys()):
                if file_path.endswith('.go'):
                    self.process_file(file_path, repo_root)
            
            # 結果を保存
            logger.info(f"Saving results to {output_file}...")
            with open(output_file, 'w') as f:
                json.dump(self.repo_structure, f, indent=2)
            
            logger.info("Done!")
            
        except Exception as e:
            logger.error(f"Error building structure: {e}")

def main():
    # コマンドライン引数の処理
    import argparse
    parser = argparse.ArgumentParser(description='Generate enhanced repository structure with file contents and function information.')
    parser.add_argument('--input', default='data/preprocess/go_repo_structure.json',
                      help='Input go_repo_structure.json file path')
    parser.add_argument('--repo-root', default='data/repos/go',
                      help='Root directory of the Go repository')
    parser.add_argument('--output', default='data/preprocess/go_repo_structure.json',
                      help='Output go_repo_structure.json file path')
    args = parser.parse_args()
    
    # 構造の構築
    builder = EnhancedRepoStructureBuilder()
    builder.build_structure(args.input, args.repo_root, args.output)

if __name__ == '__main__':
    main() 