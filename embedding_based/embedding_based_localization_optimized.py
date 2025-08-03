#!/usr/bin/env python3
"""
Memory-optimized version of embedding-based localization with batch processing
to reduce memory usage for large datasets.
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
            pass
    # Fallback estimation
    return len(text.split()) * 1.3

def load_proposals(proposal_dir):
    """Load proposal markdown files"""
    proposals = []
    for file_path in Path(proposal_dir).glob("*.md"):
        if file_path.name == "COPY_SUMMARY.md":
            continue
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        proposal_id = file_path.stem
        proposals.append({
            'id': proposal_id,
            'content': content,
            'file_path': str(file_path)
        })
    return sorted(proposals, key=lambda x: x['id'])

def load_ground_truth(gt_file):
    """Load ground truth data"""
    with open(gt_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def track_embedding_cost(text: str):
    """Track API cost for embeddings"""
    global total_tokens_used, total_cost
    tokens = count_tokens_for_embedding(text)
    cost = (tokens / 1_000_000) * EMBEDDING_PRICE
    total_tokens_used += tokens
    total_cost += cost
    return tokens, cost

def save_embedding_cost_report(output_dir):
    """Save cost tracking report"""
    report = {
        'total_tokens': total_tokens_used,
        'total_cost_usd': round(total_cost, 6),
        'model': 'text-embedding-3-large',
        'price_per_1m_tokens': EMBEDDING_PRICE,
        'timestamp': datetime.now().isoformat()
    }
    
    cost_file = output_dir / 'embedding_cost_report.json'
    with open(cost_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"💰 Total embedding cost: ${total_cost:.6f} ({total_tokens_used:,} tokens)")
    print(f"📊 Cost report saved to: {cost_file}")

def process_proposals_in_batches(proposals, ground_truth, file_embs, func_embs, 
                                file_paths, func_data, embedding_model, 
                                output_dir, batch_size=10):
    """Process proposals in batches to reduce memory usage"""
    
    results = {
        'top_k_values': list(range(1, 21)),
        'file_level': {'prec': [], 'rec': [], 'f1': []},
        'dir_level': {'prec': [], 'rec': [], 'f1': []},
        'func_level': {'prec': [], 'rec': [], 'f1': []}
    }
    
    all_predictions = []
    total_proposals = len(proposals)
    
    for batch_start in range(0, total_proposals, batch_size):
        batch_end = min(batch_start + batch_size, total_proposals)
        batch_proposals = proposals[batch_start:batch_end]
        
        print(f"🔄 Processing batch {batch_start//batch_size + 1}/{(total_proposals + batch_size - 1)//batch_size} "
              f"(proposals {batch_start + 1}-{batch_end})")
        
        batch_predictions = []
        
        for i, proposal in enumerate(batch_proposals):
            proposal_id = proposal['id']
            proposal_idx = batch_start + i + 1
            
            print(f"🔍 Processing proposal {proposal_id}... ({proposal_idx}/{total_proposals})")
            
            # Track embedding cost
            tokens, cost = track_embedding_cost(proposal['content'])
            print(f"[COST] Proposal {proposal_id}: {tokens:,} tokens, ${cost:.6f}")
            
            # Get proposal embedding
            prop_embedding = embedding_model.get_embedding(proposal['content'])
            prop_embedding = np.array(prop_embedding).reshape(1, -1)
            
            # Compute similarities
            file_similarities = cosine_similarity(prop_embedding, file_embs)[0]
            func_similarities = cosine_similarity(prop_embedding, func_embs)[0]
            
            # Get predictions for this proposal
            prediction = get_predictions_for_proposal(
                proposal_id, file_similarities, func_similarities, 
                file_paths, func_data
            )
            
            batch_predictions.append(prediction)
            
            # Force garbage collection after each proposal
            del prop_embedding
            gc.collect()
        
        all_predictions.extend(batch_predictions)
        
        # Force garbage collection after each batch
        gc.collect()
        print(f"✅ Completed batch {batch_start//batch_size + 1}")
    
    # Evaluate all predictions
    print("📊 Evaluating all predictions...")
    evaluate_all_predictions(all_predictions, ground_truth, results, output_dir)
    
    return results

def get_predictions_for_proposal(proposal_id, file_sims, func_sims, file_paths, func_data):
    """Get top-k predictions for a single proposal"""
    prediction = {'proposal_id': proposal_id}
    
    # File-level predictions
    file_indices = np.argsort(file_sims)[::-1]
    prediction['file_paths'] = [file_paths[i] for i in file_indices[:20]]
    prediction['file_scores'] = [float(file_sims[i]) for i in file_indices[:20]]
    
    # Function-level predictions
    func_indices = np.argsort(func_sims)[::-1]
    prediction['functions'] = [func_data[i] for i in func_indices[:20]]
    prediction['func_scores'] = [float(func_sims[i]) for i in func_indices[:20]]
    
    # Directory-level from files
    dirs_from_files = ['/'.join(path.split('/')[:-1]) for path in prediction['file_paths']]
    prediction['dirs_from_files'] = list(dict.fromkeys(dirs_from_files))[:20]
    
    # Directory-level from functions
    dirs_from_funcs = ['/'.join(func[0].split('/')[:-1]) for func in prediction['functions']]
    prediction['dirs_from_funcs'] = list(dict.fromkeys(dirs_from_funcs))[:20]
    
    return prediction

def evaluate_all_predictions(predictions, ground_truth, results, output_dir):
    """Evaluate all predictions and compute metrics"""
    
    for k in results['top_k_values']:
        file_metrics = {'tp': 0, 'fp': 0, 'fn': 0}
        dir_metrics = {'tp': 0, 'fp': 0, 'fn': 0}
        func_metrics = {'tp': 0, 'fp': 0, 'fn': 0}
        
        valid_proposals = 0
        
        for pred in predictions:
            proposal_id = pred['proposal_id']
            
            if proposal_id not in ground_truth:
                continue
                
            valid_proposals += 1
            gt = ground_truth[proposal_id]
            
            # File level evaluation
            if 'file' in gt:
                gt_files = set(gt['file'])
                pred_files = set(pred['file_paths'][:k])
                
                tp = len(gt_files & pred_files)
                fp = len(pred_files - gt_files)
                fn = len(gt_files - pred_files)
                
                file_metrics['tp'] += tp
                file_metrics['fp'] += fp
                file_metrics['fn'] += fn
            
            # Directory level evaluation (from files)
            if 'directory' in gt:
                gt_dirs = set(gt['directory'])
                pred_dirs = set(pred['dirs_from_files'][:k])
                
                tp = len(gt_dirs & pred_dirs)
                fp = len(pred_dirs - gt_dirs)
                fn = len(gt_dirs - pred_dirs)
                
                dir_metrics['tp'] += tp
                dir_metrics['fp'] += fp
                dir_metrics['fn'] += fn
            
            # Function level evaluation
            if 'function' in gt:
                gt_funcs = set(tuple(f) for f in gt['function'])
                pred_funcs = set(tuple(f) for f in pred['functions'][:k])
                
                tp = len(gt_funcs & pred_funcs)
                fp = len(pred_funcs - gt_funcs)
                fn = len(gt_funcs - pred_funcs)
                
                func_metrics['tp'] += tp
                func_metrics['fp'] += fp
                func_metrics['fn'] += fn
        
        # Calculate metrics
        for level, metrics in [('file_level', file_metrics), 
                              ('dir_level', dir_metrics), 
                              ('func_level', func_metrics)]:
            
            precision = metrics['tp'] / (metrics['tp'] + metrics['fp']) if (metrics['tp'] + metrics['fp']) > 0 else 0
            recall = metrics['tp'] / (metrics['tp'] + metrics['fn']) if (metrics['tp'] + metrics['fn']) > 0 else 0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
            
            results[level]['prec'].append(precision)
            results[level]['rec'].append(recall)
            results[level]['f1'].append(f1)
    
    # Save detailed results
    results_file = output_dir / 'detailed_results.json'
    with open(results_file, 'w') as f:
        json.dump({
            'results': results,
            'predictions': predictions[:5]  # Save only first 5 for inspection
        }, f, indent=2)
    
    print(f"📝 Detailed results saved to: {results_file}")

def create_plots(results, output_dir):
    """Create performance plots"""
    def plot_metric(metric_key, metric_name, filename):
        plt.figure(figsize=(10, 6))
        top_k = results['top_k_values']
        
        plt.plot(top_k, results['file_level'][metric_key], 'o-', label='File Level', linewidth=2)
        plt.plot(top_k, results['dir_level'][metric_key], 's-', label='Directory Level', linewidth=2)
        plt.plot(top_k, results['func_level'][metric_key], '^-', label='Function Level', linewidth=2)
        
        plt.xlabel('Top-k')
        plt.ylabel(metric_name)
        plt.title(f'{metric_name} vs Top-k (Content Validated)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xlim(1, 20)
        plt.ylim(0, 1)
        
        output_path = output_dir / filename
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"📊 {metric_name} plot saved to: {output_path}")

    # Generate the three plots
    plot_metric('prec', 'Precision', 'precision.png')
    plot_metric('rec', 'Recall', 'recall.png')
    plot_metric('f1', 'F1-Score', 'f1.png')

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Memory-optimized embedding-based localization evaluation")
    parser.add_argument('--max-proposals', type=int, help='Maximum number of proposals to process for testing')
    parser.add_argument('--batch-size', type=int, default=5, help='Batch size for processing proposals (default: 5)')
    parser.add_argument('--prop-dir', type=str, help='Directory containing proposal files')
    parser.add_argument('--gt-file', type=str, help='Ground truth JSON file path')
    args = parser.parse_args()
    
    # Set default paths
    base = Path(__file__).parent.parent
    if args.prop_dir:
        prop_dir = Path(args.prop_dir)
    else:
        prop_dir = base / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals_content_validated'
    
    if args.gt_file:
        gt_file = Path(args.gt_file)
    else:
        gt_file = base / 'data' / 'ground_truth' / 'accepted_proposals_ground_truth_content_validated.json'
        
    embed_dir = base / 'embedding_based' / 'output'
    embed_dir.mkdir(parents=True, exist_ok=True)

    # Create timestamped results folder
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    result_dir = embed_dir / f"{ts}_openai_text-embedding-3-large_optimized"
    result_dir.mkdir(parents=True, exist_ok=True)
    print(f"➡️  Writing optimized results to: {result_dir}")

    # Load proposals and ground-truth
    proposals = load_proposals(prop_dir)
    ground_truth = load_ground_truth(gt_file)
    
    # Limit the number of proposals if specified
    if args.max_proposals:
        proposals = proposals[:args.max_proposals]
        print(f"🔢 Limited to {len(proposals)} proposals for testing")
    else:
        print(f"🔢 Processing all {len(proposals)} proposals")

    # Load precomputed embeddings
    embedding_based_dir = Path(__file__).parent
    openai_embed_dir = embedding_based_dir / "embeddings_cache_openai"
    
    try:
        print("📥 Loading precomputed embeddings...")
        
        # Load file embeddings
        with open(openai_embed_dir / 'file_embeddings.pkl', 'rb') as f:
            file_embs = pickle.load(f)
        file_embs = np.array(file_embs)
        
        # Load function embeddings
        with open(openai_embed_dir / 'func_embeddings.pkl', 'rb') as f:
            func_embs = pickle.load(f)
        func_embs = np.array(func_embs)
        
        # Load metadata
        with open(openai_embed_dir / 'file_paths.pkl', 'rb') as f:
            file_paths = pickle.load(f)
        
        with open(openai_embed_dir / 'func_data.pkl', 'rb') as f:
            func_data = pickle.load(f)
        
        print(f"✅ Loaded OpenAI embeddings from {openai_embed_dir}")
        print(f"   Files: {len(file_paths)}, Functions: {len(func_data)}")
        
    except FileNotFoundError as e:
        print(f"❌ Could not load precomputed embeddings: {e}")
        print("   Please run embedding_creator_for_file_and_func.py first")
        return

    # Initialize embedding model for proposals
    print("🤖 Loading embedding model: text-embedding-3-large")
    embedding_model = create_openai_embedding_model('text-embedding-3-large')
    
    # Process proposals in batches
    results = process_proposals_in_batches(
        proposals, ground_truth, file_embs, func_embs, 
        file_paths, func_data, embedding_model, 
        result_dir, batch_size=args.batch_size
    )
    
    # Create plots
    create_plots(results, result_dir)
    
    # Save cost report
    save_embedding_cost_report(result_dir)
    
    print("🎉 Memory-optimized evaluation completed!")

if __name__ == '__main__':
    main()
