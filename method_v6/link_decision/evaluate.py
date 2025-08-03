#!/usr/bin/env python3

import json
import sys
from pathlib import Path

def load_ground_truth():
    """Load the ground truth from evaluation results"""
    eval_file = Path(__file__).parent.parent.parent / 'evaluation_results.json'
    if not eval_file.exists():
        print(f"Ground truth file not found: {eval_file}")
        return None
    
    with open(eval_file, 'r') as f:
        data = json.load(f)
    
    return data.get('function_level', {}).get('per_proposal', {})

def evaluate_link_decision(llm_output_file, ground_truth):
    """
    Evaluate the link decision results against ground truth
    
    FIXED: This evaluation now correctly includes ALL ground truth functions
    in the recall calculation, not just those that were considered by link decision.
    Ground truth functions missing from link decision are counted as false negatives.
    """
    with open(llm_output_file, 'r') as f:
        llm_data = json.load(f)
    
    # Remove metadata
    if "selected_function_level_output" in llm_data:
        del llm_data["selected_function_level_output"]
    
    results = {}
    total_tp = 0
    total_fp = 0
    total_fn = 0
    
    for proposal_id, file_data in llm_data.items():
        proposal_key = proposal_id.replace('.md', '')
        
        if proposal_key not in ground_truth:
            print(f"Warning: Proposal {proposal_key} not in ground truth")
            continue
        
        gt_proposal = ground_truth[proposal_key]
        gt_predicted = gt_proposal.get('predicted', {})
        gt_ground_truth = gt_proposal.get('ground_truth', {})
        
        proposal_tp = 0
        proposal_fp = 0
        proposal_fn = 0
        
        # FIXED: Evaluate ALL ground truth functions, not just those in link decision output
        # First, collect all unique files from both ground truth and link decision
        all_files = set(gt_ground_truth.keys()) | set(file_data.keys())
        
        for file_path in all_files:
            gt_file_ground_truth = gt_ground_truth.get(file_path, [])
            function_decisions = file_data.get(file_path, {})
            
            # Evaluate all ground truth functions for this file
            for gt_function in gt_file_ground_truth:
                if gt_function in function_decisions:
                    # Function was considered by link decision
                    decision = function_decisions[gt_function]
                    is_predicted_yes = (decision == "Yes")
                    if is_predicted_yes:
                        proposal_tp += 1
                    else:
                        proposal_fn += 1
                else:
                    # Ground truth function was NOT considered by link decision
                    # This counts as a false negative
                    proposal_fn += 1
            
            # Also count false positives from link decision functions not in ground truth
            for function_name, decision in function_decisions.items():
                if function_name not in gt_file_ground_truth:
                    is_predicted_yes = (decision == "Yes")
                    if is_predicted_yes:
                        proposal_fp += 1
                    # Functions marked "No" that aren't in GT are true negatives (not counted)
        
        # Calculate metrics for this proposal
        precision = proposal_tp / (proposal_tp + proposal_fp) if (proposal_tp + proposal_fp) > 0 else 0
        recall = proposal_tp / (proposal_tp + proposal_fn) if (proposal_tp + proposal_fn) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        
        results[proposal_key] = {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "tp": proposal_tp,
            "fp": proposal_fp,
            "fn": proposal_fn
        }
        
        total_tp += proposal_tp
        total_fp += proposal_fp
        total_fn += proposal_fn
        
        # Debug output to verify the fix
        total_gt_functions = sum(len(funcs) for funcs in gt_ground_truth.values())
        functions_in_link_decision = sum(len(funcs) for funcs in file_data.values())
        
        print(f"{proposal_key}: P={precision:.3f}, R={recall:.3f}, F1={f1:.3f}, TP={proposal_tp}, FP={proposal_fp}, FN={proposal_fn}")
        print(f"  GT functions: {total_gt_functions}, Link decision functions: {functions_in_link_decision}")
    
    # Calculate overall metrics
    overall_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    overall_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    overall_f1 = 2 * overall_precision * overall_recall / (overall_precision + overall_recall) if (overall_precision + overall_recall) > 0 else 0
    
    print(f"\nOverall Results:")
    print(f"Precision: {overall_precision:.4f}")
    print(f"Recall: {overall_recall:.4f}")
    print(f"F1-Score: {overall_f1:.4f}")
    print(f"Total TP: {total_tp}, FP: {total_fp}, FN: {total_fn}")
    
    return {
        "link_decision": {
            "macro_precision": sum(r["precision"] for r in results.values()) / len(results) if results else 0,
            "macro_recall": sum(r["recall"] for r in results.values()) / len(results) if results else 0,
            "macro_f1": sum(r["f1"] for r in results.values()) / len(results) if results else 0,
            "micro_precision": overall_precision,
            "micro_recall": overall_recall,
            "micro_f1": overall_f1,
            "per_proposal": results
        }
    }

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
        raise RuntimeError('No valid output directory found in method_v6/link_decision/output/. All directories are empty or missing llm_outputs.json')
    
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
    parser.add_argument('--output_dir', type=str, default=None, help='Output directory containing llm_outputs.json')
    parser.add_argument('llm_output_file', nargs='?', default=None, help='Path to llm_outputs.json file (for backward compatibility)')
    args = parser.parse_args()

    # Handle backward compatibility with direct file path argument
    if args.llm_output_file:
        llm_output_file = Path(args.llm_output_file)
        if not llm_output_file.exists():
            print(f"LLM output file not found: {llm_output_file}")
            sys.exit(1)
    elif args.output_dir:
        output_dir = Path(args.output_dir)
        llm_output_file = output_dir / 'llm_outputs.json'
        if not llm_output_file.exists():
            print(f"LLM output file not found: {llm_output_file}")
            sys.exit(1)
    else:
        # Interactive selection
        try:
            output_dir = select_output_dir()
            llm_output_file = output_dir / 'llm_outputs.json'
        except RuntimeError as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    ground_truth = load_ground_truth()
    if ground_truth is None:
        sys.exit(1)
    
    results = evaluate_link_decision(llm_output_file, ground_truth)
    
    # Save evaluation results
    output_file = llm_output_file.parent / 'evaluation_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Generate markdown summary
    generate_evaluation_summary(results, llm_output_file.parent, llm_output_file, ground_truth)
    
    print(f"\nEvaluation results saved to: {output_file}")
    print(f"Evaluation summary saved to: {llm_output_file.parent / 'evaluation_summary.md'}")

