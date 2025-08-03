import json
from pathlib import Path
from collections import defaultdict
import os
from datetime import datetime
from datetime import datetime

def load_llm_outputs(llm_output_path):
    with open(llm_output_path, 'r') as f:
        data = json.load(f)
    # Remove metadata key if present and normalize proposal IDs (remove .md extension)
    normalized_data = {}
    for k, v in data.items():
        if not k.startswith('selected_'):
            # Remove .md extension if present to match ground truth format
            proposal_id = k.replace('.md', '') if k.endswith('.md') else k
            normalized_data[proposal_id] = v
    return normalized_data

def load_directory_level_outputs(dir_output_path):
    """Load directory-level outputs"""
    with open(dir_output_path, 'r') as f:
        data = json.load(f)
    outputs = {}
    for k, v in data.items():
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
        dirs = set(parsed.get('found_directories', []))
        outputs[k.replace('.md','')] = dirs
    return outputs

def load_file_level_outputs(file_output_path):
    """Load file-level outputs"""
    with open(file_output_path, 'r') as f:
        data = json.load(f)
    outputs = {}
    for k, v in data.items():
        if isinstance(v, dict) and 'found_files' in v:
            files = set(v['found_files'])
            outputs[k.replace('.md','')] = files
    return outputs

def load_ground_truth_func_analysis(gt_path):
    with open(gt_path, 'r') as f:
        data = json.load(f)
    gt = defaultdict(dict)
    for entry in data:
        if not isinstance(entry, dict):
            continue
        proposal_id = str(entry.get('proposal_id'))  # Ensure string type
        if not proposal_id:
            continue
        
        # Parse detected_functions to create file->functions mapping
        detected_functions = entry.get('detected_functions', [])
        file_funcs = defaultdict(list)
        for func_info in detected_functions:
            if isinstance(func_info, dict):
                func_name = func_info.get('function_name')
                file_path = func_info.get('file_path')
                if func_name and file_path:
                    file_funcs[file_path].append(func_name)
        
        gt[proposal_id] = dict(file_funcs)
    return gt

def load_ground_truth_data(gt_path):
    """Load ground truth for all levels"""
    with open(gt_path, 'r') as f:
        data = json.load(f)
    
    directories = defaultdict(set)
    files = defaultdict(set)
    functions = defaultdict(dict)
    
    for entry in data:
        if not isinstance(entry, dict):
            continue
        proposal_id = str(entry.get('proposal_id'))
        if not proposal_id:
            continue
            
        # Extract directories and files
        entry_files = entry.get('files', [])
        for file_path in entry_files:
            files[proposal_id].add(file_path)
            directory = os.path.dirname(file_path)
            if directory:
                directories[proposal_id].add(directory)
        
        # Extract functions
        detected_functions = entry.get('detected_functions', [])
        file_funcs = defaultdict(list)
        for func_info in detected_functions:
            if isinstance(func_info, dict):
                func_name = func_info.get('function_name')
                file_path = func_info.get('file_path')
                if func_name and file_path:
                    file_funcs[file_path].append(func_name)
        functions[proposal_id] = dict(file_funcs)
    
    return directories, files, functions

def select_function_level_output_dir():
    output_root = Path(__file__).parent / 'output'
    if not output_root.exists():
        raise RuntimeError(f'No output directory found at {output_root}. Please run function-level main.py first to generate outputs.')
    
    output_dirs = sorted([d for d in output_root.iterdir() if d.is_dir()], reverse=True)
    if not output_dirs:
        raise RuntimeError('No output directories found in method_v2/function_level/output/. Please run function-level main.py first to generate outputs.')
    
    print('Available function-level output directories:')
    for i, d in enumerate(output_dirs):
        print(f"[{i}] {d.name}")
    selected_idx = input(f"Select function-level output index [0-{len(output_dirs)-1}]: ")
    try:
        selected_idx = int(selected_idx)
        if not (0 <= selected_idx < len(output_dirs)):
            raise ValueError
    except Exception:
        raise RuntimeError('Invalid selection.')
    return output_dirs[selected_idx]

def parse_llm_function_outputs(llm_output_path):
    with open(llm_output_path, 'r') as f:
        data = json.load(f)
    outputs = {}
    for k, v in data.items():
        if k.startswith('selected_'):
            continue
        proposal_id = k.replace('.md', '')
        file_func_map = {}
        if isinstance(v, dict):
            for file_path, func_list in v.items():
                file_func_map[file_path] = set(func_list)
        outputs[proposal_id] = file_func_map
    return outputs

