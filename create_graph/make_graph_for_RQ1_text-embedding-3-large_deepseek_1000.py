import matplotlib.pyplot as plt
import numpy as np
import os
import re
from pathlib import Path

def parse_embedding_results_from_file():
    """Parse embedding-based evaluation results from the latest OpenAI results"""
    
    # Path to the specific evaluation results
    results_dir = Path(__file__).parent.parent / 'embedding_based' / 'output' / '20250731_114126_openai_text-embedding-3-large'
    evaluation_file = results_dir / 'evaluation_summary.md'
    
    if not evaluation_file.exists():
        raise FileNotFoundError(f"Evaluation file not found: {evaluation_file}")
    
    print(f"📊 Reading evaluation results from: {evaluation_file}")
    
    # Read the evaluation summary
    with open(evaluation_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Initialize data structure
    embedding_data = {
        'top_k': [5, 10, 20, 30, 40, 50],
        'file_embeddings': {
            'directory': {'precision': [], 'recall': [], 'f1': []},
            'file': {'precision': [], 'recall': [], 'f1': []}
        },
        'function_embeddings': {
            'directory': {'precision': [], 'recall': [], 'f1': []},
            'file': {'precision': [], 'recall': [], 'f1': []},
            'function': {'precision': [], 'recall': [], 'f1': []}
        }
    }
    
    # Extract metrics from each section
    def extract_metrics_from_section(section_title):
        """Extract precision, recall, f1 values from a section"""
        # Find the section
        start_pattern = f"## {section_title}"
        end_pattern = r"## "
        
        start_idx = content.find(start_pattern)
        if start_idx == -1:
            print(f"⚠️  Could not find section: {section_title}")
            return [], [], []
        
        # Find the end of this section (next section or end of file)
        next_section_idx = content.find(end_pattern, start_idx + len(start_pattern))
        if next_section_idx == -1:
            section_content = content[start_idx:]
        else:
            section_content = content[start_idx:next_section_idx]
        
        # Extract values using regex
        precision_values = []
        recall_values = []
        f1_values = []
        
        # Pattern to match lines like "- Top-5: Precision=0.367, Recall=0.622, F1=0.401"
        pattern = r"- Top-(\d+): Precision=([\d.]+), Recall=([\d.]+), F1=([\d.]+)"
        matches = re.findall(pattern, section_content)
        
        for match in matches:
            k, prec, rec, f1 = match
            if int(k) in [5, 10, 20, 30, 40, 50]:
                precision_values.append(float(prec))
                recall_values.append(float(rec))
                f1_values.append(float(f1))
        
        return precision_values, recall_values, f1_values
    
    # Extract data for each section
    sections = [
        ("Directory-Level Macro Metrics (File Embeddings)", 'file_embeddings', 'directory'),
        ("File-Level Macro Metrics (File Embeddings)", 'file_embeddings', 'file'),
        ("Directory-Level Macro Metrics (Function Embeddings)", 'function_embeddings', 'directory'),
        ("File-Level Macro Metrics (Function Embeddings)", 'function_embeddings', 'file'),
        ("Function-Level Macro Metrics (Function Embeddings)", 'function_embeddings', 'function')
    ]
    
    for section_title, emb_type, granularity in sections:
        prec, rec, f1 = extract_metrics_from_section(section_title)
        if len(prec) == 6:  # Should have 6 values for k=5,10,20,30,40,50
            embedding_data[emb_type][granularity]['precision'] = prec
            embedding_data[emb_type][granularity]['recall'] = rec
            embedding_data[emb_type][granularity]['f1'] = f1
            print(f"✅ Extracted {section_title}: {len(prec)} values")
        else:
            print(f"⚠️  Unexpected number of values for {section_title}: {len(prec)}")
    
    print(f"✅ Successfully parsed embedding results")
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
    
    embedding_data = parse_embedding_results_from_file()
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
        
        # Add a main title indicating the embedding model used
        # fig.suptitle(f'{title} Comparison: OpenAI text-embedding-3-large vs LLM-based', 
        #             fontsize=14, fontweight='bold', y=0.98)
        
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
            loc='upper left',      # 凡例を左上に配置
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
        output_dir = 'output_deepseek_1000'
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(f'{output_dir}/RQ1_{metric}_comparison.png', dpi=300, bbox_inches='tight')
        
        print(f"Saved {title} comparison graph to {output_dir}/RQ1_{metric}_comparison.png")
        
        plt.show()

def print_summary_statistics():
    """Print summary statistics for analysis"""
    
    embedding_data = parse_embedding_results_from_file()
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

def main():
    """Main function to create all comparison graphs and print statistics"""
    print("="*70)
    print("RQ1 ANALYSIS: OpenAI text-embedding-3-large vs LLM-based Bug Localization")
    print("="*70)
    print("📁 Using results from: embedding_based/output/20250731_114126_openai_text-embedding-3-large/")
    print("="*70)
    
    create_comparison_graphs()
    print_summary_statistics()

if __name__ == "__main__":
    main()
