#!/usr/bin/env python3
"""
変更内容検証ヘルパー
CLで変更された内容が現在のリポジトリに実装されているかを確認する
"""

import re
import difflib
from typing import List, Dict, Any, Optional, Set, Tuple
import logging

logger = logging.getLogger(__name__)

class ContentValidator:
    """CLの変更内容と現在のリポジトリの内容を比較検証する"""
    
    def __init__(self, repo_loader=None):
        """
        Args:
            repo_loader: リポジトリローダー（ファイル内容取得用）
        """
        self.repo_loader = repo_loader
    
    def validate_function_content(self, 
                                  func_name: str,
                                  file_path: str, 
                                  cl_added_lines: List[str],
                                  func_start_line: int,
                                  func_end_line: int) -> Dict[str, Any]:
        """
        関数の追加内容が現在のリポジトリに反映されているかを検証
        
        Args:
            func_name: 関数名
            file_path: ファイルパス
            cl_added_lines: CLで追加された行のリスト
            func_start_line: 関数の開始行
            func_end_line: 関数の終了行
            
        Returns:
            検証結果辞書
        """
        try:
            if not self.repo_loader:
                return {
                    'validation_status': 'error',
                    'reason': 'repo_loader not available',
                    'content_match_score': 0.0,
                    'is_ground_truth': False
                }
            
            # 現在のリポジトリからファイル内容を取得
            current_content = self.repo_loader.get_file_content(file_path)
            if not current_content:
                logger.debug(f"File {file_path} not found or not accessible in current repository")
                return {
                    'validation_status': 'file_not_found',
                    'reason': f'File {file_path} not found in current repository',
                    'content_match_score': 0.0,
                    'is_ground_truth': False  # ファイルが見つからない場合はGround Truthとしない
                }
            
            # 現在のファイル内容から関数を抽出
            current_func_lines = self._extract_function_lines(
                current_content, func_name, func_start_line, func_end_line
            )
            
            if not current_func_lines:
                return {
                    'validation_status': 'function_not_found',
                    'reason': f'Function {func_name} not found in current file',
                    'content_match_score': 0.0,
                    'is_ground_truth': False
                }
            
            # CLの変更内容を正規化（追加行のみ）
            normalized_added = [self._normalize_line(line) for line in cl_added_lines if line.strip()]
            
            # 現在の関数内容を正規化
            normalized_current = [self._normalize_line(line) for line in current_func_lines if line.strip()]
            
            # 内容比較を実行（追加行のみ）
            validation_result = self._compare_content(
                normalized_added, normalized_current
            )
            
            # 詳細な分析結果を追加
            validation_result.update({
                'function_name': func_name,
                'file_path': file_path,
                'cl_added_lines_count': len(cl_added_lines),
                'current_function_lines_count': len(current_func_lines),
                'added_lines_found_in_current': self._count_matching_lines(normalized_added, normalized_current)
            })
            
            return validation_result
            
        except Exception as e:
            logger.error(f"Content validation error for {func_name} in {file_path}: {str(e)}")
            return {
                'validation_status': 'error',
                'reason': f'Validation error: {str(e)}',
                'content_match_score': 0.0,
                'is_ground_truth': False
            }
    
    def _extract_function_lines(self, 
                                content: str, 
                                func_name: str, 
                                start_line: int, 
                                end_line: int) -> List[str]:
        """
        ファイル内容から指定された関数の行を抽出
        """
        try:
            lines = content.splitlines()
            
            # 行番号は1ベースなので調整
            start_idx = max(0, start_line - 1)
            end_idx = min(len(lines), end_line)
            
            function_lines = lines[start_idx:end_idx]
            
            # 関数名が含まれているかの簡易チェック
            func_declaration_found = False
            for line in function_lines[:5]:  # 最初の5行以内に関数宣言があるはず
                if f'func ' in line and func_name in line:
                    func_declaration_found = True
                    break
            
            if not func_declaration_found:
                # 関数名での検索を試行
                return self._search_function_by_name(lines, func_name)
            
            return function_lines
            
        except Exception as e:
            logger.error(f"Error extracting function lines: {str(e)}")
            return []
    
    def _search_function_by_name(self, lines: List[str], func_name: str) -> List[str]:
        """
        関数名で検索して関数の行を抽出
        """
        try:
            func_start = None
            func_end = None
            
            # 関数宣言を探す
            for i, line in enumerate(lines):
                if re.search(rf'\bfunc\s+(?:\([^)]*\)\s*)?{re.escape(func_name)}\s*\(', line):
                    func_start = i
                    break
            
            if func_start is None:
                return []
            
            # 関数の終了を探す（ブロックの終わりを検出）
            brace_count = 0
            for i in range(func_start, len(lines)):
                line = lines[i]
                brace_count += line.count('{') - line.count('}')
                if brace_count == 0 and i > func_start:
                    func_end = i + 1
                    break
            
            if func_end is None:
                func_end = len(lines)
            
            return lines[func_start:func_end]
            
        except Exception as e:
            logger.error(f"Error searching function by name: {str(e)}")
            return []
    
    def _normalize_line(self, line: str) -> str:
        """
        行を正規化（空白の正規化、コメント除去など）
        """
        # 先頭・末尾の空白を除去
        normalized = line.strip()
        
        # 複数の空白を単一の空白に変換
        normalized = re.sub(r'\s+', ' ', normalized)
        
        # 行末コメントを除去（//以降）
        if '//' in normalized:
            comment_pos = normalized.find('//')
            # 文字列リテラル内でない場合のみ除去
            if not self._is_in_string_literal(normalized, comment_pos):
                normalized = normalized[:comment_pos].strip()
        
        return normalized
    
    def _is_in_string_literal(self, line: str, pos: int) -> bool:
        """
        指定位置が文字列リテラル内かどうかを判定
        """
        in_string = False
        escape_next = False
        
        for i, char in enumerate(line[:pos]):
            if escape_next:
                escape_next = False
                continue
            
            if char == '\\':
                escape_next = True
            elif char == '"' and not escape_next:
                in_string = not in_string
        
        return in_string
    
    def _compare_content(self, 
                         added_lines: List[str], 
                         current_lines: List[str]) -> Dict[str, Any]:
        """
        追加された行と現在の内容を比較
        一つでも追加行が存在すればground truthとして認定
        """
        # 追加された行が現在の内容に含まれているかチェック
        added_found = 0
        for added_line in added_lines:
            if any(self._lines_similar(added_line, current_line) for current_line in current_lines):
                added_found += 1
        
        # 判定ロジック：追加行が必須、かつ一つでも現在のリポジトリに存在すればground truth
        total_added = len(added_lines)
        if total_added == 0:
            # 追加行がない場合はground truthとして認定しない
            content_match_score = 0.0
            validation_status = 'no_added_lines'
            is_ground_truth = False
        else:
            content_match_score = added_found / total_added
            
            # 一つでも追加行が見つかればground truthとして認定
            if added_found > 0:
                validation_status = 'content_matches'
                is_ground_truth = True
            else:
                validation_status = 'content_differs'
                is_ground_truth = False
        
        return {
            'validation_status': validation_status,
            'content_match_score': content_match_score,
            'added_lines_found': added_found,
            'added_lines_total': len(added_lines),
            'is_ground_truth': is_ground_truth,
            'reason': self._get_validation_reason(validation_status, content_match_score, added_found)
        }
    
    def _lines_similar(self, line1: str, line2: str, threshold: float = 0.8) -> bool:
        """
        2つの行が似ているかどうかを判定
        """
        if not line1 or not line2:
            return line1 == line2
        
        # 完全一致
        if line1 == line2:
            return True
        
        # 類似度計算
        ratio = difflib.SequenceMatcher(None, line1, line2).ratio()
        return ratio >= threshold
    
    def _count_matching_lines(self, search_lines: List[str], target_lines: List[str]) -> int:
        """
        search_linesの中でtarget_linesに含まれる行数をカウント
        """
        count = 0
        for search_line in search_lines:
            if any(self._lines_similar(search_line, target_line) for target_line in target_lines):
                count += 1
        return count
    
    def _get_validation_reason(self, status: str, score: float, added_found: int) -> str:
        """
        検証結果の理由を生成
        """
        if status == 'content_matches':
            if added_found == 1:
                return f'At least one CL added line found in current repository - qualified as ground truth (score: {score:.2f})'
            else:
                return f'{added_found} CL added lines found in current repository - qualified as ground truth (score: {score:.2f})'
        elif status == 'content_differs':
            return f'No CL added lines found in current repository - not qualified as ground truth (score: {score:.2f})'
        elif status == 'no_added_lines':
            return 'No added lines detected in CL - not qualified as ground truth'
        else:
            return f'Validation status: {status}'
