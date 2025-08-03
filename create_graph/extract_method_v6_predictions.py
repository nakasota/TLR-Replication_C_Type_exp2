#!/usr/bin/env python3
"""
Method v6の予測結果とground truthを照合してTreemapデータを生成するスクリプト
正しい予測（True Positives）と間違った予測（False Positives）を可視化
"""

import json
import os
from collections import defaultdict

def load_ground_truth():
    """Ground truthデータを読み込む"""
    ground_truth_path = "/workspace/data/processed/proposal_mappings/validated/accepted_proposals_FUNCTION_LEVEL_GROUND_TRUTH.json"
    
    with open(ground_truth_path, 'r') as f:
        ground_truth_data = json.load(f)
    
    # Proposal IDごとにground truthを整理
    ground_truth_by_proposal = defaultdict(set)
    for entry in ground_truth_data:
        proposal_id, file_path, function_name = entry
        ground_truth_by_proposal[str(proposal_id)].add((file_path, function_name))
    
    return ground_truth_by_proposal

def load_method_v6_results():
    """Method v6の結果を読み込む"""
    results_path = "/workspace/method_v6/link_decision/output/20250716_160634/evaluation_results.json"
    llm_outputs_path = "/workspace/method_v6/link_decision/output/20250716_160634/llm_outputs.json"
    
    with open(results_path, 'r') as f:
        evaluation_results = json.load(f)
    
    with open(llm_outputs_path, 'r') as f:
        llm_outputs = json.load(f)
    
    return evaluation_results, llm_outputs

def extract_directory_from_path(file_path):
    """ファイルパスから最深部のディレクトリを抽出"""
    # src/crypto/tls/common.go -> src/crypto/tls
    # src/runtime/main/test.go -> src/runtime/main
    # crypto/tls/common.go -> crypto/tls
    parts = file_path.split('/')
    
    # ファイル名（最後の部分）を除外
    if len(parts) > 1:
        directory_parts = parts[:-1]  # 最後のファイル名を除外
        return '/'.join(directory_parts)
    else:
        # ファイル名のみの場合はrootディレクトリとして扱う
        return 'root'

def analyze_method_v6_predictions(ground_truth_by_proposal, llm_outputs):
    """Method v6の予測をground truthと照合して分析"""
    results = {
        'true_positives': [],   # Method v6が正しく予測した関数
        'false_positives': [],  # Method v6が間違って予測した関数
        'statistics': defaultdict(lambda: {'tp': 0, 'fp': 0})  # ディレクトリ別統計
    }
    
    # LLM outputsの"selected_function_level_output"キーを除外
    proposal_outputs = {k: v for k, v in llm_outputs.items() if not k.startswith('selected_')}
    
    for proposal_file, file_predictions in proposal_outputs.items():
        # プロポーザルIDを抽出 (例: "45428.md" -> "45428")
        proposal_id = proposal_file.replace('.md', '')
        
        # このプロポーザルのground truthを取得
        ground_truth_functions = ground_truth_by_proposal.get(proposal_id, set())
        
        # 各ファイルの予測を確認
        for file_path, function_predictions in file_predictions.items():
            for function_name, prediction in function_predictions.items():
                if prediction == "Yes":
                    # Method v6が"Yes"と予測した関数
                    predicted_function = (file_path, function_name)
                    directory = extract_directory_from_path(file_path)
                    
                    if predicted_function in ground_truth_functions:
                        # True Positive: 正しい予測
                        results['true_positives'].append({
                            'proposal_id': proposal_id,
                            'file_path': file_path,
                            'function_name': function_name,
                            'directory': directory
                        })
                        results['statistics'][directory]['tp'] += 1
                    else:
                        # False Positive: 間違った予測
                        results['false_positives'].append({
                            'proposal_id': proposal_id,
                            'file_path': file_path,
                            'function_name': function_name,
                            'directory': directory
                        })
                        results['statistics'][directory]['fp'] += 1
    
    return results

def create_treemap_data():
    """Method v6の予測結果に基づいてTreemap用のデータを作成"""
    print("Loading ground truth data...")
    ground_truth_by_proposal = load_ground_truth()
    
    print("Loading method v6 results...")
    evaluation_results, llm_outputs = load_method_v6_results()
    
    print("Analyzing method v6 predictions...")
    # Method v6の予測を分析
    analysis_results = analyze_method_v6_predictions(ground_truth_by_proposal, llm_outputs)
    
    # ディレクトリ別の統計を集計
    directory_stats = defaultdict(lambda: {'correct': 0, 'incorrect': 0})
    
    # True Positives (正しい予測)
    for tp in analysis_results['true_positives']:
        directory = tp['directory']
        directory_stats[directory]['correct'] += 1
    
    # False Positives (間違った予測)
    for fp in analysis_results['false_positives']:
        directory = fp['directory']
        directory_stats[directory]['incorrect'] += 1
    
    # Treemap用のフォーマットに変換
    treemap_data = []
    for directory, stats in directory_stats.items():
        if stats['correct'] > 0 or stats['incorrect'] > 0:
            treemap_data.append({
                'directory': directory,
                'correct': stats['correct'],
                'incorrect': stats['incorrect'],
                'total': stats['correct'] + stats['incorrect']
            })
    
    # 統計情報を表示
    total_correct = sum(item['correct'] for item in treemap_data)
    total_incorrect = sum(item['incorrect'] for item in treemap_data)
    total_predictions = total_correct + total_incorrect
    
    print(f"\n=== Method v6予測結果の統計 ===")
    print(f"正しい予測 (True Positives): {total_correct}")
    print(f"間違った予測 (False Positives): {total_incorrect}")
    print(f"総予測数: {total_predictions}")
    if total_predictions > 0:
        print(f"精度 (Precision): {total_correct / total_predictions * 100:.1f}%")
    print(f"ディレクトリ数: {len(treemap_data)}")
    
    # ディレクトリ別詳細表示
    print(f"\n=== ディレクトリ別統計 ===")
    for item in sorted(treemap_data, key=lambda x: x['total'], reverse=True):
        directory = item['directory']
        correct = item['correct']
        incorrect = item['incorrect']
        total = item['total']
        accuracy = (correct / total * 100) if total > 0 else 0
        print(f"{directory:30} | 正解: {correct:3} | 誤り: {incorrect:3} | 計: {total:3} | 精度: {accuracy:5.1f}%")
    
    return treemap_data

if __name__ == "__main__":
    try:
        print("Starting method v6 prediction analysis...")
        data = create_treemap_data()
        
        # データをJSON形式で保存
        output_path = "/workspace/create_graph/method_v6_prediction_analysis.json"
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\nMethod v6 prediction analysis data saved to: {output_path}")
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()
