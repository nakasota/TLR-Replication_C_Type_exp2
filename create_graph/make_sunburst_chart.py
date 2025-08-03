import matplotlib.pyplot as plt
import numpy as np

# データ構造: {category: {'accepted': count, 'declined': count}}
data = {
    'net': {'accepted': 15, 'declined': 25},
    'crypto': {'accepted': 12, 'declined': 18},
    'runtime': {'accepted': 8, 'declined': 12},
    'reflect': {'accepted': 5, 'declined': 5}
}

# サブカテゴリのデータ
sub_data = {
    'net/http': {'accepted': 10, 'declined': 15},
    'net/tcp': {'accepted': 5, 'declined': 10},
    'crypto/aes': {'accepted': 8, 'declined': 12},
    'crypto/rsa': {'accepted': 4, 'declined': 6},
    'runtime/mem': {'accepted': 4, 'declined': 6},
    'runtime/sched': {'accepted': 4, 'declined': 6},
    'reflect/value': {'accepted': 3, 'declined': 4},
    'reflect/type': {'accepted': 2, 'declined': 1}
}

# 色の設定
colors_accepted = '#d62728'  # 赤
colors_declined = '#1f77b4'  # 青

# カテゴリごとの色のバリエーション（濃淡で区別）
category_colors = {
    'net': {'accepted': '#d62728', 'declined': '#1f77b4'},      # 標準の赤・青
    'crypto': {'accepted': '#ff7f0e', 'declined': '#2ca02c'},   # オレンジ・緑
    'runtime': {'accepted': '#9467bd', 'declined': '#8c564b'},  # 紫・茶
    'reflect': {'accepted': '#e377c2', 'declined': '#17becf'}   # ピンク・シアン
}

# カテゴリの順序を定義
category_order = ['net', 'crypto', 'runtime', 'reflect']

# 内側のリング用データ準備 - カテゴリごとにまとめ、スペーサーを追加
inner_labels = []
inner_sizes = []
inner_colors = []

for i, category in enumerate(category_order):
    counts = data[category]
    inner_labels.extend([f"{category}\n(accepted)", f"{category}\n(declined)"])
    inner_sizes.extend([counts['accepted'], counts['declined']])
    inner_colors.extend([category_colors[category]['accepted'], 
                        category_colors[category]['declined']])
    
    # カテゴリ間にスペーサーを追加（最後のカテゴリ以外）
    if i < len(category_order) - 1:
        inner_labels.append("")  # 空のラベル
        inner_sizes.append(2)    # 小さなスペーサー
        inner_colors.append('white')  # 白色でスペーサー

# 外側のリング用データ準備 - サブカテゴリもカテゴリごとにまとめ、スペーサーを追加
outer_labels = []
outer_sizes = []
outer_colors = []

# サブカテゴリをメインカテゴリ順に整理
ordered_sub_data = {}
for category in category_order:
    ordered_sub_data[category] = {}
    for sub_category, counts in sub_data.items():
        if sub_category.startswith(category + '/'):
            ordered_sub_data[category][sub_category] = counts

for i, category in enumerate(category_order):
    for sub_category, counts in ordered_sub_data[category].items():
        outer_labels.extend([f"{sub_category}\n(accepted)", f"{sub_category}\n(declined)"])
        outer_sizes.extend([counts['accepted'], counts['declined']])
        outer_colors.extend([category_colors[category]['accepted'], 
                            category_colors[category]['declined']])
    
    # カテゴリ間にスペーサーを追加（最後のカテゴリ以外）
    if i < len(category_order) - 1:
        outer_labels.append("")  # 空のラベル
        outer_sizes.append(3)    # 小さなスペーサー
        outer_colors.append('white')  # 白色でスペーサー

# 図の作成
fig, ax = plt.subplots(figsize=(14, 12))

# 内側のリング - startangleを調整してカテゴリをまとめる
wedges_inner, texts_inner = ax.pie(
    inner_sizes,
    labels=inner_labels,
    radius=0.7,
    colors=inner_colors,
    labeldistance=0.5,
    startangle=90,  # 開始角度を設定
    wedgeprops=dict(width=0.3, edgecolor='white', linewidth=2),
    textprops={'fontsize': 8, 'weight': 'bold'}
)

# 外側のリング - 内側と同じ開始角度でアライメント
wedges_outer, texts_outer = ax.pie(
    outer_sizes,
    labels=outer_labels,
    radius=1.0,
    colors=outer_colors,
    labeldistance=1.15,
    startangle=90,  # 内側と同じ開始角度
    wedgeprops=dict(width=0.3, edgecolor='white', linewidth=2),
    textprops={'fontsize': 7}
)

# タイトルと凡例
ax.set_title("Sunburst Chart: Go Proposals Distribution\nby Feature Category", 
             fontsize=14, fontweight='bold', pad=20)

# 凡例を追加 - カテゴリ別の色分けを含む
legend_elements = []
# Accepted/Declined の基本的な区別
legend_elements.extend([
    plt.Rectangle((0,0),1,1, facecolor='#d62728', label='Accepted Proposals'),
    plt.Rectangle((0,0),1,1, facecolor='#1f77b4', label='Declined Proposals')
])
# カテゴリ別の色分け
legend_elements.extend([
    plt.Rectangle((0,0),1,1, facecolor=category_colors['net']['accepted'], label='net'),
    plt.Rectangle((0,0),1,1, facecolor=category_colors['crypto']['accepted'], label='crypto'),
    plt.Rectangle((0,0),1,1, facecolor=category_colors['runtime']['accepted'], label='runtime'),
    plt.Rectangle((0,0),1,1, facecolor=category_colors['reflect']['accepted'], label='reflect')
])

ax.legend(handles=legend_elements, loc='center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# 等しいアスペクト比で円として描画
ax.set_aspect("equal")

# ファイルに保存
output_path = 'sunburst_chart.png'
plt.savefig(output_path, bbox_inches='tight', dpi=300)

print(f"Sunburst chart saved to {output_path}")

# Optional: display the plot
# plt.show()
