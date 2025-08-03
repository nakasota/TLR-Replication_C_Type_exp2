import matplotlib.pyplot as plt
import numpy as np
import os

def parse_embedding_results():
    """Parse embedding-based evaluation results"""
    
    # Data from embedding_based/output/20250713_062003/evaluation_summary.md
    embedding_data = {
        'top_k': [5, 10, 20, 30, 40, 50],
        'file_embeddings': {
            'directory': {
                'precision': [0.311, 0.212, 0.149, 0.114, 0.096, 0.083],
                'recall': [0.502, 0.577, 0.664, 0.697, 0.729, 0.746],
                'f1': [0.338, 0.266, 0.208, 0.168, 0.146, 0.129]
            },
            'file': {
                'precision': [0.133, 0.099, 0.066, 0.052, 0.044, 0.039],
                'recall': [0.188, 0.257, 0.334, 0.388, 0.435, 0.465],
                'f1': [0.135, 0.122, 0.097, 0.081, 0.072, 0.065]
            }
        },
        'function_embeddings': {
            'directory': {
                'precision': [0.439, 0.333, 0.248, 0.207, 0.172, 0.146],
                'recall': [0.585, 0.627, 0.688, 0.725, 0.750, 0.765],
                'f1': [0.448, 0.377, 0.310, 0.268, 0.234, 0.207]
            },
            'file': {
                'precision': [0.309, 0.241, 0.183, 0.149, 0.126, 0.108],
                'recall': [0.332, 0.409, 0.501, 0.541, 0.573, 0.606],
                'f1': [0.280, 0.263, 0.230, 0.198, 0.175, 0.158]
            },
            'function': {
                'precision': [0.162, 0.123, 0.096, 0.078, 0.067, 0.059],
                'recall': [0.116, 0.170, 0.237, 0.277, 0.298, 0.323],
                'f1': [0.107, 0.111, 0.107, 0.096, 0.086, 0.080]
            }
        }
    }
    
    return embedding_data

def parse_llm_results():
    """Parse LLM-based evaluation results"""
    
    # Data from method_v6/function_level/output/20250712_163023/evaluation_summary.md
    llm_data = {
        'directory': {
            'precision': 0.713,
            'recall': 0.714,
            'f1': 0.657
        },
        'file': {
            'precision': 0.480,
            'recall': 0.537,
            'f1': 0.448
        },
        'function': {
            'precision': 0.248,
            'recall': 0.412,
            'f1': 0.264
        }
    }
    
    return llm_data

