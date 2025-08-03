#!/usr/bin/env python3
"""
Embedding-Based Localization with Full Multi-Granularity Evaluation,
Markdown Reporting, and Timestamped Plots Directory

Evaluates proposals at directory, file, and function levels using both file
and function embeddings. Computes Precision, Recall, F1 at:
  - File embeddings: directory & file levels
  - Function embeddings: directory, file, & function levels

Outputs:
  1. A detailed Markdown summary (with ✅/❌ markers)
  2. Three plots (Precision, Recall, F1 vs Top-k)

All outputs are written into:
  embedding_based/output/{TIMESTAMP}/
where TIMESTAMP is in YYYYMMDD_HHMMSS format.
"""
import glob
import json
import pickle
import numpy as np
import matplotlib.pyplot as plt
import argparse
import gc
from pathlib import Path
from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity
from openai_embedding_utils import create_openai_embedding_model

# Import tiktoken for accurate token counting
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("⚠️  tiktoken not available for cost calculation")

# text-embedding-3-large pricing (per 1M tokens)
EMBEDDING_PRICE = 0.13

# Global cost tracking
total_tokens_used = 0
total_cost = 0.0

def count_tokens_for_embedding(text: str) -> int:
    """Count tokens for text-embedding-3-large"""
    if TIKTOKEN_AVAILABLE:
        try:
            tokenizer = tiktoken.encoding_for_model("text-embedding-3-large")
            return len(tokenizer.encode(text))
        except:
            try:
                tokenizer = tiktoken.get_encoding("cl100k_base")
                return len(tokenizer.encode(text))
            except:
                pass
    # Fallback: rough estimation (4 chars per token)
    return len(text) // 4

def track_embedding_cost(text: str, description: str):
    """Track embedding cost for a text"""
    global total_tokens_used, total_cost
    tokens = count_tokens_for_embedding(text)
    cost = (tokens / 1_000_000) * EMBEDDING_PRICE
    total_tokens_used += tokens
    total_cost += cost
    print(f"[COST] {description}: {tokens:,} tokens, ${cost:.6f}")

def save_embedding_cost_report(output_dir: Path):
    """Save embedding cost report"""
    cost_report = {
        'script_info': {
            'script_name': 'embedding_based_localization_full.py',
            'model': 'text-embedding-3-large',
            'execution_time': datetime.now().isoformat(),
            'tiktoken_available': TIKTOKEN_AVAILABLE
        },
        'summary': {
            'total_tokens_used': total_tokens_used,
            'total_cost_usd': total_cost,
            'price_per_1m_tokens': EMBEDDING_PRICE
        }
    }
    
    cost_file = output_dir / 'embedding_cost_report.json'
    with open(cost_file, 'w') as f:
        json.dump(cost_report, f, indent=2)
    
    print(f"\n💰 EMBEDDING COST SUMMARY:")
    print(f"   Total tokens used: {total_tokens_used:,}")
    print(f"   Total cost: ${total_cost:.6f}")
    print(f"   Cost report saved: {cost_file}")
    
    return cost_file

def load_proposals(proposals_dir: Path):
    return sorted(glob.glob(str(proposals_dir / '*.md')))

