#!/usr/bin/env python3
"""
Method v8: File Level Link Decision Evaluation

This script evaluates the file-level link decision results.
It compares the predicted file relevance against ground truth data.
This is a new component in method v8 that uses skeleton view analysis.
"""

import json
import sys
from pathlib import Path

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
        raise RuntimeError('No valid output directory found in method_v8/file_level_link_decision/output/. All directories are empty or missing llm_outputs.json')
    
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

def evaluate_file_level_link_decision(output_dir=None):
    """
    File-level link decision結果を評価し、evaluation_results.jsonとevaluation_summary.mdを出力
    """
    if output_dir is None:
        # Interactive selection
        try:
            output_dir = select_output_dir()
        except RuntimeError as e:
            print(f"Error: {e}")
            return
    
    results_file = output_dir / 'llm_outputs.json'
    if not results_file.exists():
        print(f"Error: Results file {results_file} not found")
        return
    
    # Load results
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    # Display which directory_and_file_localization output was used
    selected_dir_file_output = results.get("selected_directory_and_file_localization_output", "Unknown")
    print(f"This file-level link decision used directory_and_file_localization output: {selected_dir_file_output}")
    
    # Filter out metadata keys to get only proposal results
    proposal_results = {}
    for key, value in results.items():
        if not key.startswith("selected_"):
            proposal_results[key] = value
    
    print(f"Found {len(proposal_results)} proposal results to evaluate")
    
    # Load ground truth
    ground_truth_file = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals_ground_truth.json'
    if not ground_truth_file.exists():
        print(f"Error: Ground truth file {ground_truth_file} not found")
        return
    
    with open(ground_truth_file, 'r') as f:
        ground_truth_data = json.load(f)
    
    # Convert ground truth to proposal_id -> files mapping
    ground_truth = {}
    for entry in ground_truth_data:
        if isinstance(entry, dict):
            proposal_id = entry.get('proposal_id')
            files = entry.get('files', [])
            if proposal_id:
                ground_truth[proposal_id] = {'relevant_files': files}
    
    print("File-Level Link Decision Evaluation Results")
    print("=" * 50)
    
    total_proposals = 0
    total_precision_sum = 0
    total_recall_sum = 0
    total_f1_sum = 0
    proposals_with_data = 0
    proposals_with_correct_files = 0
    
    detailed_results = {}
    
    for proposal_name, result in proposal_results.items():
        total_proposals += 1
        
        # Validate result structure
        if not isinstance(result, dict):
            print(f"Warning: Invalid result structure for {proposal_name}, skipping")
            continue
        
        # Get predicted relevant files from Yes decisions
        predicted_files = set()
        for file_path, decision in result.items():
            if isinstance(decision, str) and decision.lower() == 'yes':
                predicted_files.add(file_path)
        
        # Get ground truth files for this proposal
        gt_key = proposal_name.replace('.md', '')
        if gt_key not in ground_truth:
            print(f"Warning: No ground truth found for {proposal_name}")
            continue
        
        gt_files = set(ground_truth[gt_key].get('relevant_files', []))
        
        if not gt_files:
            print(f"Warning: No ground truth files for {proposal_name}")
            continue
        
        proposals_with_data += 1
        
        # Calculate metrics
        tp = len(predicted_files & gt_files)  # True positives
        fp = len(predicted_files - gt_files)  # False positives
        fn = len(gt_files - predicted_files)  # False negatives
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        
        # Count proposals with at least one correct file
        if precision > 0:
            proposals_with_correct_files += 1
        
        total_precision_sum += precision
        total_recall_sum += recall
        total_f1_sum += f1
        
        detailed_results[proposal_name] = {
            'predicted_count': len(predicted_files),
            'ground_truth_count': len(gt_files),
            'true_positives': tp,
            'false_positives': fp,
            'false_negatives': fn,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'predicted': list(predicted_files),
            'ground_truth': list(gt_files),
            'tp': tp,
            'fp': fp,
            'fn': fn
        }
        
        print(f"\n{proposal_name}:")
        print(f"  Predicted: {len(predicted_files)} files")
        print(f"  Ground Truth: {len(gt_files)} files")
        print(f"  True Positives: {tp}")
        print(f"  False Positives: {fp}")
        print(f"  False Negatives: {fn}")
        print(f"  Precision: {precision:.3f}")
        print(f"  Recall: {recall:.3f}")
        print(f"  F1-Score: {f1:.3f}")
    
    # Calculate macro averages
    average_precision = total_precision_sum / proposals_with_data if proposals_with_data > 0 else 0
    average_recall = total_recall_sum / proposals_with_data if proposals_with_data > 0 else 0
    average_f1 = total_f1_sum / proposals_with_data if proposals_with_data > 0 else 0
    
    print(f"\n{'='*50}")
    print(f"Overall Performance:")
    print(f"  Processed Proposals: {proposals_with_data}")
    print(f"  Proposals with at least one correct file (precision > 0): {proposals_with_correct_files}")
    print(f"  Average Precision: {average_precision:.3f}")
    print(f"  Average Recall: {average_recall:.3f}")
    print(f"  Average F1-Score: {average_f1:.3f}")
    
    # Prepare evaluation results
    evaluation_results = {
        'file_level_link_decision': {
            'macro_precision': average_precision,
            'macro_recall': average_recall,
            'macro_f1': average_f1,
            'proposals_with_data': proposals_with_data,
            'proposals_with_correct_files': proposals_with_correct_files,
            'total_proposals': total_proposals,
            'average_precision': average_precision,
            'average_recall': average_recall,
            'average_f1': average_f1,
            'per_proposal': detailed_results,
            'selected_directory_and_file_localization_output': selected_dir_file_output
        }
    }
    
    # Save evaluation results as JSON
    evaluation_results_file = output_dir / 'evaluation_results.json'
    with open(evaluation_results_file, 'w') as f:
        json.dump(evaluation_results, f, indent=2)
    print(f"\nEvaluation results saved to: {evaluation_results_file}")
    
    # Generate evaluation summary markdown
    md_lines = []
    md_lines.append("# File-Level Link Decision Evaluation Summary\n")
    md_lines.append(f"**Used directory_and_file_localization output:** `{selected_dir_file_output}`\n")
    
    # Overall metrics
    md_lines.append("## Overall Metrics\n")
    md_lines.append(f"- **Number of Processed Proposals**: {proposals_with_data}")
    md_lines.append(f"- **Number of Proposals with at least one correct file (precision > 0)**: {proposals_with_correct_files}")
    md_lines.append(f"- **Total Proposals**: {total_proposals}")
    md_lines.append(f"- **Macro Precision**: {average_precision:.3f}")
    md_lines.append(f"- **Macro Recall**: {average_recall:.3f}")
    md_lines.append(f"- **Macro F1**: {average_f1:.3f}\n")
    
    # Detailed per-proposal results
    md_lines.append("## Per-Proposal Results\n")
    for proposal_name, result in detailed_results.items():
        proposal_id = proposal_name.replace('.md', '')
        md_lines.append(f"### 📊 **Proposal #{proposal_id}**\n")
        found = result['true_positives']
        total = result['true_positives'] + result['false_negatives']
        md_lines.append(f"| **Precision** | **Recall** | **F1-Score** | **Found/Total** |")
        md_lines.append(f"|-----------|--------|----------|-------------|")
        md_lines.append(f"| {result['precision']*100:.1f}% | {result['recall']*100:.1f}% | {result['f1']*100:.1f}% | {found}/{total} |")
        
        md_lines.append(f"\n##### Ground Truth vs Predicted Files\n")
        gt_files = set(result['ground_truth'])
        pred_files = set(result['predicted'])
        
        md_lines.append(f"**Ground Truth Files ({len(gt_files)}):**")
        for file_path in sorted(gt_files):
            md_lines.append(f"- `{file_path}`")
        md_lines.append("")
        
        md_lines.append(f"**Predicted Files ({len(pred_files)}):**")
        for file_path in sorted(pred_files):
            mark = "✅" if file_path in gt_files else "❌"
            md_lines.append(f"- {mark} `{file_path}`")
        md_lines.append("")
    
    # Save evaluation summary markdown
    md_content = '\n'.join(md_lines)
    evaluation_summary_file = output_dir / 'evaluation_summary.md'
    with open(evaluation_summary_file, 'w') as f:
        f.write(md_content)
    print(f"Evaluation summary saved to: {evaluation_summary_file}")
    
    return evaluation_results

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', type=str, default=None, help='Output directory containing llm_outputs.json')
    args = parser.parse_args()

    if args.output_dir:
        output_dir = Path(args.output_dir)
        llm_output_file = output_dir / 'llm_outputs.json'
        if not llm_output_file.exists():
            print(f"LLM output file not found: {llm_output_file}")
            sys.exit(1)
        evaluate_file_level_link_decision(output_dir)
    else:
        # Interactive selection
        evaluate_file_level_link_decision()

if __name__ == '__main__':
    main()