def create_comparison_graphs():
    """Create three comparison graphs for Precision, Recall, and F1"""
    
    embedding_data = parse_embedding_results()
    llm_data = parse_llm_results()
    top_k = embedding_data['top_k']
    
    # Set up the plotting style
    plt.rcParams.update({'font.size': 12, 'figure.figsize': (15, 5)})
    
    # Define colors and styles
    wine_red = "#7E1946"
    pink     = "#ff99cc"
    
    colors = {
        'func_emb': pink,           # Pink for embeddings
        'llm': wine_red             # Wine red for LLM
    }
    
    line_styles = {
        'directory': '-',
        'file': '--', 
        'function': ':'
    }
    
    metrics = ['precision', 'recall', 'f1']
    metric_titles = ['Precision', 'Recall', 'F1-Score']
    
    for i, (metric, title) in enumerate(zip(metrics, metric_titles)):
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Plot embedding-based results (Function embeddings only)
        if 'directory' in embedding_data['function_embeddings']:
            ax.plot(top_k, embedding_data['function_embeddings']['directory'][metric], 
                   color=colors['func_emb'], linestyle=line_styles['directory'], 
                   marker='o', linewidth=2, markersize=10,
                   label='Embed-based (Directory-Level)')
        
        if 'file' in embedding_data['function_embeddings']:
            ax.plot(top_k, embedding_data['function_embeddings']['file'][metric], 
                   color=colors['func_emb'], linestyle=line_styles['file'], 
                   marker='s', linewidth=2, markersize=10,
                   label='Embed-based (File-Level)')
        
        if 'function' in embedding_data['function_embeddings']:
            ax.plot(top_k, embedding_data['function_embeddings']['function'][metric], 
                   color=colors['func_emb'], linestyle=line_styles['function'], 
                   marker='^', linewidth=2, markersize=10,
                   label='Embed-based (Function-Level)')
        
        # Plot LLM-based results as horizontal lines
        ax.axhline(y=llm_data['directory'][metric], color=colors['llm'], 
                  linestyle=line_styles['directory'], linewidth=3, alpha=0.8,
                  label='LLM-based (Directory-Level)')
        
        ax.axhline(y=llm_data['file'][metric], color=colors['llm'], 
                  linestyle=line_styles['file'], linewidth=3, alpha=0.8,
                  label='LLM-based (File-Level)')
        
        ax.axhline(y=llm_data['function'][metric], color=colors['llm'], 
                  linestyle=line_styles['function'], linewidth=3, alpha=0.8,
                  label='LLM-based (Function-Level)')
        
        # Customize the plot
        ax.set_xlabel('Top-K', fontsize=14)
        ax.set_ylabel(title, fontsize=14)
        
        ax.set_xticks(top_k)
        ax.set_xlim(4, 52)
        ax.set_ylim(0, max(1.0, ax.get_ylim()[1] * 1.05))
        ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
        
        # Customize legend (inside the plot)
        # ax.legend(loc='upper right', fontsize=9, 
        #          frameon=True, fancybox=True, shadow=True)
        ax.legend(
            loc='upper right',
            fontsize='x-small',    # さらに小さいフォントサイズに
            markerscale=0.7,       # マーカーサイズを70%に縮小
            handlelength=1.5,      # 凡例内の線の長さを短く
            # labelspacing=0.3,      # 項目間の縦間隔を狭く
            # borderpad=0.2,         # 凡例と枠の余白を狭く
            frameon=True,
            fancybox=True,
            shadow=True
        )

        
        plt.tight_layout()
        
        # Save the plot
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(f'{output_dir}/RQ1_{metric}_comparison.png', dpi=300, bbox_inches='tight')
        
        print(f"Saved {title} comparison graph to {output_dir}/RQ1_{metric}_comparison.png")
        
        plt.show()

def print_summary_statistics():
    """Print summary statistics for analysis"""
    
    embedding_data = parse_embedding_results()
    llm_data = parse_llm_results()
    
    print("="*60)
    print("PERFORMANCE COMPARISON SUMMARY")
    print("="*60)
    
    print("\n🔍 EMBEDDING-BASED LOCALIZATION (Variable Performance)")
    print("-" * 50)
    
    print("\nFunction Embeddings (Best Performing):")
    for level in ['directory', 'file', 'function']:
        if level in embedding_data['function_embeddings']:
            data = embedding_data['function_embeddings'][level]
            print(f"  {level.capitalize()}-Level:")
            print(f"    Top-5:  P={data['precision'][0]:.3f}, R={data['recall'][0]:.3f}, F1={data['f1'][0]:.3f}")
            print(f"    Top-50: P={data['precision'][-1]:.3f}, R={data['recall'][-1]:.3f}, F1={data['f1'][-1]:.3f}")
    
    print("\n🤖 LLM-BASED LOCALIZATION (Fixed Performance)")
    print("-" * 50)
    for level in ['directory', 'file', 'function']:
        data = llm_data[level]
        print(f"  {level.capitalize()}-Level: P={data['precision']:.3f}, R={data['recall']:.3f}, F1={data['f1']:.3f}")
    
    print("\n📊 KEY INSIGHTS:")
    print("-" * 50)
    print("1. LLM-based shows consistent high performance at directory/file levels")
    print("2. Function embeddings with high Top-K can match LLM recall performance")
    print("3. LLM-based provides balanced precision-recall, embeddings show precision-recall trade-off")
    print("4. Embedding-based allows tuning Top-K for specific precision/recall requirements")

if __name__ == "__main__":
    print("Creating RQ1 Performance Comparison Graphs...")
    create_comparison_graphs()
    print_summary_statistics()