def parse_ground_truth_functions(gt_path):
    with open(gt_path, 'r') as f:
        data = json.load(f)
    gt = {}
    for entry in data:
        proposal_id = str(entry.get('proposal_id'))
        file_func_map = {}
        for func_info in entry.get('detected_functions', []):
            file_path = func_info.get('file_path')
            func_name = func_info.get('function_name')
            if file_path and func_name:
                if file_path not in file_func_map:
                    file_func_map[file_path] = set()
                file_func_map[file_path].add(func_name)
        gt[proposal_id] = file_func_map
    return gt

def evaluate_function_level(llm_outputs, gt_outputs):
    all_prec, all_rec, all_f1 = [], [], []
    results = {}
    all_proposals = set(gt_outputs.keys())
    for proposal_id in all_proposals:
        pred_files = llm_outputs.get(proposal_id, {})
        gt_files = gt_outputs.get(proposal_id, {})
        all_files = set(pred_files.keys()) | set(gt_files.keys())
        tp = fp = fn = 0
        pred_serializable = {}
        gt_serializable = {}
        for file_path in all_files:
            pred_funcs = set(pred_files.get(file_path, set()))
            gt_funcs = set(gt_files.get(file_path, set()))
            tp += len(pred_funcs & gt_funcs)
            fp += len(pred_funcs - gt_funcs)
            fn += len(gt_funcs - pred_funcs)
            pred_serializable[file_path] = sorted(list(pred_funcs))
            gt_serializable[file_path] = sorted(list(gt_funcs))
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
        results[proposal_id] = {
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'tp': tp,
            'fp': fp,
            'fn': fn,
            'predicted': pred_serializable,
            'ground_truth': gt_serializable
        }
        all_prec.append(precision)
        all_rec.append(recall)
        all_f1.append(f1)
    macro_precision = sum(all_prec) / len(all_prec) if all_prec else 0.0
    macro_recall = sum(all_rec) / len(all_rec) if all_rec else 0.0
    macro_f1 = sum(all_f1) / len(all_f1) if all_f1 else 0.0
    return {
        'macro_precision': macro_precision,
        'macro_recall': macro_recall,
        'macro_f1': macro_f1,
        'per_proposal': results,
        'num_processed_proposals': len(all_proposals)
    }

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--function_level_output_dir', type=str, default=None, help='Function-level output directory')
    args = parser.parse_args()

    if args.function_level_output_dir:
        function_level_output_dir = Path(args.function_level_output_dir)
    else:
        function_level_output_dir = select_function_level_output_dir()
    function_level_llm_output_path = function_level_output_dir / 'llm_outputs.json'

    # Parse outputs
    llm_func_outputs = parse_llm_function_outputs(function_level_llm_output_path)
    gt_func_outputs = parse_ground_truth_functions(Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals_ground_truth.json')

    # Evaluate
    function_eval = evaluate_function_level(llm_func_outputs, gt_func_outputs)

    print(f"[Function Level] Macro Precision: {function_eval['macro_precision']:.3f}")
    print(f"[Function Level] Macro Recall: {function_eval['macro_recall']:.3f}")
    print(f"[Function Level] Macro F1: {function_eval['macro_f1']:.3f}")
    print(f"Number of Processed Proposals: {function_eval['num_processed_proposals']}")

    # Save results
    output_dir = function_level_output_dir
    with open(output_dir / 'evaluation_results.json', 'w') as f:
        json.dump({'function_level': function_eval}, f, indent=2)

    # Markdown summary
    md_lines = []
    md_lines.append(f"# LLM Directory, File & Function-Level Evaluation Summary\n")
    
    # --- NEW: Append directory and file-level results ---
    # Get selected file-level output from function-level llm_outputs.json
    selected_file_level = None
    try:
        with open(function_level_llm_output_path, 'r') as f:
            func_data = json.load(f)
        selected_file_level = func_data.get("selected_file_level_output", None)
        if selected_file_level:
            print(f"Found selected file-level output: {selected_file_level}")
    except Exception as e:
        print(f"Warning: Could not read selected file-level output: {e}")
    
    # Load both directory and file-level results from the directory_and_file_level output directory
    dir_eval = {}
    file_eval = {}
    if selected_file_level:
        file_level_output_dir = Path(__file__).parent.parent / 'directory_and_file_level' / 'output' / selected_file_level
        file_level_eval_path = file_level_output_dir / 'evaluation_results.json'
        if file_level_eval_path.exists():
            try:
                with open(file_level_eval_path, 'r') as f:
                    eval_data = json.load(f)
                dir_eval = eval_data.get('directory_level', {})
                file_eval = eval_data.get('file_level', {})
                print(f"Loaded directory and file level results from {file_level_eval_path}")
            except Exception as e:
                print(f"Warning: Could not load directory/file level results: {e}")
        else:
            print(f"Warning: Directory/File level evaluation results not found at {file_level_eval_path}")
            print("Please run method_v3/directory_and_file_level/evaluate.py first to generate these results.")
    
    # Directory-level macro metrics
    md_lines.append(f"## Directory-Level Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {function_eval['num_processed_proposals']}")
    if dir_eval:
        proposals_with_links = sum(1 for res in dir_eval.get('per_proposal', {}).values() if res['precision'] > 0.0)
        md_lines.append(f"- **Number of Proposals with at least one correct link (precision > 0)**: {proposals_with_links}")
    md_lines.append(f"- **Macro Precision**: {dir_eval.get('macro_precision', 0):.3f}")
    md_lines.append(f"- **Macro Recall**: {dir_eval.get('macro_recall', 0):.3f}")
    md_lines.append(f"- **Macro F1**: {dir_eval.get('macro_f1', 0):.3f}\n")
    
    # File-level macro metrics
    md_lines.append(f"## File-Level Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {function_eval['num_processed_proposals']}")
    if file_eval:
        proposals_with_links = sum(1 for res in file_eval.get('per_proposal', {}).values() if res['precision'] > 0.0)
        md_lines.append(f"- **Number of Proposals with at least one correct link (precision > 0)**: {proposals_with_links}")
    md_lines.append(f"- **Macro Precision**: {file_eval.get('macro_precision', 0):.3f}")
    md_lines.append(f"- **Macro Recall**: {file_eval.get('macro_recall', 0):.3f}")
    md_lines.append(f"- **Macro F1**: {file_eval.get('macro_f1', 0):.3f}\n")
    
    # Function-level macro metrics
    md_lines.append(f"## Function-Level Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {function_eval['num_processed_proposals']}")
    proposals_with_links = sum(1 for res in function_eval['per_proposal'].values() if res['precision'] > 0.0)
    md_lines.append(f"- **Number of Proposals with at least one correct link (precision > 0)**: {proposals_with_links}")
    md_lines.append(f"- **Macro Precision**: {function_eval['macro_precision']:.3f}")
    md_lines.append(f"- **Macro Recall**: {function_eval['macro_recall']:.3f}")
    md_lines.append(f"- **Macro F1**: {function_eval['macro_f1']:.3f}\n")
    
    # Detailed per-proposal results for all levels
    for pid, res in function_eval['per_proposal'].items():
        md_lines.append(f"\n### 📊 **Proposal #{pid} (Function Level)**\n")
        found = res['tp']
        total = res['tp'] + res['fn']
        md_lines.append(f"| **Precision** | **Recall** | **F1-Score** | **Found/Total** |")
        md_lines.append(f"|-----------|--------|----------|-------------|")
        md_lines.append(f"| {res['precision']*100:.1f}% | {res['recall']*100:.1f}% | {res['f1']*100:.1f}% | {found}/{total} |")
        md_lines.append(f"\n##### Ground Truth vs Predicted Functions per File\n")
        gt_files = res['ground_truth'] if isinstance(res['ground_truth'], dict) else {}
        pred_files = res['predicted'] if isinstance(res['predicted'], dict) else {}
        all_files = set(gt_files.keys()) | set(pred_files.keys())
        for file_path in sorted(all_files):
            gt_funcs = set(gt_files.get(file_path, []))
            pred_funcs = set(pred_files.get(file_path, []))
            md_lines.append(f"- **File:** `{file_path}`")
            md_lines.append(f"    - Ground Truth Functions ({len(gt_funcs)}):")
            for func in sorted(gt_funcs):
                md_lines.append(f"        - `{func}`")
            md_lines.append(f"    - Predicted Functions ({len(pred_funcs)}):")
            for func in sorted(pred_funcs):
                mark = "✅" if func in gt_funcs else "❌"
                md_lines.append(f"        - {mark} `{func}`")
            md_lines.append("")
    
    # Directory-level detailed results
    if dir_eval:
        per_proposal = dir_eval.get('per_proposal', {})
        for pid, res in per_proposal.items():
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
    
    # File-level detailed results
    if file_eval:
        per_proposal = file_eval.get('per_proposal', {})
        for pid, res in per_proposal.items():
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

if __name__ == '__main__':
    main()
