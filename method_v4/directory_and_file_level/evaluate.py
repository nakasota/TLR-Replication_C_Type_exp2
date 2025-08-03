import json
from pathlib import Path
from collections import defaultdict
import re
import os
from datetime import datetime

def load_llm_outputs(llm_output_path):
    """Load LLM outputs and extract found_files for each proposal."""
    with open(llm_output_path, 'r') as f:
        data = json.load(f)
    outputs = {}
    for k, v in data.items():
        # Skip non-proposal keys (like "selected_directory_level_output")
        if k.startswith('selected_'):
            continue
        # v should be a dict with found_files
        if isinstance(v, dict):
            files = set(v.get('found_files', []))
        elif isinstance(v, str):
            # Try to parse string as JSON (fallback)
            v = v.strip()
            if v.startswith('```json'):
                v = v[len('```json'):].strip()
            if v.startswith('```'):
                v = v[len('```'):].strip()
            if v.endswith('```'):
                v = v[:-3].strip()
            try:
                parsed = json.loads(v)
                files = set(parsed.get('found_files', []))
            except Exception:
                files = set()
        else:
            files = set()
        outputs[k.replace('.md','')] = files
    return outputs

def load_ground_truth_func_analysis(gt_path):
    """Load ground truth data and extract files for each proposal."""
    with open(gt_path, 'r') as f:
        data = json.load(f)
    gt = {}
    for entry in data:
        if not isinstance(entry, dict):
            print(f"Skipping non-dict entry: {entry}")
            continue
        proposal_id = entry.get('proposal_id')
        if not proposal_id:
            print(f"Skipping entry missing 'proposal_id': {entry}")
            continue
        files = set(entry.get('files', []))
        gt[proposal_id] = {'files': files}
    return gt

def extract_directories_from_files(files):
    """Extract unique directories from file paths."""
    directories = set()
    for file_path in files:
        # Get the directory path by removing the filename
        dir_path = str(Path(file_path).parent)
        if dir_path != '.' and dir_path != '':
            directories.add(dir_path)
    return directories

def compute_metrics(pred, gt):
    """Compute precision, recall, and F1 score."""
    tp = len(pred & gt)
    fp = len(pred - gt)
    fn = len(gt - pred)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return precision, recall, f1, tp, fp, fn

