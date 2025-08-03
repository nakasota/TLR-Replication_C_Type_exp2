#!/usr/bin/env python3
"""
拡張CLアナライザー: mdファイルからCL番号を抽出し、差分行番号を取得、
AST解析によって変更が属する関数を特定する
"""

import re
import json
import requests
import time
import logging
import argparse
import base64
import sys
import os
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path

# tree-sitterのパスを追加
sys.path.append('/workspace/tree-sitter-build/lib')

try:
    import tree_sitter as ts
    TREE_SITTER_AVAILABLE = True
except ImportError:
    TREE_SITTER_AVAILABLE = False
    print("⚠️ tree-sitterが利用できません。AST解析は無効化されます。")

# ログ設定
def log_info(msg):
    print(f"[INFO] {msg}")
def log_debug(msg):
    print(f"[DEBUG] {msg}")
def log_warning(msg):
    print(f"[WARNING] {msg}")
def log_error(msg):
    print(f"[ERROR] {msg}")

class EnhancedCLAnalyzer:
    """拡張されたCLアナライザー: 差分行とAST解析機能付き"""
    
    GERRIT_API_BASE = "https://go-review.googlesource.com"
    
    def __init__(self):
        """初期化"""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Enhanced-CL-Analyzer/1.0'
        })
        
        # tree-sitterパーサーの初期化
        self.go_parser = None
        if TREE_SITTER_AVAILABLE:
            self._init_tree_sitter()
    
    def _init_tree_sitter(self):
        """tree-sitter Go パーサーを初期化"""
        try:
            # Goライブラリのパス
            go_lib_path = '/workspace/tree-sitter-build/lib/go.so'
            if not os.path.exists(go_lib_path):
                log_warning(f"Goライブラリが見つかりません: {go_lib_path}")
                return
            
            # パーサーを初期化
            GO_LANGUAGE = ts.Language(go_lib_path, 'go')
            self.go_parser = ts.Parser()
            self.go_parser.set_language(GO_LANGUAGE)
            log_info("✓ tree-sitter Goパーサーを初期化")
            
        except Exception as e:
            log_error(f"tree-sitter初期化エラー: {str(e)}")
            self.go_parser = None
    
    def analyze_proposal(self, proposal_file_path: str) -> Dict[str, Any]:
        """提案ファイルからCLを抽出し、差分行とAST解析を実行"""
        log_info(f"拡張解析開始: {proposal_file_path}")
        
        # 1. mdファイルからCL番号を抽出
        content = self._read_file(proposal_file_path)
        if not content:
            return {'error': f'ファイル読み込み失敗: {proposal_file_path}'}
        
        cl_numbers = self._extract_cl_numbers(content)
        if not cl_numbers:
            return {'error': f'CL番号が見つかりません: {proposal_file_path}'}
        
        log_info(f"✓ {len(cl_numbers)}個のCL番号を検出: {cl_numbers}")
        
        # 2. 各CLの詳細解析
        cl_analyses = []
        
        for cl_number in cl_numbers:
            log_info(f"CL {cl_number} の詳細解析中...")
            
            cl_analysis = self._analyze_cl_detailed(cl_number)
            if cl_analysis:
                cl_analyses.append(cl_analysis)
                log_info(f"✓ CL {cl_number}: {len(cl_analysis.get('files', []))}個のファイルを解析")
            else:
                log_warning(f"⚠️ CL {cl_number}: 解析失敗")
            
            # API制限対策
            time.sleep(0.5)
        
        result = {
            'proposal_file': proposal_file_path,
            'cl_numbers': cl_numbers,
            'total_cls_analyzed': len(cl_analyses),
            'cl_analyses': cl_analyses,
            'tree_sitter_enabled': TREE_SITTER_AVAILABLE and self.go_parser is not None
        }
        
        log_info(f"✓ 完了: {len(cl_analyses)}個のCLを詳細解析")
        return result
    
    def _analyze_cl_detailed(self, cl_number: str) -> Optional[Dict[str, Any]]:
        """CLの詳細解析: 基本情報、diff、AST解析"""
        try:
            # 1. CL基本情報を取得
            basic_info = self._fetch_cl_info(cl_number)
            if not basic_info:
                return None
            
            # 2. 変更ファイル一覧を取得
            changed_files = self._fetch_file_list(cl_number)
            if not changed_files:
                return None
            
            # 3. 各ファイルの詳細解析
            file_analyses = []
            current_revision = basic_info.get('current_revision')
            
            if current_revision:
                for file_path, file_info in changed_files.items():
                    if file_path == '/COMMIT_MSG':
                        continue
                    
                    # Goファイルのみ処理
                    if not file_path.endswith('.go'):
                        continue
                    
                    file_analysis = self._analyze_file_detailed(
                        cl_number, file_path, file_info, current_revision
                    )
                    
                    if file_analysis:
                        file_analyses.append(file_analysis)
            
            return {
                'cl_number': cl_number,
                'subject': basic_info.get('subject', ''),
                'status': basic_info.get('status', ''),
                'current_revision': current_revision,
                'total_files_changed': len([f for f in changed_files.keys() if f != '/COMMIT_MSG']),
                'go_files_analyzed': len(file_analyses),
                'files': file_analyses
            }
            
        except Exception as e:
            log_error(f"CL {cl_number} 詳細解析エラー: {str(e)}")
            return None
    
    def _analyze_file_detailed(self, cl_number: str, file_path: str, 
                               file_info: Dict[str, Any], revision_id: str) -> Optional[Dict[str, Any]]:
        """ファイルの詳細解析: diff、内容、AST解析"""
        try:
            # 1. diff情報を取得
            diff_info = self._fetch_file_diff(cl_number, file_path)
            
            # 2. ファイル内容を取得（変更後）
            new_content = self._fetch_file_content(cl_number, file_path, revision_id)
            
            # 3. diff行番号を解析
            changed_lines = self._parse_diff_lines(diff_info) if diff_info else []
            
            # 4. AST解析（新しいファイル内容）
            ast_analysis = {}
            if self.go_parser and new_content:
                ast_analysis = self._analyze_go_ast(new_content, changed_lines)
            
            return {
                'file_path': file_path,
                'status': file_info.get('status', ''),
                'lines_inserted': file_info.get('lines_inserted', 0),
                'lines_deleted': file_info.get('lines_deleted', 0),
                'changed_lines': changed_lines,
                'content_size': len(new_content) if new_content else 0,
                'ast_analysis': ast_analysis
            }
            
        except Exception as e:
            log_error(f"ファイル {file_path} 詳細解析エラー: {str(e)}")
            return None
    
    def _fetch_file_diff(self, cl_number: str, file_path: str) -> Optional[str]:
        """ファイルのdiff情報を取得"""
        encoded_path = file_path.replace('/', '%2F')
        endpoints = [
            f"{self.GERRIT_API_BASE}/changes/{cl_number}/revisions/current/files/{encoded_path}/diff",
            f"{self.GERRIT_API_BASE}/changes/go~{cl_number}/revisions/current/files/{encoded_path}/diff"
        ]
        
        for endpoint in endpoints:
            try:
                response = self.session.get(endpoint, timeout=30)
                if response.status_code == 200:
                    content = response.text
                    if content.startswith(")]}'"):
                        content = content[4:]
                    return content
            except Exception:
                continue
        
        return None
    
    def _parse_diff_lines(self, diff_content: str) -> List[Dict[str, Any]]:
        """diff内容から変更行番号を解析"""
        if not diff_content:
            log_warning("diff_content が空です")
            return []
        
        try:
            # Gerrit APIのプレフィックスを除去
            content = diff_content
            if content.startswith(")]}'"):
                content = content[4:]
            
            # JSONとして解析を試行
            try:
                diff_data = json.loads(content)
                if 'content' in diff_data:
                    log_debug(f"Gerrit diff形式で解析開始、エントリ数: {len(diff_data['content'])}")
                    result = self._parse_gerrit_diff_format(diff_data)
                    log_info(f"Gerrit diff解析完了: {len(result)}行の変更を検出")
                    return result
            except json.JSONDecodeError:
                pass
            
            # JSON形式でない場合、unified diff形式として解析
            log_debug("unified diff形式として解析開始")
            result = self._parse_unified_diff_format(content)
            log_info(f"Unified diff解析完了: {len(result)}行の変更を検出")
            return result
            
        except Exception as e:
            log_error(f"diff解析エラー: {str(e)}")
            log_debug(f"diff内容（最初の500文字）: {diff_content[:500]}")
            return []
    
    def _parse_gerrit_diff_format(self, diff_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Gerrit API の diff 形式を解析"""
        changed_lines = []
        
        old_line_num = 1
        new_line_num = 1
        
        for diff_entry in diff_data.get('content', []):
            # 削除行 (only 'a' key)
            if 'a' in diff_entry and 'b' not in diff_entry:
                for line_text in diff_entry['a']:
                    changed_lines.append({
                        'type': 'deleted',
                        'old_line': old_line_num,
                        'content': line_text
                    })
                    old_line_num += 1
            
            # 追加行 (only 'b' key)
            elif 'b' in diff_entry and 'a' not in diff_entry:
                for line_text in diff_entry['b']:
                    changed_lines.append({
                        'type': 'added',
                        'new_line': new_line_num,
                        'content': line_text
                    })
                    new_line_num += 1
            
            # 変更行 (both 'a' and 'b' keys)
            elif 'a' in diff_entry and 'b' in diff_entry:
                # 削除部分
                for line_text in diff_entry['a']:
                    changed_lines.append({
                        'type': 'deleted',
                        'old_line': old_line_num,
                        'content': line_text
                    })
                    old_line_num += 1
                
                # 追加部分
                for line_text in diff_entry['b']:
                    changed_lines.append({
                        'type': 'added',
                        'new_line': new_line_num,
                        'content': line_text
                    })
                    new_line_num += 1
            
            # 変更されていない行 ('ab' key)
            elif 'ab' in diff_entry:
                # 変更されていない行の分だけ行番号を進める
                line_count = len(diff_entry['ab'])
                old_line_num += line_count
                new_line_num += line_count
        
        log_debug(f"抽出された変更行数: {len(changed_lines)}")
        return changed_lines
    
    def _parse_unified_diff_format(self, diff_content: str) -> List[Dict[str, Any]]:
        """unified diff形式を解析"""
        changed_lines = []
        lines = diff_content.split('\n')
        
        old_line_num = 0
        new_line_num = 0
        
        for line in lines:
            # ヘッダー行を解析
            if line.startswith('@@'):
                # @@ -old_start,old_count +new_start,new_count @@
                match = re.search(r'@@\s*-(\d+)(?:,\d+)?\s*\+(\d+)(?:,\d+)?\s*@@', line)
                if match:
                    old_line_num = int(match.group(1))
                    new_line_num = int(match.group(2))
                continue
            
            # 削除行
            if line.startswith('-') and not line.startswith('---'):
                changed_lines.append({
                    'type': 'deleted',
                    'old_line': old_line_num,
                    'content': line[1:]  # - を除く
                })
                old_line_num += 1
            
            # 追加行
            elif line.startswith('+') and not line.startswith('+++'):
                changed_lines.append({
                    'type': 'added',
                    'new_line': new_line_num,
                    'content': line[1:]  # + を除く
                })
                new_line_num += 1
            
            # 変更なし行
            elif line.startswith(' '):
                old_line_num += 1
                new_line_num += 1
        
        return changed_lines
    
    def _analyze_go_ast(self, content: str, changed_lines: List[Dict[str, Any]]) -> Dict[str, Any]:
        """GoコードのAST解析を実行。変更された関数・メソッド・無名関数を特定"""
        if not self.go_parser:
            return {'error': 'tree-sitter parser not available'}

        try:
            tree = self.go_parser.parse(bytes(content, 'utf8'))
            root_node = tree.root_node

            # 変更内容を整理
            changes = []
            for change in changed_lines:
                if change['type'] == 'added':
                    changes.append({
                        'type': 'added',
                        'content': change['content'].strip(),
                        'line': change['new_line'],
                        'original_content': change['content']
                    })
                elif change['type'] == 'deleted':
                    changes.append({
                        'type': 'deleted',
                        'content': change['content'].strip(),
                        'line': change['old_line'],
                        'original_content': change['content']
                    })
            
            # 変更内容をグループ化（近接する変更をまとめる）
            change_groups = []
            current_group = []
            
            for change in sorted(changes, key=lambda x: x['line']):
                if not current_group or abs(change['line'] - current_group[-1]['line']) <= 5:
                    current_group.append(change)
                else:
                    if current_group:
                        change_groups.append(current_group)
                    current_group = [change]
            
            if current_group:
                change_groups.append(current_group)

            # すべての関数ノードを収集
            all_functions = []
            self._collect_all_functions(root_node, all_functions)

            # 変更された関数を特定
            detected_functions = []
            for func_node in all_functions:
                start_line = func_node.start_point[0] + 1
                end_line = func_node.end_point[0] + 1
                
                # 関数の実際の本体を取得（block要素）
                actual_body_start = None
                actual_body_end = None
                for child in func_node.children:
                    if child.type == 'block':
                        actual_body_start = child.start_point[0] + 1
                        actual_body_end = child.end_point[0] + 1
                        break
                
                # 本体が見つからない場合（インターフェースメソッドや関数宣言など）
                is_declaration_only = actual_body_start is None
                if is_declaration_only:
                    # 関数宣言のみの場合は、宣言行の範囲を本体として扱う
                    actual_body_start = start_line
                    actual_body_end = end_line
                
                # この関数に関連する変更グループを探す
                func_changes = []
                overlapping_lines = []
                added_contents = []
                deleted_contents = []
                
                for group in change_groups:
                    # グループの開始行と終了行を取得
                    group_start = min(c['line'] for c in group)
                    group_end = max(c['line'] for c in group)
                    
                    # 変更グループが関数の範囲内にあるかチェック
                    if ((start_line <= group_start <= end_line) or 
                        (start_line <= group_end <= end_line) or
                        (group_start <= start_line <= group_end)):
                        
                        # 変更の内容を確認
                        real_changes = []
                        for change in group:
                            stripped_content = change['content']
                            original_content = change['original_content']
                            change_line = change['line']
                            
                            # 関数の範囲外の変更は除外
                            if not (start_line <= change_line <= end_line):
                                continue
                            
                            # 関数宣言のみの場合は、宣言の変更を検出対象とする
                            if is_declaration_only:
                                # 関数宣言の変更は重要な変更として扱う
                                if stripped_content.startswith('func '):
                                    # インデントを除去して比較
                                    normalized_content = original_content.lstrip()
                                    
                                    # 追加・削除された内容を記録
                                    if change['type'] == 'added':
                                        added_contents.append(normalized_content)
                                    else:
                                        deleted_contents.append(normalized_content)
                                    
                                    real_changes.append(change)
                                    overlapping_lines.append(change_line)
                                continue
                            
                            # 通常の関数（本体がある場合）の処理
                            # 関数宣言や閉じ括弧、空行は除外
                            if (not stripped_content or 
                                stripped_content == '}' or 
                                (stripped_content.startswith('func ') and change_line == start_line)):
                                continue
                            
                            # 関数の本体以外の変更（宣言部分の変更など）も除外
                            if actual_body_start and change_line < actual_body_start:
                                # 関数の宣言部分の変更は除外（パラメータの変更など）
                                continue
                            
                            # 関数の終了行（閉じ括弧）の変更も除外
                            if actual_body_end and change_line >= actual_body_end:
                                continue
                            
                            # インデントを除去して比較
                            normalized_content = original_content.lstrip()
                            
                            # 追加・削除された内容を記録
                            if change['type'] == 'added':
                                added_contents.append(normalized_content)
                            else:
                                deleted_contents.append(normalized_content)
                            
                            real_changes.append(change)
                            overlapping_lines.append(change_line)
                        
                        if real_changes:
                            func_changes.extend(real_changes)
                
                # 関数の内容が実際に変更されたかチェック
                has_real_changes = False
                if func_changes:
                    # 関数宣言のみの場合は、シグネチャの変更を検出
                    if is_declaration_only:
                        # 追加された行と削除された行を比較
                        added_set = set(added_contents)
                        deleted_set = set(deleted_contents)
                        
                        # 関数宣言の変更があるかチェック
                        if len(added_set) > 0 and len(deleted_set) > 0:
                            # 正規化して比較
                            normalized_added = set(line.strip() for line in added_set)
                            normalized_deleted = set(line.strip() for line in deleted_set)
                            
                            # シグネチャが変更されている場合
                            if normalized_added != normalized_deleted:
                                has_real_changes = True
                        elif len(added_set) > 0 or len(deleted_set) > 0:
                            # 追加のみまたは削除のみの場合も変更とみなす
                            has_real_changes = True
                    else:
                        # 通常の関数の場合の処理（既存のロジック）
                        # 追加された行と削除された行を比較
                        added_set = set(added_contents)
                        deleted_set = set(deleted_contents)
                        
                        # 関数の移動を検出
                        is_function_moved = False
                        if len(added_set) == len(deleted_set) and len(added_set) > 0:
                            # 内容が同じで、インデントだけが異なる場合は移動とみなす
                            normalized_added = set(line.strip() for line in added_set)
                            normalized_deleted = set(line.strip() for line in deleted_set)
                            
                            # 関数の宣言行と終了行を除外して比較
                            filtered_added = set()
                            filtered_deleted = set()
                            
                            for line in normalized_added:
                                if not (line.startswith('func ') or line == '}' or not line):
                                    filtered_added.add(line)
                            
                            for line in normalized_deleted:
                                if not (line.startswith('func ') or line == '}' or not line):
                                    filtered_deleted.add(line)
                            
                            # フィルタリングされた内容を比較
                            if len(filtered_added) > 0 and filtered_added == filtered_deleted:
                                is_function_moved = True
                        
                        # 関数の内容が実際に変更されたかチェック
                        if not is_function_moved and len(added_set) > 0 and len(deleted_set) > 0:
                            # 関数の宣言行と終了行の変更は無視
                            filtered_added = set()
                            filtered_deleted = set()
                            
                            for content in added_set:
                                content = content.strip()
                                if not (content.startswith('func ') or content == '}' or not content):
                                    filtered_added.add(content)
                            
                            for content in deleted_set:
                                content = content.strip()
                                if not (content.startswith('func ') or content == '}' or not content):
                                    filtered_deleted.add(content)
                            
                            # フィルタリングされた内容を比較
                            if filtered_added != filtered_deleted:
                                # 実際の内容変更があるかチェック
                                normalized_added = set(line.strip() for line in filtered_added)
                                normalized_deleted = set(line.strip() for line in filtered_deleted)
                                
                                # 関数の本体の内容が変更されているかチェック
                                if normalized_added != normalized_deleted:
                                    # 関数の本体が実際に変更されている場合のみ
                                    has_real_changes = True
                        elif not is_function_moved and (len(added_set) > 0 or len(deleted_set) > 0):
                            # 追加のみまたは削除のみの場合も変更とみなす
                            has_real_changes = True
                
                if has_real_changes:
                    # 実際の内容変更があった場合のみ関数を追加
                    func_name = self._extract_function_name(func_node)
                    full_name = self._extract_full_function_name(func_node)
                    selection_reason = 'function_declaration_change' if is_declaration_only else 'actual_content_change'
                    detected_functions.append({
                        'function_name': func_name,
                        'full_name': full_name,
                        'start_line': start_line,
                        'end_line': end_line,
                        'body_start': actual_body_start,
                        'body_end': actual_body_end,
                        'is_declaration_only': is_declaration_only,
                        'overlapping_lines': sorted(list(set(overlapping_lines))),
                        'confidence': 'high',
                        'has_actual_changes': has_real_changes,
                        'selection_reason': selection_reason
                    })

            return {'detected_functions': detected_functions}

        except Exception as e:
            log_error(f"AST解析エラー: {str(e)}")
            return {'error': str(e)}

    def _calculate_node_depth(self, node):
        """ノードの深さ（ネストレベル）を計算"""
        depth = 0
        current = node
        while current.parent:
            if current.parent.type in ("function_declaration", "method_declaration"):
                depth += 1
            current = current.parent
        return depth
    
    def _collect_all_functions(self, node, all_functions):
        """再帰的に関数ノードを収集（拡張版）"""
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

    def _extract_function_name(self, func_node):
        """関数ノードから関数名を抽出（拡張版）"""
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

    def _extract_full_function_name(self, func_node):
        """関数ノードからフルネームを抽出（メソッドの場合はレシーバー情報を含む）"""
        if func_node.type == 'function_declaration':
            # 通常の関数宣言の場合
            return self._extract_function_name(func_node)
            
        elif func_node.type == 'method_declaration':
            # メソッド宣言の場合（レシーバーがある）
            # 構造: func (receiver) methodName(params) returnType { body }
            receiver_info = ""
            method_name = ""
            
            found_receiver = False
            for child in func_node.children:
                if child.type == 'parameter_list' and not found_receiver:
                    # 最初のparameter_listはレシーバー
                    found_receiver = True
                    # レシーバー情報を抽出
                    receiver_parts = []
                    for receiver_child in child.children:
                        if receiver_child.type in ['identifier', 'pointer_type', 'type_identifier']:
                            text = receiver_child.text
                            if isinstance(text, bytes):
                                text = text.decode('utf-8')
                            receiver_parts.append(text.strip())
                    if receiver_parts:
                        # レシーバー名と型を結合
                        if len(receiver_parts) >= 2:
                            receiver_info = f"({receiver_parts[0]} {receiver_parts[1]})"
                        else:
                            receiver_info = f"({receiver_parts[0]})"
                    continue
                elif child.type in ['identifier', 'field_identifier'] and found_receiver:
                    # レシーバーの後のidentifierまたはfield_identifierがメソッド名
                    method_name = child.text
                    if isinstance(method_name, bytes):
                        method_name = method_name.decode('utf-8')
                    method_name = method_name.strip()
                    break
                    
            if receiver_info and method_name:
                return f"{receiver_info}.{method_name}"
            elif method_name:
                return method_name
        
        return "unknown"

    def _get_line_start_offsets(self, content: str) -> List[int]:
        """各行の開始byte offsetリストを返す（0-indexed）"""
        offsets = []
        offset = 0
        for line in content.splitlines(keepends=True):
            offsets.append(offset)
            offset += len(line.encode('utf-8'))
        return offsets

    # ヘルパーメソッド
    def _read_file(self, file_path: str) -> Optional[str]:
        """ファイルを読み込み"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            log_error(f"ファイル読み込みエラー: {file_path}, {str(e)}")
            return None
    
    def _extract_cl_numbers(self, content: str) -> List[str]:
        """コンテンツからCL番号を抽出"""
        patterns = [
            r'https://golang\.org/cl/(\d+)',
            r'https://go\.dev/cl/(\d+)',
            r'https://go-review\.googlesource\.com/c/go/\+/?(\d+)',
            r'Change https://golang\.org/cl/(\d+)',
            r'Change https://go\.dev/cl/(\d+)',
            r'CL\s+(\d+)',
            r'cl/(\d+)',
        ]
        
        cl_numbers = set()
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            cl_numbers.update(matches)
        
        return sorted(list(cl_numbers))
    
    def _fetch_cl_info(self, cl_number: str) -> Optional[Dict[str, Any]]:
        """CL基本情報を取得"""
        endpoints = [
            f"{self.GERRIT_API_BASE}/changes/{cl_number}?o=CURRENT_REVISION&o=CURRENT_COMMIT",
            f"{self.GERRIT_API_BASE}/changes/go~{cl_number}?o=CURRENT_REVISION&o=CURRENT_COMMIT"
        ]
        
        for endpoint in endpoints:
            try:
                response = self.session.get(endpoint, timeout=30)
                if response.status_code == 200:
                    content = response.text
                    if content.startswith(")]}'"):
                        content = content[4:]
                    return json.loads(content)
            except Exception:
                continue
        
        return None
    
    def _fetch_file_list(self, cl_number: str) -> Optional[Dict[str, Any]]:
        """変更されたファイル一覧を取得"""
        endpoints = [
            f"{self.GERRIT_API_BASE}/changes/{cl_number}/revisions/current/files",
            f"{self.GERRIT_API_BASE}/changes/go~{cl_number}/revisions/current/files"
        ]
        
        for endpoint in endpoints:
            try:
                response = self.session.get(endpoint, timeout=30)
                if response.status_code == 200:
                    content = response.text
                    if content.startswith(")]}'"):
                        content = content[4:]
                    return json.loads(content)
            except Exception:
                continue
        
        return None
    
    def _fetch_file_content(self, cl_number: str, file_path: str, revision_id: str) -> Optional[str]:
        """ファイル内容を取得"""
        encoded_path = file_path.replace('/', '%2F')
        endpoints = [
            f"{self.GERRIT_API_BASE}/changes/{cl_number}/revisions/{revision_id}/files/{encoded_path}/content",
            f"{self.GERRIT_API_BASE}/changes/go~{cl_number}/revisions/{revision_id}/files/{encoded_path}/content"
        ]
        
        for endpoint in endpoints:
            try:
                response = self.session.get(endpoint, timeout=30)
                if response.status_code == 200:
                    content = response.text
                    try:
                        # Base64デコード
                        decoded_content = base64.b64decode(content).decode('utf-8')
                        return decoded_content
                    except Exception:
                        # Base64でない場合はそのまま返す
                        return content
            except Exception:
                continue
        
        return None

def print_analysis_summary(result):
    """解析結果のサマリーを表示"""
    print("\n=== 拡張解析結果 ===")
    print(f"提案ファイル: {result['proposal_file']}")
    print(f"CL番号: {result['cl_numbers']}")
    print(f"解析したCL数: {result['total_cls_analyzed']}")
    print(f"tree-sitter有効: {result.get('tree_sitter_enabled', False)}")
    print()

    for cl in result['cl_analyses']:
        print(f"--- CL {cl['cl_number']} ---")
        print(f"件名: {cl['subject']}")
        print(f"Goファイル解析数: {cl['go_files_analyzed']}")
        
        for file in cl['files']:
            print(f"  📄 {file['file_path']}")
            print(f"     状態: {file.get('status', '')}")
            print(f"     変更行数: +{file['lines_inserted']} -{file['lines_deleted']}")
            print(f"     差分行数: {len(file['changed_lines'])}")
            
            # 検出された関数の情報を表示
            if 'ast_analysis' in file and 'detected_functions' in file['ast_analysis']:
                functions = file['ast_analysis']['detected_functions']
                if functions:
                    print("     検出された関数:")
                    for func in functions:
                        # 関数名の表示（full_nameがある場合はそちらを使用）
                        func_name = func.get('full_name', func.get('function_name', 'unknown'))
                        print(f"       - {func_name} (行: {func['start_line']}-{func['end_line']})")
                        if func.get('has_actual_changes', False):
                            print(f"         変更行: {func['overlapping_lines']}")
            print()

def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='拡張CLアナライザー: 差分行とAST解析')
    parser.add_argument('proposal_file', help='提案ファイルのパス')
    parser.add_argument('--output', '-o', help='出力ファイル名（JSONで保存）')
    parser.add_argument('--verbose', '-v', action='store_true', help='詳細ログ')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # 拡張解析実行
    analyzer = EnhancedCLAnalyzer()
    result = analyzer.analyze_proposal(args.proposal_file)
    
    # 結果表示
    print_analysis_summary(result)
    
    # 結果をJSONファイルに保存
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"\n💾 詳細結果を保存: {args.output}")
    
if __name__ == '__main__':
    main()
