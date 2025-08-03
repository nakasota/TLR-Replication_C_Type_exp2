#!/usr/bin/env python3
"""
CL状態を考慮したバッチ関数解析スクリプト
MERGED状態のCLのみを対象として関数解析を実行する
変更内容の詳細情報付き
"""

import os
import glob
import json
import sys
from pathlib import Path
from find_relative_func import EnhancedCLAnalyzer
from content_validator import ContentValidator
from repo_loader import GoRepoLoader
from tqdm import tqdm
import logging

# ログ設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    # ディレクトリと出力ファイルのパス
    proposals_dir = Path("../data/preprocess/accepted_proposals")
    output_json = Path("../data/ground_truth/accepted_proposals_func_analysis_merged_validated.json")
    repo_structure_path = Path("../data/ground_truth/go_repo_structure.json")

    # .mdファイルをすべて取得
    md_files = sorted(proposals_dir.glob("*.md"))
    print(f"解析対象: {len(md_files)}件のmdファイル")

    # リポジトリローダーと変更内容検証器を初期化
    print("🔧 リポジトリローダーと変更内容検証器を初期化中...")
    repo_loader = GoRepoLoader(str(repo_structure_path))
    content_validator = ContentValidator(repo_loader)

    analyzer = EnhancedCLAnalyzer()
    all_results = []
    failed_files = []
    merged_count = 0
    non_merged_count = 0
    status_counts = {}
    content_analysis_stats = {
        'functions_with_content_analysis': 0,
        'content_validation_errors': 0
    }

    # tqdmを使用して進捗表示
    with tqdm(md_files, desc="提案ファイル解析中", unit="file", 
              bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}] {postfix}') as pbar:
        for md_file in pbar:
            try:
                # 現在のファイル名と統計を進捗バーに表示
                pbar.set_postfix_str(f"{md_file.name} | MERGED: {merged_count}, 提案: {len(all_results)}")
                result = analyzer.analyze_proposal(str(md_file))
                
                # CLの状態を確認してフィルタリング
                filtered_cl_analyses = []
                for cl_analysis in result.get('cl_analyses', []):
                    cl_status = cl_analysis.get('status', '').upper()
                    
                    # 統計用にステータスをカウント
                    status_counts[cl_status] = status_counts.get(cl_status, 0) + 1
                    
                    # MERGED状態のもののみを採用
                    if cl_status == 'MERGED':
                        # MERGED状態のCLに対して変更内容分析を追加
                        enhanced_cl_analysis = cl_analysis.copy()
                        
                        # 各ファイルの関数に対して変更内容分析を実行
                        enhanced_files = []
                        for file_data in cl_analysis.get('files', []):
                            enhanced_file_data = file_data.copy()
                            
                            # AST解析結果がある場合、変更内容分析を追加
                            ast_analysis = file_data.get('ast_analysis', {})
                            if 'detected_functions' in ast_analysis:
                                enhanced_functions = []
                                
                                for func in ast_analysis['detected_functions']:
                                    enhanced_func = func.copy()
                                    
                                    try:
                                        # 変更内容の追加分析
                                        func_name = func.get('function_name')
                                        file_path = file_data.get('file_path')
                                        changed_lines = file_data.get('changed_lines', [])
                                        
                                        if func_name and file_path and changed_lines:
                                            # 関数範囲内の変更行を抽出
                                            func_start = func.get('start_line', 1)
                                            func_end = func.get('end_line', 1)
                                            
                                            func_changes = [
                                                line for line in changed_lines
                                                if func_start <= line.get('new_line', 0) <= func_end or
                                                   func_start <= line.get('old_line', 0) <= func_end
                                            ]
                                            
                                            enhanced_func['function_changes'] = {
                                                'changes_in_function': len(func_changes),
                                                'added_lines': [
                                                    line.get('content', '') 
                                                    for line in func_changes 
                                                    if line.get('type') == 'added'
                                                ]
                                            }
                                            
                                            content_analysis_stats['functions_with_content_analysis'] += 1
                                        
                                    except Exception as e:
                                        logging.error(f"Content analysis error for {func_name}: {str(e)}")
                                        content_analysis_stats['content_validation_errors'] += 1
                                    
                                    enhanced_functions.append(enhanced_func)
                                
                                # 強化されたAST解析結果で置き換え
                                enhanced_ast_analysis = ast_analysis.copy()
                                enhanced_ast_analysis['detected_functions'] = enhanced_functions
                                enhanced_file_data['ast_analysis'] = enhanced_ast_analysis
                            
                            enhanced_files.append(enhanced_file_data)
                        
                        enhanced_cl_analysis['files'] = enhanced_files
                        filtered_cl_analyses.append(enhanced_cl_analysis)
                        merged_count += 1
                    else:
                        non_merged_count += 1
                
                # MERGED状態のCLがある場合のみ結果に追加
                if filtered_cl_analyses:
                    filtered_result = result.copy()
                    filtered_result['cl_analyses'] = filtered_cl_analyses
                    all_results.append(filtered_result)
                    
            except Exception as e:
                print(f"[ERROR] {md_file}: {e}")
                failed_files.append({"file": str(md_file), "error": str(e)})

    # 統計情報を表示
    print(f"\n📊 CL状態統計:")
    print(f"├─ MERGED状態のCL: {merged_count}件")
    print(f"├─ 非MERGED状態のCL: {non_merged_count}件")
    print(f"└─ MERGED状態を含む提案: {len(all_results)}件")
    
    print(f"\n📋 状態別詳細:")
    for status, count in sorted(status_counts.items()):
        print(f"├─ {status}: {count}件")
    
    print(f"\n🔍 変更内容分析統計:")
    print(f"├─ 変更内容分析済み関数: {content_analysis_stats['functions_with_content_analysis']}件")
    print(f"└─ 分析エラー: {content_analysis_stats['content_validation_errors']}件")

    # 結果を保存
    output_json.parent.mkdir(parents=True, exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump({
            "results": all_results,
            "failed_files": failed_files,
            "statistics": {
                "total_proposals_analyzed": len(md_files),
                "proposals_with_merged_cls": len(all_results),
                "merged_cls_count": merged_count,
                "non_merged_cls_count": non_merged_count,
                "status_breakdown": status_counts,
                "content_analysis_stats": content_analysis_stats
            }
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 MERGED状態のCLのみを含む結果（変更内容検証付き）を保存: {output_json}")
    print(f"失敗: {len(failed_files)}件")

if __name__ == "__main__":
    main()