def read_markdown(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def load_ground_truth(gt_path: Path):
    with open(gt_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Handle new data structure where ground truth is under 'ground_truth' key
    if isinstance(data, dict) and 'ground_truth' in data:
        entries = data['ground_truth']
    else:
        # Fallback to old format where data is directly a list
        entries = data
    
    gt = {}
    for entry in entries:
        pid = str(entry['proposal_id'])
        files = entry.get('files', [])
        dirs = sorted({str(Path(fp).parent) for fp in files})
        funcs = [(d['file_path'], d['function_name']) for d in entry.get('detected_functions', [])]
        gt[pid] = {'directory': dirs, 'file': files, 'function': funcs}
    return gt

def unique(seq):
    seen, out = set(), []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

def compute_metrics(pred, true):
    pu = unique(pred)
    tu = unique(true)
    tp = len(set(pu) & set(tu))
    fp = len(set(pu) - set(tu))
    fn = len(set(tu) - set(pu))
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec  = tp / (tp + fn) if (tp + fn) else 0.0
    f1   = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
    return prec, rec, f1

def get_directory(path_str: str) -> str:
    return str(Path(path_str).parent)

def write_markdown(output_dir: Path, ks, metrics, per_preds, ground_truth):
    md = []
    date = datetime.now().strftime('%Y-%m-%d')
    md.append(f"# Embedding-Based Localization Evaluation Summary ({date})\n")
    md.append(f"Processed Proposals: {len(per_preds)}\n")

    # --- File embeddings ---
    md.append("## Directory-Level Macro Metrics (File Embeddings)\n")
    for k in ks:
        p, r, f1 = np.mean(metrics['file_emb']['directory'][k], axis=0)
        md.append(f"- Top-{k}: Precision={p:.3f}, Recall={r:.3f}, F1={f1:.3f}")
    md.append("\n## File-Level Macro Metrics (File Embeddings)\n")
    for k in ks:
        p, r, f1 = np.mean(metrics['file_emb']['file'][k], axis=0)
        md.append(f"- Top-{k}: Precision={p:.3f}, Recall={r:.3f}, F1={f1:.3f}")

    # --- Function embeddings ---
    md.append("\n## Directory-Level Macro Metrics (Function Embeddings)\n")
    for k in ks:
        p, r, f1 = np.mean(metrics['func_emb']['directory'][k], axis=0)
        md.append(f"- Top-{k}: Precision={p:.3f}, Recall={r:.3f}, F1={f1:.3f}")
    md.append("\n## File-Level Macro Metrics (Function Embeddings)\n")
    for k in ks:
        p, r, f1 = np.mean(metrics['func_emb']['file'][k], axis=0)
        md.append(f"- Top-{k}: Precision={p:.3f}, Recall={r:.3f}, F1={f1:.3f}")
    md.append("\n## Function-Level Macro Metrics (Function Embeddings)\n")
    for k in ks:
        p, r, f1 = np.mean(metrics['func_emb']['function'][k], axis=0)
        md.append(f"- Top-{k}: Precision={p:.3f}, Recall={r:.3f}, F1={f1:.3f}")

    # Detailed per-proposal
    md.append("\n## Detailed Per-Proposal Comparisons\n")
    for pid, pred in per_preds.items():
        gt = ground_truth[pid]
        md.append(f"### 📊 Proposal #{pid}\n")
        md.append("#### File Embeddings - Directory Level")
        for d in gt['directory']:
            mark = '✅' if d in pred['dirs'] else '❌'
            md.append(f"- {mark} `{d}`")
        md.append("")
        md.append("#### File Embeddings - File Level")
        for f in gt['file']:
            mark = '✅' if f in pred['files'] else '❌'
            md.append(f"- {mark} `{f}`")
        md.append("")
        md.append("#### Function Embeddings - Directory Level")
        for d in gt['directory']:
            mark = '✅' if d in pred['func_dirs'] else '❌'
            md.append(f"- {mark} `{d}`")
        md.append("")
        md.append("#### Function Embeddings - File Level")
        for f in gt['file']:
            mark = '✅' if f in pred['func_files'] else '❌'
            md.append(f"- {mark} `{f}`")
        md.append("")
        md.append("#### Function Embeddings - Function Level")
        for fn in gt['function']:
            mark = '✅' if fn in pred['func_funcs'] else '❌'
            md.append(f"- {mark} (`{fn[0]}`, `{fn[1]}`)")
        md.append("")

    out = output_dir / 'evaluation_summary.md'
    with open(out, 'w', encoding='utf-8') as f:
        f.write("\n".join(md))
    print(f"📝 Markdown summary written to {out}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Embedding-based localization evaluation")
    parser.add_argument('--max-proposals', type=int, default=10, help='Maximum number of proposals to process for testing (default: 10)')
    parser.add_argument('--prop-dir', type=str, help='Directory containing proposal files')
    parser.add_argument('--gt-file', type=str, help='Ground truth JSON file path')
    parser.add_argument('--all', action='store_true', help='Process all proposals (overrides --max-proposals)')
    args = parser.parse_args()
    
    # Set default paths
    base = Path(__file__).parent.parent
    if args.prop_dir:
        prop_dir = Path(args.prop_dir)
    else:
        prop_dir = base / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals_for_embedding_content_validated'
    
    if args.gt_file:
        gt_file = Path(args.gt_file)
    else:
        gt_file = base / 'data' / 'ground_truth' / 'accepted_proposals_ground_truth_content_validated.json'
        
    embed_dir = base / 'embedding_based' / 'output'
    embed_dir.mkdir(parents=True, exist_ok=True)

    # --- create a timestamped results folder with OpenAI identifier ---
    ts        = datetime.now().strftime('%Y%m%d_%H%M%S')
    result_dir = embed_dir / f"{ts}_openai_text-embedding-3-large"
    result_dir.mkdir(parents=True, exist_ok=True)
    print(f"➡️  Writing OpenAI results to: {result_dir}")

    # Load proposals and ground-truth
    proposals    = load_proposals(prop_dir)
    ground_truth = load_ground_truth(gt_file)
    
    print(f"📄 Loaded {len(proposals)} proposals")
    print(f"📊 Loaded ground truth for {len(ground_truth)} proposals")
    
    # Limit the number of proposals if specified
    if args.all:
        print(f"🔢 Processing all {len(proposals)} proposals")
    elif args.max_proposals:
        proposals = proposals[:args.max_proposals]
        print(f"🔢 Limited to {len(proposals)} proposals for testing")
    else:
        proposals = proposals[:10]  # Default to 10 proposals
        print(f"🔢 Limited to {len(proposals)} proposals for testing (use --all to process all)")

    # Load precomputed OpenAI embeddings
    # Note: Using embeddings generated by embedding_creator_for_file_and_func.py
    embedding_based_dir = Path(__file__).parent
    openai_embed_dir = embedding_based_dir / "embeddings_cache_openai"
    
    # Validate paths
    print(f"📁 Proposal directory: {prop_dir}")
    print(f"📁 Ground truth file: {gt_file}")
    print(f"📁 Embedding directory: {openai_embed_dir}")
    
    if not prop_dir.exists():
        print(f"❌ Proposal directory not found: {prop_dir}")
        return
    
    if not gt_file.exists():
        print(f"❌ Ground truth file not found: {gt_file}")
        return
        
    if not openai_embed_dir.exists():
        print(f"❌ Embedding directory not found: {openai_embed_dir}")
        return
    
    try:
        # Load OpenAI embeddings with available file names
        # Try different possible file names for file embeddings
        file_emb_files = [
            'file_embeddings.pkl',
            'all_file_embeddings.pkl',
            'intermediate/file_embeddings_batch_2.pkl'
        ]
        
        file_embs = None
        for file_name in file_emb_files:
            try:
                with open(openai_embed_dir / file_name, 'rb') as f:
                    file_embs = pickle.load(f)
                print(f"✅ Loaded file embeddings from {file_name}")
                break
            except FileNotFoundError:
                continue
        
        if file_embs is None:
            raise FileNotFoundError("No file embeddings found")
        
        file_embs = np.array(file_embs)
        
        with open(openai_embed_dir / 'file_paths.pkl', 'rb') as f:
            file_paths = pickle.load(f)
        
        # Try different possible file names for function embeddings
        func_emb_files = [
            'function_embeddings.pkl',
            'all_function_embeddings.pkl'
        ]
        
        func_embs = None
        func_ids = None
        
        # If no function embeddings available, create dummy data for files only
        for file_name in func_emb_files:
            try:
                with open(openai_embed_dir / file_name, 'rb') as f:
                    func_embs = pickle.load(f)
                print(f"✅ Loaded function embeddings from {file_name}")
                break
            except FileNotFoundError:
                continue
        
        if func_embs is None:
            print("⚠️  No function embeddings found, using file embeddings only")
            # Use file embeddings as function embeddings for file-level evaluation only
            func_embs = file_embs.copy()
            # Create dummy function identifiers based on file paths
            func_ids = [(path, f"dummy_func_{i}") for i, path in enumerate(file_paths)]
        else:
            func_embs = np.array(func_embs)
            with open(openai_embed_dir / 'function_identifiers.pkl', 'rb') as f:
                func_ids = pickle.load(f)
        
        print(f"✅ Loaded OpenAI embeddings from {openai_embed_dir}")
        print(f"   Files: {len(file_paths)}, Functions: {len(func_ids)}")
    except FileNotFoundError as e:
        print(f"❌ OpenAI embedding files not found in {openai_embed_dir}")
        print("Please run embedding_creator_for_file_and_func.py first to generate OpenAI embeddings")
        raise e

    print("🤖 Loading embedding model: text-embedding-3-large")
    model = create_openai_embedding_model('text-embedding-3-large')
    ks    = [5,10,20,30,40,50]

    # Initialize accumulators
    metrics  = {
        'file_emb': {
            'directory': {k: [] for k in ks},
            'file':      {k: [] for k in ks},
        },
        'func_emb': {
            'directory': {k: [] for k in ks},
            'file':      {k: [] for k in ks},
            'function':  {k: [] for k in ks},
        }
    }
    per_preds = {}

    # Main loop
    total_proposals = len(proposals)
    processed_count = 0
    for prop in proposals:
        pid = Path(prop).stem
        
        # Skip proposals not in ground truth
        if pid not in ground_truth:
            print(f"⚠️  Skipping proposal {pid} - not in ground truth")
            continue
            
        processed_count += 1
        print(f"🔍 Processing proposal {pid}... ({processed_count}/{total_proposals})")
        
        # Track embedding cost for this proposal
        proposal_text = read_markdown(prop)
        track_embedding_cost(proposal_text, f"Proposal {pid}")
        
        emb     = model.encode([proposal_text], show_progress_bar=False)
        sims_f  = cosine_similarity(emb, file_embs)[0]
        idxs_f  = np.argsort(-sims_f)
        sims_fn = cosine_similarity(emb, func_embs)[0]
        idxs_fn = np.argsort(-sims_fn)
        
        # Clear memory after computing similarities
        del emb, proposal_text
        gc.collect()

        for k in ks:
            # File embeddings
            topf = [file_paths[i] for i in idxs_f[:k]]
            topd = [get_directory(fp) for fp in topf]
            metrics['file_emb']['file'][k].append(
                compute_metrics(topf, ground_truth[pid]['file'])[:3]
            )
            metrics['file_emb']['directory'][k].append(
                compute_metrics(topd, ground_truth[pid]['directory'])[:3]
            )
            
            # Clear temporary variables
            del topf, topd
            # Function embeddings
            topfn = [func_ids[i] for i in idxs_fn[:k]]
            topff = [fp for fp,_ in topfn]
            topfd = [get_directory(fp) for fp,_ in topfn]
            metrics['func_emb']['function'][k].append(
                compute_metrics(topfn, ground_truth[pid]['function'])[:3]
            )
            metrics['func_emb']['file'][k].append(
                compute_metrics(topff, ground_truth[pid]['file'])[:3]
            )
            metrics['func_emb']['directory'][k].append(
                compute_metrics(topfd, ground_truth[pid]['directory'])[:3]
            )

            if k == ks[0]:
                per_preds[pid] = {
                    'dirs':       unique(topd),
                    'files':      unique(topf),
                    'func_dirs':  unique(topfd),
                    'func_files': unique(topff),
                    'func_funcs': unique(topfn),
                }
            
            # Clear temporary variables
            del topfn, topff, topfd
        
        # Clean up variables after processing each proposal
        del sims_f, idxs_f, sims_fn, idxs_fn
        gc.collect()
        
        # Force garbage collection every 5 proposals
        if processed_count % 5 == 0:
            print(f"   🧹 Memory cleanup after {processed_count} proposals")
            gc.collect()

    # Write Markdown
    write_markdown(result_dir, ks, metrics, per_preds, ground_truth)

    # Prepare macro-metric series for plotting
    series = {}
    for name in ['file_dir','file_file','func_dir','func_file','func_func']:
        series[name] = { m: [] for m in ['prec','rec','f1'] }

    for k in ks:
        fd = np.mean(metrics['file_emb']['directory'][k], axis=0)
        ff = np.mean(metrics['file_emb']['file'][k],      axis=0)
        td = np.mean(metrics['func_emb']['directory'][k], axis=0)
        tf = np.mean(metrics['func_emb']['file'][k],      axis=0)
        fn = np.mean(metrics['func_emb']['function'][k],  axis=0)
        series['file_dir']['prec'].append(fd[0]); series['file_dir']['rec'].append(fd[1]); series['file_dir']['f1'].append(fd[2])
        series['file_file']['prec'].append(ff[0]); series['file_file']['rec'].append(ff[1]); series['file_file']['f1'].append(ff[2])
        series['func_dir']['prec'].append(td[0]); series['func_dir']['rec'].append(td[1]); series['func_dir']['f1'].append(td[2])
        series['func_file']['prec'].append(tf[0]); series['func_file']['rec'].append(tf[1]); series['func_file']['f1'].append(tf[2])
        series['func_func']['prec'].append(fn[0]); series['func_func']['rec'].append(fn[1]); series['func_func']['f1'].append(fn[2])

    # Plotting helper
    def plot_metric(metric_key, ylabel, filename):
        plt.figure()
        labels = [
            'Directory (File Embedding)',
            'File      (File Embedding)',
            'Directory (Function Embedding)',
            'File      (Function Embedding)',
            'Function  (Function Embedding)',
        ]
        keys   = ['file_dir','file_file','func_dir','func_file','func_func']
        for key, label in zip(keys, labels):
            plt.plot(ks, series[key][metric_key], marker='o', label=label)
        plt.xlabel('Top-k')
        plt.ylabel(ylabel)
        plt.title(f'{ylabel} vs Top-k')
        plt.grid(True)
        plt.legend()
        plt.xlim(0, 55)
        plt.ylim(0, 1.0)
        plt.savefig(result_dir / filename)
        plt.close()
        print(f"🖼️  Saved plot: {filename}")

    # Generate the three plots:
    plot_metric('prec', 'Precision', 'precision.png')
    plot_metric('rec',  'Recall',    'recall.png')
    plot_metric('f1',   'F1-Score',  'f1.png')
    
    # Save embedding cost report
    save_embedding_cost_report(result_dir)


if __name__ == '__main__':
    main()
