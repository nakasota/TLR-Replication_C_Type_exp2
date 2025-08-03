import matplotlib.pyplot as plt
import matplotlib.patches as patches
import squarify
import numpy as np
import json
import os

def load_method_v6_data():
    """Load the extracted method_v6 data"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(script_dir, 'method_v6_treemap_data.json')
    
    with open(data_file, 'r') as f:
        raw_data = json.load(f)
    
    # Keep complete directory paths including 'src/' prefix
    # This shows the deepest directory level accurately
    return raw_data

# Load real method_v6 data
data = load_method_v6_data()

# 色の設定
colors_accepted = '#d62728'  # 赤
colors_declined = '#1f77b4'  # 青

def create_treemap():
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # ディレクトリごとにデータをグループ化
    directory_groups = {}
    for directory, counts in data.items():
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
        # フォントサイズを矩形のサイズに応じて調整（小さくても読めるように）
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
    
    # 凡例を追加
    legend_elements = [
        patches.Rectangle((0,0),1,1, facecolor=colors_accepted, label='Accepted Proposals'),
        patches.Rectangle((0,0),1,1, facecolor=colors_declined, label='Declined Proposals')
    ]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.02), ncol=2)
    
    # Save to file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'method_v6_treemap_chart.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Method v6 treemap chart saved to {output_path}")
    
    # 統計情報を出力
    total_accepted = sum(counts['accepted'] for counts in data.values())
    total_declined = sum(counts['declined'] for counts in data.values())
    total_directories = len(data)
    
    print(f"\n=== Method v6 Results Statistics ===")
    print(f"Total directories: {total_directories}")
    print(f"Total accepted proposals: {total_accepted}")
    print(f"Total declined proposals: {total_declined}")
    print(f"Total proposals: {total_accepted + total_declined}")
    print(f"Acceptance rate: {total_accepted/(total_accepted + total_declined)*100:.1f}%")
    
    # ディレクトリ別の詳細統計（トップ20のみ表示）
    print(f"\n=== Top 20 Directories by Total Proposals ===")
    for i, (directory, group) in enumerate(sorted_directories[:20]):
        acceptance_rate = (group['accepted'] / group['total'] * 100) if group['total'] > 0 else 0
        print(f"{directory:30} | Total: {group['total']:3} | Accepted: {group['accepted']:2} | Declined: {group['declined']:2} | Rate: {acceptance_rate:5.1f}%")
    
    if len(sorted_directories) > 20:
        print(f"... and {len(sorted_directories) - 20} more directories")
    
    # Optional: display the plot
    # plt.show()

if __name__ == "__main__":
    create_treemap()
