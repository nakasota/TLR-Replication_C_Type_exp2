#!/usr/bin/env python3
"""
Go リポジトリ構造解析器: 
現在のGoリポジトリからすべての.goファイルを解析し、go_repo_structure.jsonと同じ形式でデータを作成する
find_relative_func.pyと同じtree-sitter手法を使用して関数・メソッドを抽出する
"""

import os
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any

# tree-sitterのパスを追加
sys.path.append('/workspace/tree-sitter-build/lib')

try:
    import tree_sitter as ts
    TREE_SITTER_AVAILABLE = True
except ImportError:
    TREE_SITTER_AVAILABLE = False
    print("⚠️ tree-sitterが利用できません。")
    sys.exit(1)

class GoRepoStructureCreator:
    """Go リポジトリの構造を解析し、JSONファイルを作成する"""
    
    def __init__(self, repo_path: str):
        """初期化"""
        self.repo_path = Path(repo_path)
        self.go_parser = None
        self._init_tree_sitter()
    
    def _init_tree_sitter(self):
        """tree-sitter Go パーサーを初期化"""
        try:
            # Goライブラリのパス
            go_lib_path = '/workspace/tree-sitter-build/lib/go.so'
            if not os.path.exists(go_lib_path):
                print(f"⚠️ Goライブラリが見つかりません: {go_lib_path}")
                sys.exit(1)
            
            # パーサーを初期化
            GO_LANGUAGE = ts.Language(go_lib_path, 'go')
            self.go_parser = ts.Parser()
            self.go_parser.set_language(GO_LANGUAGE)
            print("✓ tree-sitter Goパーサーを初期化")
            
        except Exception as e:
            print(f"❌ tree-sitter初期化エラー: {str(e)}")
            sys.exit(1)
    
    def analyze_repository(self) -> Dict[str, Any]:
        """リポジトリ全体を解析"""
        print(f"🔍 Goリポジトリ解析開始: {self.repo_path}")
        
        if not self.repo_path.exists():
            print(f"❌ リポジトリパスが存在しません: {self.repo_path}")
            return {}
        
        # すべての.goファイルを検索
        go_files = list(self.repo_path.rglob("*.go"))
        print(f"✓ {len(go_files)}個の.goファイルを発見")
        
        repo_structure = {}
        processed_count = 0
        
        for go_file in go_files:
            try:
                # 相対パスを計算（リポジトリルートからの相対パス）
                relative_path = go_file.relative_to(self.repo_path)
                relative_path_str = str(relative_path).replace(os.sep, '/')
                
                # ファイル解析
                file_analysis = self._analyze_go_file(go_file)
                if file_analysis:
                    repo_structure[relative_path_str] = file_analysis
                    processed_count += 1
                
                # 進捗表示
                if processed_count % 100 == 0:
                    print(f"📊 進捗: {processed_count}/{len(go_files)} ファイル処理完了")
                    
            except Exception as e:
                print(f"⚠️ ファイル処理エラー {go_file}: {str(e)}")
                continue
        
        print(f"✅ 解析完了: {processed_count}個のファイルを処理")
        return repo_structure
    
    def _analyze_go_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """個別のGoファイルを解析"""
        try:
            # ファイル内容を読み込み
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # AST解析で関数を抽出
            functions = self._extract_functions_from_content(content)
            
            return {
                'content': content,
                'functions': functions
            }
            
        except Exception as e:
            print(f"⚠️ ファイル解析エラー {file_path}: {str(e)}")
            return None
    
    def _extract_functions_from_content(self, content: str) -> Dict[str, Any]:
        """コンテンツからtree-sitterを使って関数を抽出"""
        if not self.go_parser:
            return {}
        
        try:
            # ASTを解析
            tree = self.go_parser.parse(bytes(content, 'utf8'))
            root_node = tree.root_node
            
            # すべての関数を収集
            all_functions = []
            self._collect_all_functions(root_node, all_functions)
            
            # 行の開始オフセットを計算
            line_start_offsets = self._get_line_start_offsets(content)
            
            # 関数情報を構築
            functions = {}
            for func_node in all_functions:
                func_info = self._build_function_info(func_node, content, line_start_offsets)
                if func_info and func_info['name']:
                    functions[func_info['name']] = {
                        'start_line': func_info['start_line'],
                        'end_line': func_info['end_line'],
                        'content': func_info['content']
                    }
            
            return functions
            
        except Exception as e:
            print(f"⚠️ AST解析エラー: {str(e)}")
            return {}
    
    def _collect_all_functions(self, node, all_functions):
        """再帰的に関数ノードを収集（find_relative_func.pyと完全一致版）"""
        # 通常の関数・メソッド
        if node.type in ("function_declaration", "method_declaration"):
            all_functions.append(node)
        
        # 変数宣言から名前付き関数リテラルを検出
        if node.type == "var_declaration":
            for child in node.children:
                if child.type == "var_spec":
                    var_name = None
                    function_literal = None
                    for vchild in child.children:
                        if vchild.type == "identifier":
                            var_name = vchild.text.decode('utf-8') if isinstance(vchild.text, bytes) else vchild.text
                        elif vchild.type == "expression_list":
                            for expr_child in vchild.children:
                                if expr_child.type == "function_literal":
                                    function_literal = expr_child
                                    break
                    if var_name and function_literal:
                        all_functions.append({
                            'type': 'named_function_literal',
                            'name': var_name,
                            'node': function_literal,
                            'start_point': function_literal.start_point,
                            'end_point': function_literal.end_point
                        })
        
        # インターフェースメソッド
        if node.type == "type_declaration":
            for child in node.children:
                if child.type == "type_spec":
                    for grandchild in child.children:
                        if grandchild.type == "interface_type":
                            for method in grandchild.children:
                                if method.type == "method_spec":
                                    all_functions.append(method)
        
        # 子ノードを再帰的に処理
        for child in node.children:
            self._collect_all_functions(child, all_functions)
    

    
    def _build_function_info(self, func_node, content: str, line_start_offsets: List[int]) -> Optional[Dict[str, Any]]:
        """関数ノードから関数情報を構築"""
        try:
            # 関数名を抽出
            func_name = self._extract_function_name(func_node)
            if not func_name or func_name == "unknown":
                return None
            
            # 辞書型の場合（named_function_literal）
            if isinstance(func_node, dict):
                actual_node = func_node['node']
                start_byte = actual_node.start_byte
                end_byte = actual_node.end_byte
            else:
                start_byte = func_node.start_byte
                end_byte = func_node.end_byte
            
            start_line = self._byte_to_line(start_byte, line_start_offsets) + 1  # 1ベース
            end_line = self._byte_to_line(end_byte, line_start_offsets) + 1
            
            # 関数の内容を抽出
            func_content = content[start_byte:end_byte]
            
            return {
                'name': func_name,
                'start_line': start_line,
                'end_line': end_line,
                'content': func_content
            }
            
        except Exception as e:
            print(f"⚠️ 関数情報構築エラー: {str(e)}")
            return None
    
    def _extract_function_name(self, func_node):
        """関数ノードから関数名を抽出（find_relative_func.pyと完全一致版）"""
        if isinstance(func_node, dict) and func_node.get('type') == 'named_function_literal':
            return func_node.get('name', 'unknown')
        if not isinstance(func_node, dict) and hasattr(func_node, 'type') and func_node.type == 'method_spec':
            for child in getattr(func_node, 'children', []):
                if child.type in ['identifier', 'field_identifier']:
                    name = child.text
                    if isinstance(name, bytes):
                        name = name.decode('utf-8')
                    return name.strip()
        if not isinstance(func_node, dict) and hasattr(func_node, 'type') and func_node.type == 'function_declaration':
            for child in getattr(func_node, 'children', []):
                if child.type == 'identifier':
                    name = child.text
                    if isinstance(name, bytes):
                        name = name.decode('utf-8')
                    return name.strip()
        elif not isinstance(func_node, dict) and hasattr(func_node, 'type') and func_node.type == 'method_declaration':
            found_receiver = False
            method_name = None
            for child in getattr(func_node, 'children', []):
                if child.type == 'parameter_list' and not found_receiver:
                    found_receiver = True
                    continue
                elif child.type in ['identifier', 'field_identifier'] and found_receiver:
                    name = child.text
                    if isinstance(name, bytes):
                        name = name.decode('utf-8')
                    method_name = name.strip()
                    break
            if method_name:
                return method_name
        return "unknown"
    
    def _get_line_start_offsets(self, content: str) -> List[int]:
        """各行の開始バイトオフセットを計算"""
        offsets = [0]
        for i, char in enumerate(content):
            if char == '\n':
                offsets.append(i + 1)
        return offsets
    
    def _byte_to_line(self, byte_offset: int, line_start_offsets: List[int]) -> int:
        """バイトオフセットから行番号を計算（0ベース）"""
        for line_num, start_offset in enumerate(line_start_offsets):
            if line_num + 1 < len(line_start_offsets):
                if start_offset <= byte_offset < line_start_offsets[line_num + 1]:
                    return line_num
            else:
                if start_offset <= byte_offset:
                    return line_num
        return len(line_start_offsets) - 1

def main():
    """メイン処理"""
    # リポジトリパス
    repo_path = "../data/repos/go"
    
    # 出力ファイルパス
    output_path = "../data/ground_truth/go_repo_structure.json"
    
    print("🚀 Go リポジトリ構造解析開始")
    print(f"📁 リポジトリパス: {repo_path}")
    print(f"📄 出力ファイル: {output_path}")
    
    # 解析実行
    creator = GoRepoStructureCreator(repo_path)
    repo_structure = creator.analyze_repository()
    
    if not repo_structure:
        print("❌ 解析結果が空です")
        return
    
    # 結果をJSONファイルに保存
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(repo_structure, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 解析完了！")
        print(f"📊 処理したファイル数: {len(repo_structure)}")
        print(f"💾 結果を保存: {output_path}")
        
        # 統計情報を表示
        total_functions = sum(len(file_data.get('functions', {})) for file_data in repo_structure.values())
        print(f"🔧 検出した関数数: {total_functions}")
        
    except Exception as e:
        print(f"❌ ファイル保存エラー: {str(e)}")

if __name__ == "__main__":
    main()
