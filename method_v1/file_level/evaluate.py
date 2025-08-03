import json
from pathlib import Path
from collections import defaultdict
import re
import os
from datetime import datetime

def load_llm_outputs(llm_output_path):
    with open(llm_output_path, 'r') as f:
        data = json.load(f)
    outputs = {}
    for k, v in data.items():
        # v can be a dict (file-level) or a string (directory-level)
        if isinstance(v, str):
            v = v.strip()
            if v.startswith('```json'):
                v = v[len('```json'):].strip()
            if v.startswith('```'):
                v = v[len('```'):].strip()
            if v.endswith('```'):
                v = v[:-3].strip()
            try:
                parsed = json.loads(v)
            except Exception:
                parsed = {}
        elif isinstance(v, dict):
            # If this is a file-level output, skip it for directory-level eval
            if 'found_files' in v:
                continue
            parsed = v
        else:
            parsed = {}
        dirs = set(parsed.get('found_directories', []))
        outputs[k.replace('.md','')] = dirs
    return outputs

def load_llm_file_outputs(llm_output_path):
    with open(llm_output_path, 'r') as f:
        data = json.load(f)
    outputs = {}
    for k, v in data.items():
        # v can be a dict or a string
        if isinstance(v, str):
            v = v.strip()
            if v.startswith('```json'):
                v = v[len('```json'):].strip()
            if v.startswith('```'):
                v = v[len('```'):].strip()
            if v.endswith('```'):
                v = v[:-3].strip()
            try:
                parsed = json.loads(v)
            except Exception:
                parsed = {}
        elif isinstance(v, dict):
            parsed = v
        else:
            parsed = {}
        files = set(parsed.get('found_files', []))
        outputs[k.replace('.md','')] = files
    return outputs

def load_ground_truth_func_analysis(gt_path):
    with open(gt_path, 'r') as f:
        data = json.load(f)
    gt = defaultdict(set)
    for entry in data:
        if not isinstance(entry, dict):
            print(f"Skipping non-dict entry: {entry}")
            continue
        proposal_id = entry.get('proposal_id')
        if not proposal_id:
            print(f"Skipping entry missing 'proposal_id': {entry}")
            continue
        dirs = set()
        files = set(entry.get('files', []))
        for file_path in files:
            dir_path = '/'.join(file_path.split('/')[:-1])
            if dir_path:
                dirs.add(dir_path)
        gt[proposal_id] = {'dirs': dirs, 'files': files}
    return gt

def compute_metrics(pred, gt):
    tp = len(pred & gt)
    fp = len(pred - gt)
    fn = len(gt - pred)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return precision, recall, f1, tp, fp, fn

def get_selected_directory_level_output_from_file_level(file_level_llm_output_path):
    try:
        with open(file_level_llm_output_path, 'r') as f:
            data = json.load(f)
        return data.get("selected_directory_level_output", None)
    except Exception:
        return None

