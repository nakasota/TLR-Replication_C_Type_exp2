#!/usr/bin/env python3
"""
Method v6のground truth正解データ（accepted）+ declined proposalsダミーデータを使用してTreemapを作成
既存のmethod_v6_treemap_chart.pngと同じ形式で、acceptedはground truth正確なmethod_v6予測のみを使用
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

def extract_ground_truth_accurate_accepted(ground_truth_by_proposal, llm_outputs, evaluation_results):
    """ディレクトリ別にmethod_v6のground truthに正確な予測のみをカウント（accepted用）"""
    directory_stats = defaultdict(int)
    
    print("=== Extracting Ground Truth Accurate Accepted Predictions ===")
    
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
        
        if proposal_tp_count > 0:
            print(f"Proposal {proposal_id}: {proposal_tp_count} true positive functions")
    
    print(f"\nAccepted Summary:")
    print(f"Processed proposals: {processed_proposals}")
    print(f"Total ground truth accurate accepted functions: {total_tp_functions}")
    print(f"Directories with correct accepted predictions: {len(directory_stats)}")
    
    return directory_stats

def add_realistic_declined_data(accepted_directory_stats):
    """現実的なdeclined proposalsのダミーデータを追加"""
    
    # 最終的なディレクトリ統計（accepted + declined）
    final_directory_stats = defaultdict(lambda: {'accepted': 0, 'declined': 0})
    
    # Acceptedデータを設定
    for directory, count in accepted_directory_stats.items():
        final_directory_stats[directory]['accepted'] = count
    
    # 現実的なdeclined proposalsデータ（元のextract_method_v6_data.pyから）
    realistic_declined_data = {
        # 大きなディレクトリにより多くのdeclined proposalsを追加
        'src/runtime': 12,          # 88 accepted + 12 declined = 100 total (88.0% acceptance)
        'src/net/netip': 8,         # 77 accepted + 8 declined = 85 total (90.6% acceptance)
        'src/syscall': 10,          # 61 accepted + 10 declined = 71 total (85.9% acceptance)
        'src/sync/atomic': 6,       # 41 accepted + 6 declined = 47 total (87.2% acceptance)
        'src/reflect': 8,           # 32 accepted + 8 declined = 40 total (80.0% acceptance)
        'src/time': 6,              # 19 accepted + 6 declined = 25 total (76.0% acceptance)
        'src/go/doc/comment': 5,    # 16 accepted + 5 declined = 21 total (76.2% acceptance)
        'src/crypto/tls': 10,       # 15 accepted + 10 declined = 25 total (60.0% acceptance)
        'src/io': 5,                # 15 accepted + 5 declined = 20 total (75.0% acceptance)
        'src/crypto/ecdh': 4,       # 13 accepted + 4 declined = 17 total (76.5% acceptance)
        'src/testing': 6,           # 12 accepted + 6 declined = 18 total (66.7% acceptance)
        'src/go/types': 8,          # 12 accepted + 8 declined = 20 total (60.0% acceptance)
        'src/encoding/binary': 5,   # 12 accepted + 5 declined = 17 total (70.6% acceptance)
        'src/flag': 4,              # 11 accepted + 4 declined = 15 total (73.3% acceptance)
        'src/crypto/x509': 6,       # 11 accepted + 6 declined = 17 total (64.7% acceptance)
        'src/sync': 4,              # 10 accepted + 4 declined = 14 total (71.4% acceptance)
        'src/go/build/constraint': 5, # 10 accepted + 5 declined = 15 total (66.7% acceptance)
        'src/net': 5,               # 9 accepted + 5 declined = 14 total (64.3% acceptance)
        'src/io/fs': 4,             # 9 accepted + 4 declined = 13 total (69.2% acceptance)
        'src/cmd/covdata': 3,       # 8 accepted + 3 declined = 11 total (72.7% acceptance)
        'src/io/ioutil': 5,         # 8 accepted + 5 declined = 13 total (61.5% acceptance)
        'src/net/http/httputil': 3, # 7 accepted + 3 declined = 10 total (70.0% acceptance)
        'src/compress/lzw': 3,      # 7 accepted + 3 declined = 10 total (70.0% acceptance)
        'src/hash/maphash': 2,      # 6 accepted + 2 declined = 8 total (75.0% acceptance)
        'src/os/signal': 4,         # 6 accepted + 4 declined = 10 total (60.0% acceptance)
        'src/runtime/cgo': 2,       # 6 accepted + 2 declined = 8 total (75.0% acceptance)
        'src/runtime/metrics': 2,   # 6 accepted + 2 declined = 8 total (75.0% acceptance)
        'src/unicode/utf16': 2,     # 6 accepted + 2 declined = 8 total (75.0% acceptance)
        'src/net/url': 10,          # 5 accepted + 10 declined = 15 total (33.3% acceptance) - 低い成功率
        'src/unicode/utf8': 2,      # 4 accepted + 2 declined = 6 total (66.7% acceptance)
        'src/crypto/ed25519': 2,    # 4 accepted + 2 declined = 6 total (66.7% acceptance)
        'src/crypto/subtle': 2,     # 4 accepted + 2 declined = 6 total (66.7% acceptance)
        'src/strconv': 3,           # 4 accepted + 3 declined = 7 total (57.1% acceptance)
        'src/strings': 3,           # 4 accepted + 3 declined = 7 total (57.1% acceptance)
        'src/database/sql': 2,      # 4 accepted + 2 declined = 6 total (66.7% acceptance)
        
        # 新しいディレクトリ（acceptedがない、または少ない）
        'src/net/smtp': 6,          # 1 accepted + 6 declined = 7 total (14.3% acceptance) - 非常に低い
        'src/encoding/json': 12,    # 1 accepted + 12 declined = 13 total (7.7% acceptance) - 非常に低い
        'src/path/filepath': 5,     # 5 accepted + 5 declined = 10 total (50.0% acceptance)
        'src/net/http': 8,          # 3 accepted + 8 declined = 11 total (27.3% acceptance) - 低い
        'src/fmt': 6,               # 2 accepted + 6 declined = 8 total (25.0% acceptance) - 低い
        'src/bufio': 4,             # 3 accepted + 4 declined = 7 total (42.9% acceptance)
        'src/math/big': 3,          # 2 accepted + 3 declined = 5 total (40.0% acceptance)
        'src/mime/multipart': 2,    # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        'src/go/ast': 2,            # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        'src/go/printer': 2,        # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        
        # 追加のディレクトリ（acceptedがない）
        'src/context': 10,          # 0 accepted + 10 declined = 10 total (0% acceptance)
        'src/errors': 6,            # 0 accepted + 6 declined = 6 total (0% acceptance)
        'src/sort': 5,              # 0 accepted + 5 declined = 5 total (0% acceptance)
        'src/math': 4,              # 0 accepted + 4 declined = 4 total (0% acceptance)
        'src/os': 5,                # 1 accepted + 5 declined = 6 total (16.7% acceptance)
        'src/regexp': 5,            # 0 accepted + 5 declined = 5 total (0% acceptance)
        'src/archive/zip': 3,       # 0 accepted + 3 declined = 3 total (0% acceptance)
        'src/encoding/xml': 4,      # 2 accepted + 4 declined = 6 total (33.3% acceptance)
        'src/encoding/csv': 3,      # 2 accepted + 3 declined = 5 total (40.0% acceptance)
        'src/image': 2,             # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        'src/html/template': 4,     # 0 accepted + 4 declined = 4 total (0% acceptance)
        'src/text/template': 3,     # 0 accepted + 3 declined = 3 total (0% acceptance)
    }
    
    print("Adding realistic declined data to match existing treemap format...")
    
    total_declined = 0
    for directory, declined_count in realistic_declined_data.items():
        final_directory_stats[directory]['declined'] = declined_count
        total_declined += declined_count
        print(f"  {directory}: +{declined_count} declined")
    
    print(f"Total declined proposals added: {total_declined}")
    
    return final_directory_stats

def create_ground_truth_accurate_treemap_with_declined(directory_stats):
    """Ground truthに正確なaccepted + declined proposalsを使用してtreemapを作成（既存形式と同じ）"""
    
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # ディレクトリごとにデータをグループ化
    directory_groups = {}
    for directory, counts in directory_stats.items():
        total = counts['accepted'] + counts['declined']
        directory_groups[directory] = {
            'accepted': counts['accepted'],
            'declined': counts['declined'], 
            'total': total
        }
    
    # ディレクトリを総数でソート（大きい順）
    sorted_directories = sorted(directory_groups.items(), key=lambda x: x[1]['total'], reverse=True)
    
    # squarifyを使用してtreemapのレイアウトを計算
    sizes = [group['total'] for _, group in sorted_directories]
    labels = [directory for directory, _ in sorted_directories]
    
    # treemapの座標を取得
    treemap_rects = squarify.normalize_sizes(sizes, 100, 100)
    treemap_coords = squarify.squarify(treemap_rects, 0, 0, 100, 100)
    
    # 色の設定
    colors_accepted = '#d62728'  # 赤
    colors_declined = '#1f77b4'  # 青
    
    # 各ディレクトリの位置情報を準備
    positions = []
    for i, (directory, group) in enumerate(sorted_directories):
        coord = treemap_coords[i]
        positions.append({
            'directory': directory,
            'x': coord['x'],
            'y': coord['y'],
            'width': coord['dx'],
            'height': coord['dy'],
            'accepted': group['accepted'],
            'declined': group['declined'],
            'total': group['total']
        })
    
    # 各ディレクトリを描画
    for pos in positions:
        x, y, width, height = pos['x'], pos['y'], pos['width'], pos['height']
        accepted, declined = pos['accepted'], pos['declined']
        total = pos['total']
        directory = pos['directory']
        
        # ディレクトリ全体の枠線（太い黒線）
        border_rect = patches.Rectangle(
            (x, y), width, height,
            facecolor='none', 
            edgecolor='black', 
            linewidth=3
        )
        ax.add_patch(border_rect)
        
        # accepted/declined の分割比率
        if total > 0:
            accepted_ratio = accepted / total
            declined_ratio = declined / total
        else:
            accepted_ratio = declined_ratio = 0
        
        # 横分割で accepted/declined を表示
        if accepted > 0:
            accepted_width = width * accepted_ratio
            accepted_rect = patches.Rectangle(
                (x, y), accepted_width, height,
                facecolor=colors_accepted, 
                edgecolor='white', 
                linewidth=1,
                alpha=0.8
            )
            ax.add_patch(accepted_rect)
            
            # accepted のラベル - accepted > 0 なら必ず表示
            if accepted_width > 1.5 and height > 1.5:  # 最小限のサイズ要件
                label_size = min(12, max(4, int(width/8)))
                ax.text(x + accepted_width/2, y + height/2, 
                       f'{accepted}',
                       ha='center', va='center', 
                       fontsize=label_size, 
                       fontweight='bold',
                       color='white')
        
        if declined > 0:
            declined_width = width * declined_ratio
            declined_x = x + (width * accepted_ratio)
            declined_rect = patches.Rectangle(
                (declined_x, y), declined_width, height,
                facecolor=colors_declined, 
                edgecolor='white', 
                linewidth=1,
                alpha=0.8
            )
            ax.add_patch(declined_rect)
            
            # declined のラベル - declined > 0 なら必ず表示
            if declined_width > 1.5 and height > 1.5:  # 最小限のサイズ要件
                label_size = min(12, max(4, int(width/8)))
                ax.text(declined_x + declined_width/2, y + height/2, 
                       f'{declined}',
                       ha='center', va='center', 
                       fontsize=label_size, 
                       fontweight='bold',
                       color='white')
        
        # ディレクトリ名のラベル - 常にフルパスを表示（省略なし）
        base_font_size = max(5, min(12, int(width/12)))
        dir_label_size = max(4, base_font_size)  # 最小4ピクセル、最大12ピクセル
        
        # 長いパスの場合は改行して表示（高さに余裕がある場合のみ）
        if len(directory) > 15 and '/' in directory and height > 10:
            parts = directory.split('/')
            if len(parts) > 2:
                display_name = f"{parts[0]}/\n{'/'.join(parts[1:])}"
            else:
                display_name = directory
        else:
            display_name = directory
        
        # 矩形のサイズに関係なく、常にフルパスを表示
        if height > 8:  # 高さがある場合は上部に表示
            ax.text(x + width/2, y + height - 1, 
                   display_name,
                   ha='center', va='top', 
                   fontsize=dir_label_size, 
                   fontweight='bold',
                   color='black',
                   bbox=dict(boxstyle="round,pad=0.15", facecolor='white', alpha=0.85))
        else:  # 高さが少ない場合は中央に表示
            # 小さい矩形の場合はさらにフォントサイズを調整
            small_font_size = max(3, min(dir_label_size, int(height/2)))
            ax.text(x + width/2, y + height/2, 
                   display_name,
                   ha='center', va='center', 
                   fontsize=small_font_size, 
                   fontweight='bold',
                   color='black',
                   bbox=dict(boxstyle="round,pad=0.1", facecolor='white', alpha=0.85))
    
    # 軸の設定
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # タイトルを追加
    plt.suptitle('Method v6: Ground Truth Accurate Accepted + Declined Proposals by Directory', 
                 fontsize=18, fontweight='bold', y=0.98)
    
    # 凡例を追加
    legend_elements = [
        patches.Rectangle((0,0),1,1, facecolor=colors_accepted, label='Accepted Proposals (Ground Truth Accurate)'),
        patches.Rectangle((0,0),1,1, facecolor=colors_declined, label='Declined Proposals (Dummy Data)')
    ]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.02), ncol=2)
    
    # ファイルに保存
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'method_v6_ground_truth_accurate_with_declined_treemap.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Ground truth accurate treemap (with declined) saved to {output_path}")
    
    # 統計情報を出力
    total_accepted = sum(counts['accepted'] for counts in directory_stats.values())
    total_declined = sum(counts['declined'] for counts in directory_stats.values())
    total_directories = len(directory_stats)
    
    print(f"\n=== Ground Truth Accurate Method v6 Results Statistics ===")
    print(f"Total directories: {total_directories}")
    print(f"Total accepted proposals (ground truth accurate): {total_accepted}")
    print(f"Total declined proposals (dummy data): {total_declined}")
    print(f"Total proposals: {total_accepted + total_declined}")
    print(f"Acceptance rate: {total_accepted/(total_accepted + total_declined)*100:.1f}%")
    
    # ディレクトリ別の詳細統計（トップ20のみ表示）
    print(f"\n=== Top 20 Directories by Total Proposals ===")
    for i, (directory, group) in enumerate(sorted_directories[:20]):
        acceptance_rate = (group['accepted'] / group['total'] * 100) if group['total'] > 0 else 0
        print(f"{directory:30} | Total: {group['total']:3} | Accepted: {group['accepted']:2} | Declined: {group['declined']:2} | Rate: {acceptance_rate:5.1f}%")
    
    if len(sorted_directories) > 20:
        print(f"... and {len(sorted_directories) - 20} more directories")
    
    return output_path

def generate_ground_truth_accurate_treemap_data():
    """Ground truthに正確なmethod_v6予測（accepted）+ declined proposalsのtreemapデータを生成"""
    print("Loading ground truth data...")
    ground_truth = load_ground_truth()
    
    print("Loading method v6 results...")
    evaluation_results, llm_outputs = load_method_v6_results()
    
    print("Extracting ground truth accurate accepted predictions...")
    accepted_directory_stats = extract_ground_truth_accurate_accepted(ground_truth, llm_outputs, evaluation_results)
    
    print("Adding declined proposals dummy data...")
    final_directory_stats = add_realistic_declined_data(accepted_directory_stats)
    
    return final_directory_stats

if __name__ == "__main__":
    try:
        print("Starting ground truth accurate treemap with declined data generation...")
        
        # Ground truthに正確なaccepted + declined proposalsデータを生成
        directory_stats = generate_ground_truth_accurate_treemap_data()
        
        # Treemapを作成
        output_path = create_ground_truth_accurate_treemap_with_declined(directory_stats)
        
        # データをJSON形式でも保存（参考用）
        json_output_path = "/workspace/create_graph/method_v6_ground_truth_accurate_with_declined_data.json"
        with open(json_output_path, 'w') as f:
            json.dump(directory_stats, f, indent=2, default=lambda x: dict(x) if hasattr(x, 'items') else x)
        
        print(f"Ground truth accurate data (with declined) also saved to: {json_output_path}")
        print("✅ Ground truth accurate treemap (with declined) generation completed successfully!")
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        import traceback
        traceback.print_exc() 