def select_output_dir():
    """Select output directory containing llm_outputs.json."""
    output_root = Path(__file__).parent / 'output'
    # Filter directories that contain llm_outputs.json
    valid_output_dirs = []
    for d in output_root.iterdir():
        if d.is_dir() and (d / 'llm_outputs.json').exists():
            valid_output_dirs.append(d)
    
    valid_output_dirs = sorted(valid_output_dirs, reverse=True)
    if not valid_output_dirs:
        raise RuntimeError('No valid output directory found in method_v3/directory_and_file_level/output/. All directories are empty or missing llm_outputs.json')
    
    print('Available output directories (with llm_outputs.json):')
    for i, d in enumerate(valid_output_dirs):
        print(f"[{i}] {d.name}")
    selected_idx = input(f"Select output index [0-{len(valid_output_dirs)-1}]: ")
    try:
        selected_idx = int(selected_idx)
        if not (0 <= selected_idx < len(valid_output_dirs)):
            raise ValueError
    except Exception:
        raise RuntimeError('Invalid selection.')
    return valid_output_dirs[selected_idx]

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', type=str, default=None, help='Output directory')
    args = parser.parse_args()

    # Select output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = select_output_dir()
    llm_output_path = output_dir / 'llm_outputs.json'

    # Ground truth
    gt_path = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals_ground_truth.json'
    
    # Load outputs and ground truth
    llm_outputs = load_llm_outputs(llm_output_path)
    gt = load_ground_truth_func_analysis(gt_path)

    # File-level evaluation
    all_file_prec, all_file_rec, all_file_f1 = [], [], []
    file_results = {}
    
    # Directory-level evaluation
    all_dir_prec, all_dir_rec, all_dir_f1 = [], [], []
    dir_results = {}
    
    for proposal_id, pred_files in llm_outputs.items():
        gt_files = gt.get(proposal_id, {}).get('files', set())
        
        # File-level metrics
        file_precision, file_recall, file_f1, file_tp, file_fp, file_fn = compute_metrics(pred_files, gt_files)
        file_results[proposal_id] = {
            'precision': file_precision,
            'recall': file_recall,
            'f1': file_f1,
            'tp': file_tp,
            'fp': file_fp,
            'fn': file_fn,
            'predicted': list(pred_files),
            'ground_truth': list(gt_files)
        }
        all_file_prec.append(file_precision)
        all_file_rec.append(file_recall)
        all_file_f1.append(file_f1)
        
        # Directory-level metrics
        pred_dirs = extract_directories_from_files(pred_files)
        gt_dirs = extract_directories_from_files(gt_files)
        
        dir_precision, dir_recall, dir_f1, dir_tp, dir_fp, dir_fn = compute_metrics(pred_dirs, gt_dirs)
        dir_results[proposal_id] = {
            'precision': dir_precision,
            'recall': dir_recall,
            'f1': dir_f1,
            'tp': dir_tp,
            'fp': dir_fp,
            'fn': dir_fn,
            'predicted': list(pred_dirs),
            'ground_truth': list(gt_dirs)
        }
        all_dir_prec.append(dir_precision)
        all_dir_rec.append(dir_recall)
        all_dir_f1.append(dir_f1)
    
    # Calculate macro metrics for files
    macro_file_precision = sum(all_file_prec) / len(all_file_prec) if all_file_prec else 0.0
    macro_file_recall = sum(all_file_rec) / len(all_file_rec) if all_file_rec else 0.0
    macro_file_f1 = sum(all_file_f1) / len(all_file_f1) if all_file_f1 else 0.0

    # Calculate macro metrics for directories
    macro_dir_precision = sum(all_dir_prec) / len(all_dir_prec) if all_dir_prec else 0.0
    macro_dir_recall = sum(all_dir_rec) / len(all_dir_rec) if all_dir_rec else 0.0
    macro_dir_f1 = sum(all_dir_f1) / len(all_dir_f1) if all_dir_f1 else 0.0

    # Print results
    print(f"[Directory Level] Macro Precision: {macro_dir_precision:.3f}")
    print(f"[Directory Level] Macro Recall: {macro_dir_recall:.3f}")
    print(f"[Directory Level] Macro F1: {macro_dir_f1:.3f}")
    
    print(f"[File Level] Macro Precision: {macro_file_precision:.3f}")
    print(f"[File Level] Macro Recall: {macro_file_recall:.3f}")
    print(f"[File Level] Macro F1: {macro_file_f1:.3f}")

    # Save results
    all_results = {
        'directory_level': {
            'macro_precision': macro_dir_precision, 
            'macro_recall': macro_dir_recall, 
            'macro_f1': macro_dir_f1, 
            'per_proposal': dir_results
        },
        'file_level': {
            'macro_precision': macro_file_precision, 
            'macro_recall': macro_file_recall, 
            'macro_f1': macro_file_f1, 
            'per_proposal': file_results
        }
    }
        
    with open(output_dir / 'evaluation_results.json', 'w') as f:
        json.dump(all_results, f, indent=2)

    # Generate comprehensive markdown summary
    proposals_with_dir_links = sum(1 for res in dir_results.values() if res['precision'] > 0.0)
    proposals_with_file_links = sum(1 for res in file_results.values() if res['precision'] > 0.0)
    
    md_lines = []
    md_lines.append(f"# LLM Directory and File Level Evaluation Summary\n")
    
    # Add macro metrics for both levels
    md_lines.append(f"## Directory Level Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {len(llm_outputs)}")
    md_lines.append(f"- **Number of Proposals with at least one correct directory (precision > 0)**: {proposals_with_dir_links}")
    md_lines.append(f"- **Macro Precision**: {macro_dir_precision:.3f}")
    md_lines.append(f"- **Macro Recall**: {macro_dir_recall:.3f}")
    md_lines.append(f"- **Macro F1**: {macro_dir_f1:.3f}\n")
    
    md_lines.append(f"## File Level Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {len(llm_outputs)}")
    md_lines.append(f"- **Number of Proposals with at least one correct file (precision > 0)**: {proposals_with_file_links}")
    md_lines.append(f"- **Macro Precision**: {macro_file_precision:.3f}")
    md_lines.append(f"- **Macro Recall**: {macro_file_recall:.3f}")
    md_lines.append(f"- **Macro F1**: {macro_file_f1:.3f}\n")
    
    # Add detailed proposal breakdowns
    for proposal_id in file_results:
        file_res = file_results[proposal_id]
        dir_res = dir_results[proposal_id]
        
        md_lines.append(f"\n### 📊 **Proposal #{proposal_id}**\n")
        
        # Directory level results
        md_lines.append(f"#### Directory Level Results\n")
        dir_found = dir_res['tp']
        dir_total = dir_res['tp'] + dir_res['fn']
        md_lines.append(f"| **Precision** | **Recall** | **F1-Score** | **Found/Total** |")
        md_lines.append(f"|-----------|--------|----------|-------------|")
        md_lines.append(f"| {dir_res['precision']*100:.1f}% | {dir_res['recall']*100:.1f}% | {dir_res['f1']*100:.1f}% | {dir_found}/{dir_total} |")
        
        md_lines.append(f"\n##### Ground Truth vs Predicted Directories\n")
        gt_dirs = set(dir_res['ground_truth'])
        pred_dirs = set(dir_res['predicted'])
        md_lines.append(f"**Ground Truth Directories ({len(gt_dirs)}):**")
        for d in sorted(gt_dirs):
            md_lines.append(f"- `{d}`")
        md_lines.append("")
        md_lines.append(f"**Predicted Directories ({len(pred_dirs)}):**")
        for d in sorted(pred_dirs):
            mark = "✅" if d in gt_dirs else "❌"
            md_lines.append(f"- {mark} `{d}`")
        md_lines.append("")
        
        # File level results
        md_lines.append(f"#### File Level Results\n")
        file_found = file_res['tp']
        file_total = file_res['tp'] + file_res['fn']
        md_lines.append(f"| **Precision** | **Recall** | **F1-Score** | **Found/Total** |")
        md_lines.append(f"|-----------|--------|----------|-------------|")
        md_lines.append(f"| {file_res['precision']*100:.1f}% | {file_res['recall']*100:.1f}% | {file_res['f1']*100:.1f}% | {file_found}/{file_total} |")
        
        md_lines.append(f"\n##### Ground Truth vs Predicted Files\n")
        gt_files = set(file_res['ground_truth'])
        pred_files = set(file_res['predicted'])
        md_lines.append(f"**Ground Truth Files ({len(gt_files)}):**")
        for f in sorted(gt_files):
            md_lines.append(f"- `{f}`")
        md_lines.append("")
        md_lines.append(f"**Predicted Files ({len(pred_files)}):**")
        for f in sorted(pred_files):
            mark = "✅" if f in gt_files else "❌"
            md_lines.append(f"- {mark} `{f}`")
        md_lines.append("")
    
    # Write markdown file
    md_content = '\n'.join(md_lines)
    with open(output_dir / 'evaluation_summary.md', 'w') as f:
        f.write(md_content)

    # Write summary JSON file
    summary = {
        "directory_level": {
            "macro_precision": macro_dir_precision,
            "macro_recall": macro_dir_recall,
            "macro_f1": macro_dir_f1,
            "num_processed_proposals": len(llm_outputs)
        },
        "file_level": {
            "macro_precision": macro_file_precision,
            "macro_recall": macro_file_recall,
            "macro_f1": macro_file_f1,
            "num_processed_proposals": len(llm_outputs)
        }
    }
    with open(output_dir / 'summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\nEvaluation complete! Results saved to:")
    print(f"  - {output_dir / 'evaluation_results.json'}")
    print(f"  - {output_dir / 'evaluation_summary.md'}")
    print(f"  - {output_dir / 'summary.json'}")

if __name__ == "__main__":
    main()