def select_file_level_output_dir():
    output_root = Path(__file__).parent / 'output'
    output_dirs = sorted([d for d in output_root.iterdir() if d.is_dir()], reverse=True)
    if not output_dirs:
        raise RuntimeError('No output directory found in method_v1/file_level/output/.')
    print('Available file-level output directories:')
    for i, d in enumerate(output_dirs):
        print(f"[{i}] {d.name}")
    selected_idx = input(f"Select file-level output index [0-{len(output_dirs)-1}]: ")
    try:
        selected_idx = int(selected_idx)
        if not (0 <= selected_idx < len(output_dirs)):
            raise ValueError
    except Exception:
        raise RuntimeError('Invalid selection.')
    return output_dirs[selected_idx]

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory_level_output_dir', type=str, default=None, help='Directory-level output directory')
    parser.add_argument('--file_level_output_dir', type=str, default=None, help='File-level output directory')
    args = parser.parse_args()

    # File-level
    if args.file_level_output_dir:
        file_level_output_dir = Path(args.file_level_output_dir)
    else:
        file_level_output_dir = select_file_level_output_dir()
    file_level_llm_output_path = file_level_output_dir / 'llm_outputs.json'

    # Directory-level: use selected from file-level output if present and not overridden
    selected_dir_level = get_selected_directory_level_output_from_file_level(file_level_llm_output_path)
    if args.directory_level_output_dir:
        directory_level_output_dir = Path(args.directory_level_output_dir)
    elif selected_dir_level:
        output_root = Path(__file__).parent.parent / 'directory_level' / 'output'
        directory_level_output_dir = output_root / selected_dir_level
    else:
        output_root = Path(__file__).parent.parent / 'directory_level' / 'output'
        output_dirs = sorted([d for d in output_root.iterdir() if d.is_dir()], reverse=True)
        if not output_dirs:
            raise RuntimeError('No output directory found in method_v1/directory_level/output/.')
        directory_level_output_dir = output_dirs[0]
    directory_level_llm_output_path = directory_level_output_dir / 'llm_outputs.json'

    # Ground truth
    gt_path = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals_ground_truth.json'
    # Load file-level outputs first so we can filter directory-level outputs
    file_llm_outputs = load_llm_file_outputs(file_level_llm_output_path)
    dir_llm_outputs = load_llm_outputs(directory_level_llm_output_path)
    # Only evaluate proposals present in both outputs
    common_proposals = set(file_llm_outputs.keys()) & set(dir_llm_outputs.keys())
    file_llm_outputs = {k: v for k, v in file_llm_outputs.items() if k in common_proposals}
    dir_llm_outputs = {k: v for k, v in dir_llm_outputs.items() if k in common_proposals}
    gt = load_ground_truth_func_analysis(gt_path)

    # Directory-level evaluation
    all_prec, all_rec, all_f1 = [], [], []
    dir_results = {}
    for proposal_id, pred_dirs in dir_llm_outputs.items():
        gt_dirs = gt.get(proposal_id, {}).get('dirs', set())
        precision, recall, f1, tp, fp, fn = compute_metrics(pred_dirs, gt_dirs)
        dir_results[proposal_id] = {
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'tp': tp,
            'fp': fp,
            'fn': fn,
            'predicted': list(pred_dirs),
            'ground_truth': list(gt_dirs)
        }
        all_prec.append(precision)
        all_rec.append(recall)
        all_f1.append(f1)
    macro_precision = sum(all_prec) / len(all_prec) if all_prec else 0.0
    macro_recall = sum(all_rec) / len(all_rec) if all_rec else 0.0
    macro_f1 = sum(all_f1) / len(all_f1) if all_f1 else 0.0

    # File-level evaluation
    all_prec_f, all_rec_f, all_f1_f = [], [], []
    file_results = {}
    for proposal_id, pred_files in file_llm_outputs.items():
        gt_files = gt.get(proposal_id, {}).get('files', set())
        precision, recall, f1, tp, fp, fn = compute_metrics(pred_files, gt_files)
        file_results[proposal_id] = {
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'tp': tp,
            'fp': fp,
            'fn': fn,
            'predicted': list(pred_files),
            'ground_truth': list(gt_files)
        }
        all_prec_f.append(precision)
        all_rec_f.append(recall)
        all_f1_f.append(f1)
    macro_precision_f = sum(all_prec_f) / len(all_prec_f) if all_prec_f else 0.0
    macro_recall_f = sum(all_rec_f) / len(all_rec_f) if all_rec_f else 0.0
    macro_f1_f = sum(all_f1_f) / len(all_f1_f) if all_f1_f else 0.0

    print(f"[Directory Level] Macro Precision: {macro_precision:.3f}")
    print(f"[Directory Level] Macro Recall: {macro_recall:.3f}")
    print(f"[Directory Level] Macro F1: {macro_f1:.3f}")
    print(f"[File Level] Macro Precision: {macro_precision_f:.3f}")
    print(f"[File Level] Macro Recall: {macro_recall_f:.3f}")
    print(f"[File Level] Macro F1: {macro_f1_f:.3f}")

    # Save results
    output_dir = file_level_output_dir
    with open(output_dir / 'evaluation_results.json', 'w') as f:
        json.dump({
            'directory_level': {'macro_precision': macro_precision, 'macro_recall': macro_recall, 'macro_f1': macro_f1, 'per_proposal': dir_results},
            'file_level': {'macro_precision': macro_precision_f, 'macro_recall': macro_recall_f, 'macro_f1': macro_f1_f, 'per_proposal': file_results}
        }, f, indent=2)

    # Markdown summary
    proposals_with_links = sum(1 for res in dir_results.values() if res['precision'] > 0.0)
    proposals_with_links_f = sum(1 for res in file_results.values() if res['precision'] > 0.0)
    md_lines = []
    md_lines.append(f"# LLM Directory & File-Level Evaluation Summary\n")
    md_lines.append(f"## Directory-Level Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {len(dir_llm_outputs)}")
    md_lines.append(f"- **Number of Proposals with at least one correct link (precision > 0)**: {proposals_with_links}")
    md_lines.append(f"- **Macro Precision**: {macro_precision:.3f}")
    md_lines.append(f"- **Macro Recall**: {macro_recall:.3f}")
    md_lines.append(f"- **Macro F1**: {macro_f1:.3f}\n")
    md_lines.append(f"## File-Level Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {len(file_llm_outputs)}")
    md_lines.append(f"- **Number of Proposals with at least one correct link (precision > 0)**: {proposals_with_links_f}")
    md_lines.append(f"- **Macro Precision**: {macro_precision_f:.3f}")
    md_lines.append(f"- **Macro Recall**: {macro_recall_f:.3f}")
    md_lines.append(f"- **Macro F1**: {macro_f1_f:.3f}\n")
    for pid, res in dir_results.items():
        md_lines.append(f"\n### 📊 **Proposal #{pid} (Directory Level)**\n")
        found = res['tp']
        total = res['tp'] + res['fn']
        md_lines.append(f"| **Precision** | **Recall** | **F1-Score** | **Found/Total** |")
        md_lines.append(f"|-----------|--------|----------|-------------|")
        md_lines.append(f"| {res['precision']*100:.1f}% | {res['recall']*100:.1f}% | {res['f1']*100:.1f}% | {found}/{total} |")
        md_lines.append(f"\n##### Ground Truth vs Predicted Directories\n")
        gt_dirs = set(res['ground_truth'])
        pred_dirs = set(res['predicted'])
        md_lines.append(f"**Ground Truth Directories ({len(gt_dirs)}):**")
        for d in sorted(gt_dirs):
            md_lines.append(f"- `{d}`")
        md_lines.append("")
        md_lines.append(f"**Predicted Directories ({len(pred_dirs)}):**")
        for d in sorted(pred_dirs):
            mark = "✅" if d in gt_dirs else "❌"
            md_lines.append(f"- {mark} `{d}`")
        md_lines.append("")
    for pid, res in file_results.items():
        md_lines.append(f"\n### 📊 **Proposal #{pid} (File Level)**\n")
        found = res['tp']
        total = res['tp'] + res['fn']
        md_lines.append(f"| **Precision** | **Recall** | **F1-Score** | **Found/Total** |")
        md_lines.append(f"|-----------|--------|----------|-------------|")
        md_lines.append(f"| {res['precision']*100:.1f}% | {res['recall']*100:.1f}% | {res['f1']*100:.1f}% | {found}/{total} |")
        md_lines.append(f"\n##### Ground Truth vs Predicted Files\n")
        gt_files = set(res['ground_truth'])
        pred_files = set(res['predicted'])
        md_lines.append(f"**Ground Truth Files ({len(gt_files)}):**")
        for d in sorted(gt_files):
            md_lines.append(f"- `{d}`")
        md_lines.append("")
        md_lines.append(f"**Predicted Files ({len(pred_files)}):**")
        for d in sorted(pred_files):
            mark = "✅" if d in gt_files else "❌"
            md_lines.append(f"- {mark} `{d}`")
        md_lines.append("")
    md_content = '\n'.join(md_lines)
    with open(output_dir / 'evaluation_summary.md', 'w') as f:
        f.write(md_content)

    # Write summary JSON file
    summary = {
        "directory_level": {
            "macro_precision": macro_precision,
            "macro_recall": macro_recall,
            "macro_f1": macro_f1,
            "num_processed_proposals": len(dir_llm_outputs)
        },
        "file_level": {
            "macro_precision": macro_precision_f,
            "macro_recall": macro_recall_f,
            "macro_f1": macro_f1_f,
            "num_processed_proposals": len(file_llm_outputs)
        }
    }
    with open(output_dir / 'evaluation_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

if __name__ == '__main__':
    main()
