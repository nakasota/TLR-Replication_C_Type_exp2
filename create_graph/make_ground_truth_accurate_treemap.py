#!/usr/bin/env python3
"""
Method v6の正しい予測のみ（Ground Truthに一致するもの）を使用してTreemapを作成するスクリプト
Declined proposalsのダミーデータは使用せず、純粋にmethod_v6の正確な予測能力を表示
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import squarify
import numpy as np
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
    parts = file_path.split('/')
    
    if len(parts) > 1:
        directory_parts = parts[:-1]  # 最後のファイル名を除外
        return '/'.join(directory_parts)
    else:
        return 'root'

def extract_true_positives_by_directory(ground_truth_by_proposal, llm_outputs, evaluation_results):
    """ディレクトリ別にmethod_v6の正解した予測のみをカウント"""
    directory_stats = defaultdict(int)
    
    print("=== Extracting True Positives from Method v6 ===")
    
    # LLM outputsの"selected_function_level_output"キーを除外
    proposal_outputs = {k: v for k, v in llm_outputs.items() if not k.startswith('selected_')}
    
    total_tp_functions = 0
    processed_proposals = 0
    
    for proposal_file, file_predictions in proposal_outputs.items():
        # プロポーザルIDを抽出 (例: "45428.md" -> "45428")
        proposal_id = proposal_file.replace('.md', '')
        
        # このプロポーザルのground truthを取得
        ground_truth_functions = ground_truth_by_proposal.get(proposal_id, set())
        
        if not ground_truth_functions:
            continue
            
        processed_proposals += 1
        proposal_tp_count = 0
        
        # 各ファイルの予測を確認
        for file_path, function_predictions in file_predictions.items():
            for function_name, prediction in function_predictions.items():
                if prediction == "Yes":
                    # Method v6が"Yes"と予測した関数
                    predicted_function = (file_path, function_name)
                    
                    if predicted_function in ground_truth_functions:
                        # True Positive: 正しい予測
                        directory = extract_directory_from_path(file_path)
                        directory_stats[directory] += 1
                        total_tp_functions += 1
                        proposal_tp_count += 1
        
        print(f"Proposal {proposal_id}: {proposal_tp_count} true positive functions")
    
    print(f"\nSummary:")
    print(f"Processed proposals: {processed_proposals}")
    print(f"Total true positive functions: {total_tp_functions}")
    print(f"Directories with correct predictions: {len(directory_stats)}")
    
    return directory_stats

def create_ground_truth_accurate_treemap(directory_stats):
    """Ground truthに一致するmethod_v6の予測のみを使用してtreemapを作成"""
    
    if not directory_stats:
        print("No data to display")
        return
    
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # ディレクトリを正解数でソート（大きい順）
    sorted_directories = sorted(directory_stats.items(), key=lambda x: x[1], reverse=True)
    
    # squarifyを使用してtreemapのレイアウトを計算
    sizes = [count for _, count in sorted_directories]
    labels = [directory for directory, _ in sorted_directories]
    
    # treemapの座標を取得
    treemap_rects = squarify.normalize_sizes(sizes, 100, 100)
    treemap_coords = squarify.squarify(treemap_rects, 0, 0, 100, 100)
    
    # 色設定（正解した予測のみなので緑系統を使用）
    colors = plt.cm.Greens(np.linspace(0.3, 0.9, len(sorted_directories)))
    
    # 各ディレクトリの位置情報を準備
    positions = []
    for i, (directory, count) in enumerate(sorted_directories):
        coord = treemap_coords[i]
        positions.append({
            'directory': directory,
            'x': coord['x'],
            'y': coord['y'], 
            'width': coord['dx'],
            'height': coord['dy'],
            'count': count,
            'color': colors[i]
        })
    
    # 各ディレクトリを描画
    for pos in positions:
        x, y, width, height = pos['x'], pos['y'], pos['width'], pos['height']
        count = pos['count']
        directory = pos['directory']
        color = pos['color']
        
        # 矩形を描画
        rect = patches.Rectangle(
            (x, y), width, height,
            facecolor=color,
            edgecolor='white',
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(rect)
        
        # 数値ラベル（正解した関数数）
        if width > 2 and height > 2:
            label_size = min(16, max(8, int(width/6)))
            ax.text(x + width/2, y + height/2, 
                   f'{count}',
                   ha='center', va='center', 
                   fontsize=label_size, 
                   fontweight='bold',
                   color='white' if count > max(sizes)/2 else 'black')
        
        # ディレクトリ名のラベル
        base_font_size = max(6, min(14, int(width/12)))
        
        # 長いパスの場合は改行して表示
        if len(directory) > 15 and '/' in directory and height > 12:
            parts = directory.split('/')
            if len(parts) > 2:
                display_name = f"{parts[0]}/\n{'/'.join(parts[1:])}"
            else:
                display_name = directory
        else:
            display_name = directory
        
        # ディレクトリ名を表示
        if height > 10:  # 高さがある場合は上部に表示
            ax.text(x + width/2, y + height - 2, 
                   display_name,
                   ha='center', va='top', 
                   fontsize=base_font_size, 
                   fontweight='bold',
                   color='black',
                   bbox=dict(boxstyle="round,pad=0.15", facecolor='white', alpha=0.9))
        else:  # 高さが少ない場合は中央上部に表示
            small_font_size = max(4, min(base_font_size, int(height/2)))
            ax.text(x + width/2, y + height*0.75, 
                   display_name,
                   ha='center', va='center', 
                   fontsize=small_font_size, 
                   fontweight='bold',
                   color='black',
                   bbox=dict(boxstyle="round,pad=0.1", facecolor='white', alpha=0.9))
    
    # 軸の設定
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # タイトルと説明
    plt.suptitle('Method v6: Correct Predictions by Directory\n(True Positives Only - Ground Truth Accurate)', 
                 fontsize=20, fontweight='bold', y=0.95)
    
    # 統計情報をテキストとして追加
    total_correct = sum(directory_stats.values())
    total_directories = len(directory_stats)
    
    stats_text = f'Total Correct Predictions: {total_correct}\nDirectories with Correct Predictions: {total_directories}'
    ax.text(2, 98, stats_text, fontsize=12, va='top', ha='left',
            bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.8))
    
    # 凡例的な説明
    legend_text = 'Each rectangle shows the number of correctly predicted functions by Method v6\nOnly predictions that match ground truth are included'
    ax.text(50, 2, legend_text, fontsize=10, va='bottom', ha='center',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8))
    
    # ファイルに保存
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'method_v6_ground_truth_accurate_treemap.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Ground truth accurate treemap saved to {output_path}")
    
    # 統計情報を詳細出力
    print(f"\n=== Method v6 Ground Truth Accurate Results ===")
    print(f"Total correct predictions: {total_correct}")
    print(f"Total directories with correct predictions: {total_directories}")
    
    # ディレクトリ別の詳細統計
    print(f"\n=== Directory-wise Correct Predictions (Top 20) ===")
    for i, (directory, count) in enumerate(sorted_directories[:20]):
        percentage = (count / total_correct * 100) if total_correct > 0 else 0
        print(f"{directory:35} | Correct: {count:3} | Percentage: {percentage:5.1f}%")
    
    if len(sorted_directories) > 20:
        print(f"... and {len(sorted_directories) - 20} more directories")
    
    return output_path

def generate_ground_truth_accurate_data():
    """Ground truthに正確に一致するmethod_v6の予測データを生成"""
    print("Loading ground truth data...")
    ground_truth = load_ground_truth()
    
    print("Loading method v6 results...")
    evaluation_results, llm_outputs = load_method_v6_results()
    
    print("Extracting true positives by directory...")
    directory_stats = extract_true_positives_by_directory(ground_truth, llm_outputs, evaluation_results)
    
    return directory_stats

if __name__ == "__main__":
    try:
        print("Starting ground truth accurate treemap generation...")
        
        # Ground truthに一致するmethod_v6の予測のみを抽出
        directory_stats = generate_ground_truth_accurate_data()
        
        # Treemapを作成
        output_path = create_ground_truth_accurate_treemap(directory_stats)
        
        # データをJSON形式でも保存（参考用）
        json_output_path = "/workspace/create_graph/method_v6_ground_truth_accurate_data.json"
        with open(json_output_path, 'w') as f:
            json.dump(directory_stats, f, indent=2)
        
        print(f"Ground truth accurate data also saved to: {json_output_path}")
        print("✅ Ground truth accurate treemap generation completed successfully!")
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        import traceback
        traceback.print_exc() 