def generate_evaluation_summary(results, output_dir, llm_output_file, ground_truth):
    """Generate a detailed markdown evaluation summary"""
    link_eval = results['link_decision']
    
    # Read LLM output for detailed analysis
    with open(llm_output_file, 'r') as f:
        llm_data = json.load(f)
    
    # Get selected function-level output
    selected_function_level = llm_data.get("selected_function_level_output", None)
    
    # Remove metadata for processing
    if "selected_function_level_output" in llm_data:
        del llm_data["selected_function_level_output"]
    
    md_lines = []
    md_lines.append("# LLM Directory, File, Function & Link Decision Evaluation Summary\n")
    
    # Load directory, file, and function level results
    dir_eval = {}
    file_eval = {}
    function_eval = {}
    selected_file_level = None
    
    if selected_function_level:
        # Load function-level results
        function_level_output_dir = Path(__file__).parent.parent / 'function_level' / 'output' / selected_function_level
        function_level_eval_path = function_level_output_dir / 'evaluation_results.json'
        function_level_llm_path = function_level_output_dir / 'llm_outputs.json'
        
        if function_level_eval_path.exists():
            try:
                with open(function_level_eval_path, 'r') as f:
                    func_eval_data = json.load(f)
                function_eval = func_eval_data.get('function_level', {})
                print(f"Loaded function level results from {function_level_eval_path}")
                
                # Get selected file-level output from function-level llm_outputs.json
                if function_level_llm_path.exists():
                    with open(function_level_llm_path, 'r') as f:
                        func_llm_data = json.load(f)
                    selected_file_level = func_llm_data.get("selected_file_level_output", None)
                    if selected_file_level:
                        print(f"Found selected file-level output: {selected_file_level}")
            except Exception as e:
                print(f"Warning: Could not load function level results: {e}")
        else:
            print(f"Warning: Function level evaluation results not found at {function_level_eval_path}")
    
    if selected_file_level:
        # Load directory and file-level results
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
    
    # Directory-level macro metrics
    md_lines.append("## Directory-Level Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {len(link_eval['per_proposal'])}")
    if dir_eval:
        proposals_with_links = sum(1 for res in dir_eval.get('per_proposal', {}).values() if res['precision'] > 0.0)
        md_lines.append(f"- **Number of Proposals with at least one correct link (precision > 0)**: {proposals_with_links}")
    md_lines.append(f"- **Macro Precision**: {dir_eval.get('macro_precision', 0):.3f}")
    md_lines.append(f"- **Macro Recall**: {dir_eval.get('macro_recall', 0):.3f}")
    md_lines.append(f"- **Macro F1**: {dir_eval.get('macro_f1', 0):.3f}\n")
    
    # File-level macro metrics
    md_lines.append("## File-Level Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {len(link_eval['per_proposal'])}")
    if file_eval:
        proposals_with_links = sum(1 for res in file_eval.get('per_proposal', {}).values() if res['precision'] > 0.0)
        md_lines.append(f"- **Number of Proposals with at least one correct link (precision > 0)**: {proposals_with_links}")
    md_lines.append(f"- **Macro Precision**: {file_eval.get('macro_precision', 0):.3f}")
    md_lines.append(f"- **Macro Recall**: {file_eval.get('macro_recall', 0):.3f}")
    md_lines.append(f"- **Macro F1**: {file_eval.get('macro_f1', 0):.3f}\n")
    
    # Function-level macro metrics
    md_lines.append("## Function-Level Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {len(link_eval['per_proposal'])}")
    if function_eval:
        proposals_with_links = sum(1 for res in function_eval.get('per_proposal', {}).values() if res['precision'] > 0.0)
        md_lines.append(f"- **Number of Proposals with at least one correct link (precision > 0)**: {proposals_with_links}")
    md_lines.append(f"- **Macro Precision**: {function_eval.get('macro_precision', 0):.3f}")
    md_lines.append(f"- **Macro Recall**: {function_eval.get('macro_recall', 0):.3f}")
    md_lines.append(f"- **Macro F1**: {function_eval.get('macro_f1', 0):.3f}\n")
    
    # Link Decision macro metrics
    md_lines.append("## Link Decision Macro Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {len(link_eval['per_proposal'])}")
    proposals_with_links = sum(1 for res in link_eval['per_proposal'].values() if res['precision'] > 0.0)
    md_lines.append(f"- **Number of Proposals with at least one correct link (precision > 0)**: {proposals_with_links}")
    md_lines.append(f"- **Macro Precision**: {link_eval['macro_precision']:.3f}")
    md_lines.append(f"- **Macro Recall**: {link_eval['macro_recall']:.3f}")
    md_lines.append(f"- **Macro F1**: {link_eval['macro_f1']:.3f}")
    md_lines.append(f"- **Micro Precision**: {link_eval['micro_precision']:.3f}")
    md_lines.append(f"- **Micro Recall**: {link_eval['micro_recall']:.3f}")
    md_lines.append(f"- **Micro F1**: {link_eval['micro_f1']:.3f}\n")
    
    # Directory-level detailed results
    if dir_eval and dir_eval.get('per_proposal'):
        for pid, res in dir_eval['per_proposal'].items():
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
    if file_eval and file_eval.get('per_proposal'):
        for pid, res in file_eval['per_proposal'].items():
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
    
    # Function-level detailed results
    if function_eval and function_eval.get('per_proposal'):
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
    
    # Link Decision detailed per-proposal results
    for proposal_id, res in link_eval['per_proposal'].items():
        proposal_key = proposal_id.replace('.md', '')
        
        md_lines.append(f"\n### 📊 **Proposal #{proposal_key} (Link Decision)**\n")
        found = res['tp']
        total = res['tp'] + res['fn']
        md_lines.append(f"| **Precision** | **Recall** | **F1-Score** | **Found/Total** |")
        md_lines.append(f"|-----------|--------|----------|-------------|")
        md_lines.append(f"| {res['precision']*100:.1f}% | {res['recall']*100:.1f}% | {res['f1']*100:.1f}% | {found}/{total} |")
        md_lines.append(f"\n##### Ground Truth vs Predicted Link Decisions per File\n")
        
        # Get ground truth and predicted data for this proposal
        gt_proposal = ground_truth.get(proposal_key, {})
        gt_ground_truth = gt_proposal.get('ground_truth', {})
        
        # Get LLM predictions for this proposal
        llm_proposal_key = f"{proposal_key}.md"
        file_data = llm_data.get(llm_proposal_key, {})
        
        # Collect all files mentioned in either ground truth or predictions
        all_files = set(gt_ground_truth.keys()) | set(file_data.keys())
        
        for file_path in sorted(all_files):
            gt_functions = set(gt_ground_truth.get(file_path, []))
            predicted_decisions = file_data.get(file_path, {})
            
            # Get functions that were predicted as "Yes"
            predicted_yes_functions = {func for func, decision in predicted_decisions.items() if decision == "Yes"}
            
            md_lines.append(f"- **File:** `{file_path}`")
            md_lines.append(f"    - Ground Truth Functions ({len(gt_functions)}):")
            for func in sorted(gt_functions):
                md_lines.append(f"        - `{func}`")
            md_lines.append(f"    - Predicted 'Yes' Functions ({len(predicted_yes_functions)}):")
            for func in sorted(predicted_yes_functions):
                mark = "✅" if func in gt_functions else "❌"
                md_lines.append(f"        - {mark} `{func}`")
            
            # Also show functions predicted as "No" that should have been "Yes"
            predicted_no_functions = {func for func, decision in predicted_decisions.items() if decision == "No"}
            missed_functions = gt_functions & predicted_no_functions
            if missed_functions:
                md_lines.append(f"    - Missed Functions (predicted 'No' but should be 'Yes') ({len(missed_functions)}):")
                for func in sorted(missed_functions):
                    md_lines.append(f"        - ❌ `{func}`")
            
            md_lines.append("")
    
    # Write the summary
    md_content = '\n'.join(md_lines)
    with open(output_dir / 'evaluation_summary.md', 'w') as f:
        f.write(md_content)

if __name__ == "__main__":
    main()
