#!/usr/bin/env python3
"""
正しいground truthファイル（data/preprocess/accepted_proposals_ground_truth.json）を使用して
Method v6の正確な予測のみ（accepted）+ declined proposalsダミーデータを表示するTreemap
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import squarify
import numpy as np
import json
import os
from collections import defaultdict

def load_correct_ground_truth():
    """正しいground truthデータを読み込む"""
    ground_truth_path = "/workspace/data/preprocess/accepted_proposals_ground_truth.json"
    
    with open(ground_truth_path, 'r') as f:
        ground_truth_data = json.load(f)
    
    # Proposal IDごとにground truthを整理
    ground_truth_by_proposal = defaultdict(set)
    for entry in ground_truth_data:
        proposal_id = entry['proposal_id']
        detected_functions = entry.get('detected_functions', [])
        
        for func_data in detected_functions:
            function_name = func_data['function_name']
            file_path = func_data['file_path']
            ground_truth_by_proposal[proposal_id].add((file_path, function_name))
    
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

def extract_corrected_ground_truth_accurate_accepted(ground_truth_by_proposal, llm_outputs):
    """正しいground truthを使用してmethod_v6の正確な予測のみをカウント"""
    directory_stats = defaultdict(int)
    
    print("=== Using CORRECT Ground Truth File ===")
    print(f"Ground truth proposals available: {len(ground_truth_by_proposal)}")
    
    # LLM outputsの"selected_function_level_output"キーを除外
    proposal_outputs = {k: v for k, v in llm_outputs.items() if not k.startswith('selected_')}
    
    total_tp_functions = 0
    processed_proposals = 0
    total_gt_functions = sum(len(funcs) for funcs in ground_truth_by_proposal.values())
    
    print(f"Total ground truth functions: {total_gt_functions}")
    print(f"Method v6 proposals available: {len(proposal_outputs)}")
    
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
            print(f"Proposal {proposal_id}: {proposal_tp_count} true positive functions (GT: {len(ground_truth_functions)})")
    
    print(f"\n=== Corrected Accepted Summary ===")
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
    
    # 現実的なdeclined proposalsデータ
    realistic_declined_data = {
        # 大きなディレクトリにより多くのdeclined proposalsを追加
        'src/runtime': 12,
        'src/net/netip': 8,
        'src/syscall': 10,
        'src/sync/atomic': 6,
        'src/reflect': 8,
        'src/time': 6,
        'src/go/doc/comment': 5,
        'src/crypto/tls': 10,
        'src/io': 5,
        'src/crypto/ecdh': 4,
        'src/testing': 6,
        'src/go/types': 8,
        'src/encoding/binary': 5,
        'src/flag': 4,
        'src/crypto/x509': 6,
        'src/sync': 4,
        'src/go/build/constraint': 5,
        'src/net': 5,
        'src/io/fs': 4,
        'src/cmd/covdata': 3,
        'src/io/ioutil': 5,
        'src/net/http/httputil': 3,
        'src/compress/lzw': 3,
        'src/hash/maphash': 2,
        'src/os/signal': 4,
        'src/runtime/cgo': 2,
        'src/runtime/metrics': 2,
        'src/unicode/utf16': 2,
        'src/net/url': 10,
        'src/unicode/utf8': 2,
        'src/crypto/ed25519': 2,
        'src/crypto/subtle': 2,
        'src/strconv': 3,
        'src/strings': 3,
        'src/database/sql': 2,
        
        # 新しいディレクトリ（acceptedがない、または少ない）
        'src/net/smtp': 6,
        'src/encoding/json': 12,
        'src/path/filepath': 5,
        'src/net/http': 8,
        'src/fmt': 6,
        'src/bufio': 4,
        'src/math/big': 3,
        'src/mime/multipart': 2,
        'src/go/ast': 2,
        'src/go/printer': 2,
        
        # 追加のディレクトリ（acceptedがない）
        'src/context': 10,
        'src/errors': 6,
        'src/sort': 5,
        'src/math': 4,
        'src/os': 5,
        'src/regexp': 5,
        'src/archive/zip': 3,
        'src/encoding/xml': 4,
        'src/encoding/csv': 3,
        'src/image': 2,
        'src/html/template': 4,
        'src/text/template': 3,
    }
    
    print("Adding realistic declined data to match existing treemap format...")
    
    total_declined = 0
    for directory, declined_count in realistic_declined_data.items():
        final_directory_stats[directory]['declined'] = declined_count
        total_declined += declined_count
    
    print(f"Total declined proposals added: {total_declined}")
    
    return final_directory_stats

def create_corrected_ground_truth_treemap(directory_stats):
    """正しいground truthを使用したtreemapを作成"""
    
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
            
            # accepted のラベル
            if accepted_width > 1.5 and height > 1.5:
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
            
            # declined のラベル
            if declined_width > 1.5 and height > 1.5:
                label_size = min(12, max(4, int(width/8)))
                ax.text(declined_x + declined_width/2, y + height/2, 
                       f'{declined}',
                       ha='center', va='center', 
                       fontsize=label_size, 
                       fontweight='bold',
                       color='white')
        
        # ディレクトリ名のラベル
        base_font_size = max(5, min(12, int(width/12)))
        dir_label_size = max(4, base_font_size)
        
        # 長いパスの場合は改行して表示
        if len(directory) > 15 and '/' in directory and height > 10:
            parts = directory.split('/')
            if len(parts) > 2:
                display_name = f"{parts[0]}/\n{'/'.join(parts[1:])}"
            else:
                display_name = directory
        else:
            display_name = directory
        
        # ディレクトリ名を表示
        if height > 8:
            ax.text(x + width/2, y + height - 1, 
                   display_name,
                   ha='center', va='top', 
                   fontsize=dir_label_size, 
                   fontweight='bold',
                   color='black',
                   bbox=dict(boxstyle="round,pad=0.15", facecolor='white', alpha=0.85))
        else:
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
    plt.suptitle('Method v6: CORRECTED Ground Truth Accurate Accepted + Declined Proposals', 
                 fontsize=18, fontweight='bold', y=0.98)
    
    # 凡例を追加
    legend_elements = [
        patches.Rectangle((0,0),1,1, facecolor=colors_accepted, label='Accepted (CORRECTED Ground Truth Accurate)'),
        patches.Rectangle((0,0),1,1, facecolor=colors_declined, label='Declined Proposals (Dummy Data)')
    ]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.02), ncol=2)
    
    # ファイルに保存
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'method_v6_CORRECTED_ground_truth_treemap.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"CORRECTED ground truth treemap saved to {output_path}")
    
    # 統計情報を出力
    total_accepted = sum(counts['accepted'] for counts in directory_stats.values())
    total_declined = sum(counts['declined'] for counts in directory_stats.values())
    total_directories = len(directory_stats)
    
    print(f"\n=== CORRECTED Method v6 Results Statistics ===")
    print(f"Total directories: {total_directories}")
    print(f"Total accepted proposals (CORRECTED ground truth): {total_accepted}")
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

def main():
    try:
        print("=== USING CORRECT GROUND TRUTH FILE ===")
        print("File: data/preprocess/accepted_proposals_ground_truth.json")
        print("="*60)
        
        # 正しいground truthを読み込み
        ground_truth = load_correct_ground_truth()
        
        # Method v6の結果を読み込み
        evaluation_results, llm_outputs = load_method_v6_results()
        
        # 正しいground truthを使用してaccepted予測を抽出
        accepted_directory_stats = extract_corrected_ground_truth_accurate_accepted(ground_truth, llm_outputs)
        
        # declined proposalsのダミーデータを追加
        final_directory_stats = add_realistic_declined_data(accepted_directory_stats)
        
        # Treemapを作成
        output_path = create_corrected_ground_truth_treemap(final_directory_stats)
        
        # データをJSON形式でも保存
        json_output_path = "/workspace/create_graph/method_v6_CORRECTED_ground_truth_data.json"
        with open(json_output_path, 'w') as f:
            json.dump(final_directory_stats, f, indent=2, default=lambda x: dict(x) if hasattr(x, 'items') else x)
        
        print(f"CORRECTED ground truth data also saved to: {json_output_path}")
        print("✅ CORRECTED ground truth treemap generation completed successfully!")
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 