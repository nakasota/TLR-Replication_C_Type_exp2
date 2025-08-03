#!/usr/bin/env python3
"""
Ground Truth作成スクリプト（最終版）
現在のリポジトリで実装されている関数のみを含む、クリーンなground truthを作成する
"""

import json
import os
from pathlib import Path

def create_ground_truth():
    """メイン処理：ground truthを作成"""
    
    # 入力ファイル
    func_analysis_path = "../data/ground_truth/accepted_proposals_func_analysis.json"
    repo_structure_path = "../data/ground_truth/go_repo_structure.json"
    output_path = "../data/ground_truth/accepted_proposals_ground_truth.json"
    
    print("🚀 Ground Truth作成開始")
    print(f"📁 関数解析データ: {func_analysis_path}")
    print(f"📁 リポジトリ構造: {repo_structure_path}")
    print(f"💾 出力ファイル: {output_path}")
    
    # ファイル存在チェック
    for p in [func_analysis_path, repo_structure_path]:
        if not os.path.exists(p):
            print(f"❌ ファイルが見つかりません: {p}")
            return
    
    # リポジトリ構造をロード
    print("📖 リポジトリ構造を読み込み中...")
    with open(repo_structure_path, 'r', encoding='utf-8') as f:
        repo_data = json.load(f)
    
    # ファイルパスと関数の効率的な検索用データ構造
    repo_files = set(repo_data.keys())
    repo_file_functions = {
        fp: set(d['functions'].keys()) 
        for fp, d in repo_data.items() 
        if 'functions' in d
    }
    
    print(f"✓ リポジトリファイル数: {len(repo_files)}")
    print(f"✓ 関数を持つファイル数: {len(repo_file_functions)}")
    
    # 関数解析データをロード
    print("📖 関数解析データを読み込み中...")
    with open(func_analysis_path, 'r', encoding='utf-8') as f:
        func_analysis = json.load(f)
    
    results = func_analysis.get('results', [])
    print(f"✓ 解析済み提案数: {len(results)}")
    
    # Ground truthを作成
    print("🔍 Ground truth作成中...")
    ground_truth = []
    
    matched_proposals = 0
    total_matched_files = 0
    total_matched_functions = 0
    
    for proposal in results:
        # 提案ID（ファイル名から抽出）
        proposal_file = proposal.get('proposal_file', '')
        proposal_id = Path(proposal_file).stem if proposal_file else 'unknown'
        
        # この提案で一致するファイルと関数を収集
        matched_files = set()
        matched_functions = []
        
        for cl_analysis in proposal.get('cl_analyses', []):
            for file_data in cl_analysis.get('files', []):
                file_path = file_data.get('file_path')
                ast_analysis = file_data.get('ast_analysis', {})
                detected_functions = ast_analysis.get('detected_functions', [])
                
                # ファイルがリポジトリに存在するかチェック
                if file_path in repo_files:
                    repo_funcs = repo_file_functions.get(file_path, set())
                    
                    # この ファイルで一致する関数
                    file_matched_functions = []
                    for func in detected_functions:
                        func_name = func.get('function_name')
                        if func_name and func_name in repo_funcs:
                            file_matched_functions.append({
                                'function_name': func_name,
                                'file_path': file_path,
                                'start_line': func.get('start_line'),
                                'end_line': func.get('end_line')
                            })
                    
                    # 一致する関数があれば記録
                    if file_matched_functions:
                        matched_files.add(file_path)
                        matched_functions.extend(file_matched_functions)
        
        # 一致するファイル・関数があれば ground truth に追加
        if matched_files and matched_functions:
            ground_truth_entry = {
                'proposal_id': proposal_id,
                'proposal_file': proposal_file,
                'files': sorted(list(matched_files)),  # ソートして一貫性を保つ
                'detected_functions': matched_functions
            }
            
            ground_truth.append(ground_truth_entry)
            matched_proposals += 1
            total_matched_files += len(matched_files)
            total_matched_functions += len(matched_functions)
    
    print(f"✅ Ground truth作成完了！")
    print(f"📊 統計:")
    print(f"├─ 一致した提案数: {matched_proposals}")
    print(f"├─ 総ファイル数: {total_matched_files}")
    print(f"├─ 総関数数: {total_matched_functions}")
    print(f"├─ 平均ファイル/提案: {total_matched_files/matched_proposals:.2f}")
    print(f"└─ 平均関数/提案: {total_matched_functions/matched_proposals:.2f}")
    
    # JSONファイルに保存
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(ground_truth, f, ensure_ascii=False, indent=2)
    
    print(f"💾 結果を保存: {output_path}")
    
    # サンプル表示
    if ground_truth:
        print(f"\n📝 サンプル提案:")
        sample = ground_truth[0]
        print(f"├─ ID: {sample['proposal_id']}")
        print(f"├─ ファイル数: {len(sample['files'])}")
        print(f"├─ 関数数: {len(sample['detected_functions'])}")
        print(f"└─ 最初の3ファイル: {sample['files'][:3]}")

def main():
    """エントリーポイント"""
    create_ground_truth()

if __name__ == "__main__":
    main() 