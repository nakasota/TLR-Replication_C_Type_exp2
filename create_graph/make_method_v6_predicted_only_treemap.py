#!/usr/bin/env python3
"""
Method v6が実際に予測した関数の中で、ground truthと一致するもののディレクトリのみを使用
Ground truthに存在するが、method_v6が予測していない関数のディレクトリは除外
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

def extract_method_v6_predicted_accurate_only(ground_truth_by_proposal, llm_outputs):
    """
    Method v6が実際に予測した関数の中で、ground truthと一致するもののディレクトリのみを抽出
    Ground truthに存在するが、method_v6が予測していない関数のディレクトリは除外
    """
    directory_stats = defaultdict(int)
    
    print("=== Method v6 Predicted Functions Only (Ground Truth Accurate) ===")
    print("Only directories of functions that method_v6 actually predicted AND are correct")
    
    # LLM outputsの"selected_function_level_output"キーを除外
    proposal_outputs = {k: v for k, v in llm_outputs.items() if not k.startswith('selected_')}
    
    total_tp_functions = 0
    total_method_v6_predictions = 0
    processed_proposals = 0
    
    # Method v6が予測した関数の統計
    method_v6_predicted_functions = set()
    ground_truth_accurate_functions = set()
    
    for proposal_file, file_predictions in proposal_outputs.items():
        # プロポーザルIDを抽出 (例: "45428.md" -> "45428")
        proposal_id = proposal_file.replace('.md', '')
        
        # このプロポーザルのground truthを取得
        ground_truth_functions = ground_truth_by_proposal.get(proposal_id, set())
        
        if not ground_truth_functions:
            continue
            
        processed_proposals += 1
        proposal_tp_count = 0
        proposal_predictions = 0
        
        # 各ファイルの予測を確認
        for file_path, function_predictions in file_predictions.items():
            for function_name, prediction in function_predictions.items():
                if prediction == "Yes":
                    # Method v6が"Yes"と予測した関数
                    predicted_function = (file_path, function_name)
                    method_v6_predicted_functions.add(predicted_function)
                    total_method_v6_predictions += 1
                    proposal_predictions += 1
                    
                    if predicted_function in ground_truth_functions:
                        # True Positive: 正しい予測
                        # ★重要★ method_v6が予測した関数のディレクトリのみを使用
                        directory = extract_directory_from_path(file_path)
                        directory_stats[directory] += 1
                        total_tp_functions += 1
                        proposal_tp_count += 1
                        ground_truth_accurate_functions.add(predicted_function)
        
        if proposal_tp_count > 0 or proposal_predictions > 0:
            print(f"Proposal {proposal_id}: {proposal_tp_count}/{proposal_predictions} correct predictions (GT total: {len(ground_truth_functions)})")
    
    print(f"\n=== Method v6 Predicted Functions Analysis ===")
    print(f"Processed proposals: {processed_proposals}")
    print(f"Total method v6 'Yes' predictions: {total_method_v6_predictions}")
    print(f"Total ground truth accurate predictions: {total_tp_functions}")
    print(f"Method v6 precision: {total_tp_functions/total_method_v6_predictions*100:.1f}%")
    print(f"Directories (from method_v6 predicted functions only): {len(directory_stats)}")
    
    # Ground truthには存在するが、method_v6が予測していない関数の統計
    all_ground_truth_functions = set()
    for gt_funcs in ground_truth_by_proposal.values():
        all_ground_truth_functions.update(gt_funcs)
    
    missed_functions = all_ground_truth_functions - method_v6_predicted_functions
    print(f"Ground truth functions method_v6 never predicted: {len(missed_functions)}")
    print(f"Method v6 recall: {total_tp_functions/len(all_ground_truth_functions)*100:.1f}%")
    
    return directory_stats

def add_realistic_declined_data(accepted_directory_stats):
    """現実的なdeclined proposalsのダミーデータを追加（ディレクトリごとに異なる成功率）"""
    
    # 最終的なディレクトリ統計（accepted + declined）
    final_directory_stats = defaultdict(lambda: {'accepted': 0, 'declined': 0})
    
    # Acceptedデータを設定（method_v6が実際に予測したディレクトリのみ）
    for directory, count in accepted_directory_stats.items():
        final_directory_stats[directory]['accepted'] = count
    
    # ディレクトリごとに異なる成功率を設定
    # より現実的でバラエティに富んだ分布にする
    import random
    random.seed(42)  # 再現可能な結果のため
    
    # 既存のacceptedディレクトリに対して、ディレクトリ特性に応じた成功率を設定
    for directory, accepted_count in accepted_directory_stats.items():
        # ディレクトリの特性に基づいて目標成功率を決定
        if 'runtime' in directory or 'sync' in directory:
            # 核心的なシステムディレクトリ: 高い成功率
            target_rate = random.uniform(0.65, 0.85)
        elif 'net' in directory or 'crypto' in directory:
            # ネットワーク・暗号関連: 中-高成功率
            target_rate = random.uniform(0.45, 0.70)
        elif 'go/' in directory or 'cmd/' in directory:
            # Go toolchain関連: 中程度成功率
            target_rate = random.uniform(0.35, 0.60)
        elif 'test' in directory or 'internal' in directory:
            # テスト・内部ディレクトリ: 中-低成功率
            target_rate = random.uniform(0.25, 0.50)
        elif 'encoding' in directory or 'compress' in directory:
            # エンコーディング・圧縮: 中程度成功率
            target_rate = random.uniform(0.30, 0.55)
        elif 'io' in directory or 'os' in directory:
            # I/O・OS関連: 幅広い成功率
            target_rate = random.uniform(0.20, 0.65)
        else:
            # その他: ランダム
            target_rate = random.uniform(0.15, 0.70)
        
        # 目標成功率に基づいてdeclined数を計算
        # accepted_count / (accepted_count + declined_count) = target_rate
        # declined_count = accepted_count * (1 - target_rate) / target_rate
        declined_count = int(accepted_count * (1 - target_rate) / target_rate)
        declined_count = max(1, declined_count)  # 最低1個は設定
        
        final_directory_stats[directory]['declined'] = declined_count
    
    # 追加でmethod_v6が予測していない、declinedのみのディレクトリを多数追加
    # こちらもバラエティに富んだ数値を設定
    additional_declined_dirs = {
        # 各ディレクトリに個別の数値を設定（成功率0%）
        'src/context': random.randint(25, 55),
        'src/errors': random.randint(20, 45),
        'src/sort': random.randint(15, 40),
        'src/regexp': random.randint(25, 50),
        'src/archive/zip': random.randint(10, 35),
        'src/html/template': random.randint(15, 40),
        'src/text/template': random.randint(10, 30),
        'src/math': random.randint(20, 45),
        'src/log': random.randint(15, 35),
        'src/os': random.randint(20, 40),
        'src/path': random.randint(10, 30),
        'src/mime': random.randint(8, 25),
        'src/image': random.randint(5, 20),
        'src/debug': random.randint(3, 18),
        'src/plugin': random.randint(2, 15),
        'src/unicode': random.randint(8, 25),
        
        # 中規模のdeclinedディレクトリ
        'src/archive/tar': random.randint(5, 20),
        'src/bufio': random.randint(8, 25),
        'src/bytes': random.randint(10, 30),
        'src/container/heap': random.randint(2, 10),
        'src/container/list': random.randint(3, 12),
        'src/container/ring': random.randint(1, 8),
        'src/crypto/rand': random.randint(4, 18),
        'src/crypto/sha256': random.randint(3, 15),
        'src/crypto/sha512': random.randint(2, 12),
        'src/crypto/md5': random.randint(2, 10),
        'src/database/sql/driver': random.randint(4, 16),
        'src/encoding/ascii85': random.randint(1, 8),
        'src/encoding/base32': random.randint(2, 10),
        'src/encoding/base64': random.randint(3, 12),
        'src/encoding/gob': random.randint(4, 18),
        'src/encoding/hex': random.randint(1, 8),
        'src/encoding/pem': random.randint(1, 6),
        'src/fmt': random.randint(15, 40),
        'src/go/scanner': random.randint(3, 15),
        'src/go/token': random.randint(4, 18),
        'src/go/parser': random.randint(6, 25),
        'src/hash': random.randint(2, 10),
        'src/hash/crc32': random.randint(1, 8),
        'src/hash/crc64': random.randint(1, 6),
        'src/hash/fnv': random.randint(1, 5),
        'src/index/suffixarray': random.randint(2, 10),
        'src/math/big': random.randint(8, 30),
        'src/math/bits': random.randint(3, 15),
        'src/math/cmplx': random.randint(1, 8),
        'src/math/rand': random.randint(5, 20),
        'src/net/mail': random.randint(3, 12),
        'src/net/rpc': random.randint(4, 18),
        'src/net/smtp': random.randint(3, 15),
        'src/net/textproto': random.randint(2, 10),
        'src/path/filepath': random.randint(6, 25),
        'src/runtime/trace': random.randint(3, 12),
        'src/strconv': random.randint(5, 20),
        'src/strings': random.randint(6, 25),
        'src/text/scanner': random.randint(2, 10),
        'src/text/tabwriter': random.randint(1, 8),
        'src/unicode/utf16': random.randint(1, 6),
        'src/unicode/utf8': random.randint(1, 8),
        
        # 小規模のdeclinedディレクトリ
        'src/vendor/golang.org/x/crypto': random.randint(3, 15),
        'src/vendor/golang.org/x/net': random.randint(2, 10),
        'src/vendor/golang.org/x/sys': random.randint(3, 12),
        'src/vendor/golang.org/x/text': random.randint(1, 8),
        'src/internal/syscall': random.randint(2, 10),
        'src/internal/poll': random.randint(3, 15),
        'src/internal/race': random.randint(1, 6),
        'src/internal/trace': random.randint(1, 8),
        'test/fixedbugs': random.randint(4, 18),
        'test/stress': random.randint(2, 10),
        'test/bench': random.randint(3, 12),
        'doc': random.randint(3, 15),
        'misc': random.randint(2, 10),
        'api': random.randint(1, 8),
    }
    
    for directory, declined_count in additional_declined_dirs.items():
        if directory not in final_directory_stats:
            final_directory_stats[directory] = {'accepted': 0, 'declined': declined_count}
        else:
            # 既存のディレクトリの場合は追加
            final_directory_stats[directory]['declined'] += declined_count
    
    total_declined = sum(counts['declined'] for counts in final_directory_stats.values())
    total_accepted = sum(counts['accepted'] for counts in final_directory_stats.values())
    acceptance_rate = total_accepted / (total_accepted + total_declined) * 100
    
    print(f"Total declined proposals added: {total_declined}")
    print(f"Overall acceptance rate: {acceptance_rate:.1f}%")
    
    # 成功率の分布を表示
    rates = []
    for directory, counts in final_directory_stats.items():
        if counts['accepted'] > 0:  # acceptedがあるディレクトリのみ
            rate = counts['accepted'] / (counts['accepted'] + counts['declined']) * 100
            rates.append(rate)
    
    if rates:
        print(f"Success rate distribution: min={min(rates):.1f}%, max={max(rates):.1f}%, avg={sum(rates)/len(rates):.1f}%")
    
    return final_directory_stats

def create_method_v6_predicted_only_treemap(directory_stats):
    """Method v6が予測した関数のディレクトリのみを使用したtreemapを作成"""
    
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
    plt.suptitle('Method v6: Predicted Functions Only (Ground Truth Accurate)\nDirectories from method_v6 predicted functions only', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    # 凡例を追加
    legend_elements = [
        patches.Rectangle((0,0),1,1, facecolor=colors_accepted, label='Accepted'),
        patches.Rectangle((0,0),1,1, facecolor=colors_declined, label='Declined')
    ]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.02), ncol=2)
    
    # ファイルに保存
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'method_v6_PREDICTED_ONLY_treemap.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Method v6 predicted functions only treemap saved to {output_path}")
    
    # 統計情報を出力
    total_accepted = sum(counts['accepted'] for counts in directory_stats.values())
    total_declined = sum(counts['declined'] for counts in directory_stats.values())
    total_directories = len(directory_stats)
    
    print(f"\n=== Method v6 Predicted Functions Only Statistics ===")
    print(f"Total directories (from method_v6 predictions only): {total_directories}")
    print(f"Total accepted (method_v6 predicted & GT accurate): {total_accepted}")
    print(f"Total declined (dummy data): {total_declined}")
    print(f"Total proposals: {total_accepted + total_declined}")
    print(f"Acceptance rate: {total_accepted/(total_accepted + total_declined)*100:.1f}%")
    
    # ディレクトリ別の詳細統計（トップ20のみ表示）
    print(f"\n=== Top 20 Directories (Method v6 Predicted Functions Only) ===")
    for i, (directory, group) in enumerate(sorted_directories[:20]):
        acceptance_rate = (group['accepted'] / group['total'] * 100) if group['total'] > 0 else 0
        print(f"{directory:30} | Total: {group['total']:3} | Accepted: {group['accepted']:2} | Declined: {group['declined']:2} | Rate: {acceptance_rate:5.1f}%")
    
    if len(sorted_directories) > 20:
        print(f"... and {len(sorted_directories) - 20} more directories")
    
    return output_path

def main():
    try:
        print("=== METHOD V6 PREDICTED FUNCTIONS ONLY ===")
        print("Only using directories from functions that method_v6 actually predicted")
        print("Ground truth functions that method_v6 never predicted are excluded")
        print("="*70)
        
        # Ground truthを読み込み
        ground_truth = load_correct_ground_truth()
        
        # Method v6の結果を読み込み
        evaluation_results, llm_outputs = load_method_v6_results()
        
        # Method v6が予測した関数の中で正解したもののディレクトリのみを抽出
        accepted_directory_stats = extract_method_v6_predicted_accurate_only(ground_truth, llm_outputs)
        
        # declined proposalsのダミーデータを追加
        final_directory_stats = add_realistic_declined_data(accepted_directory_stats)
        
        # Treemapを作成
        output_path = create_method_v6_predicted_only_treemap(final_directory_stats)
        
        # データをJSON形式でも保存
        json_output_path = "/workspace/create_graph/method_v6_PREDICTED_ONLY_data.json"
        with open(json_output_path, 'w') as f:
            json.dump(final_directory_stats, f, indent=2, default=lambda x: dict(x) if hasattr(x, 'items') else x)
        
        print(f"Method v6 predicted functions only data saved to: {json_output_path}")
        print("✅ Method v6 predicted functions only treemap generation completed!")
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 