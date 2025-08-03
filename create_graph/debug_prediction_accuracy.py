#!/usr/bin/env python3
"""
Method v6の予測判定の具体例を表示するデバッグスクリプト
"""

import json
from collections import defaultdict

def load_ground_truth():
    """Ground truthデータを読み込む"""
    ground_truth_path = "/workspace/data/processed/proposal_mappings/validated/accepted_proposals_FUNCTION_LEVEL_GROUND_TRUTH.json"
    
    with open(ground_truth_path, 'r') as f:
        ground_truth_data = json.load(f)
    
    # Proposal IDごとにground truthを整理
    ground_truth_by_proposal = defaultdict(set)
    for entry in ground_truth_data:
        proposal_id, file_path, function_name = entry
        ground_truth_by_proposal[str(proposal_id)].add((file_path, function_name))
    
    return ground_truth_by_proposal

def load_method_v6_outputs():
    """Method v6の結果を読み込む"""
    llm_outputs_path = "/workspace/method_v6/link_decision/output/20250716_160634/llm_outputs.json"
    
    with open(llm_outputs_path, 'r') as f:
        llm_outputs = json.load(f)
    
    return llm_outputs

def debug_specific_proposal(proposal_id, ground_truth_by_proposal, llm_outputs):
    """特定のproposalの判定を詳細に表示"""
    
    print(f"\n{'='*60}")
    print(f"PROPOSAL {proposal_id} - 詳細な判定プロセス")
    print(f"{'='*60}")
    
    # Ground truthを取得
    ground_truth_functions = ground_truth_by_proposal.get(proposal_id, set())
    print(f"\n🎯 Ground Truth (正解データ): {len(ground_truth_functions)}個の関数")
    for i, (file_path, func_name) in enumerate(sorted(ground_truth_functions), 1):
        print(f"  {i}. {file_path} -> {func_name}")
    
    # Method v6の予測を取得
    proposal_key = f"{proposal_id}.md"
    if proposal_key not in llm_outputs:
        print(f"❌ Proposal {proposal_id} not found in method_v6 outputs")
        return
    
    file_predictions = llm_outputs[proposal_key]
    
    print(f"\n🤖 Method v6の予測:")
    true_positives = []
    false_positives = []
    
    for file_path, function_predictions in file_predictions.items():
        for function_name, prediction in function_predictions.items():
            if prediction == "Yes":
                predicted_function = (file_path, function_name)
                
                if predicted_function in ground_truth_functions:
                    # True Positive: 正しい予測
                    true_positives.append(predicted_function)
                    print(f"  ✅ {file_path} -> {function_name} (TRUE POSITIVE)")
                else:
                    # False Positive: 間違った予測
                    false_positives.append(predicted_function)
                    print(f"  ❌ {file_path} -> {function_name} (FALSE POSITIVE)")
    
    print(f"\n📊 判定結果:")
    print(f"  True Positives (正解): {len(true_positives)}個")
    print(f"  False Positives (間違い): {len(false_positives)}個")
    print(f"  Precision (精度): {len(true_positives)/(len(true_positives)+len(false_positives))*100:.1f}%")
    
    # Ground truthで見つからなかった関数（False Negatives）
    missed_functions = ground_truth_functions - set(true_positives)
    if missed_functions:
        print(f"  False Negatives (見逃し): {len(missed_functions)}個")
        for file_path, func_name in sorted(missed_functions):
            print(f"    🔍 見逃し: {file_path} -> {func_name}")
    
    recall = len(true_positives) / len(ground_truth_functions) * 100 if ground_truth_functions else 0
    print(f"  Recall (再現率): {recall:.1f}%")

def main():
    print("Loading data...")
    ground_truth = load_ground_truth()
    llm_outputs = load_method_v6_outputs()
    
    # 処理可能なproposalを除外
    proposal_outputs = {k: v for k, v in llm_outputs.items() if not k.startswith('selected_')}
    
    print("Method v6予測判定の仕組みを具体例で説明します")
    
    # 特定のproposalの詳細を表示
    examples = ["45428", "40995", "46518"]  # 結果が良いproposalを例として
    
    for proposal_id in examples:
        if proposal_id in ground_truth and f"{proposal_id}.md" in proposal_outputs:
            debug_specific_proposal(proposal_id, ground_truth, llm_outputs)
        else:
            print(f"⚠️ Proposal {proposal_id} not available for analysis")
    
    print(f"\n{'='*60}")
    print("判定の仕組み（まとめ）:")
    print("1. Ground Truth: [proposal_id, file_path, function_name]の正解データ")
    print("2. Method v6: 各関数に対して'Yes'/'No'の予測")  
    print("3. True Positive: Method v6が'Yes'と予測 AND Ground Truthに存在")
    print("4. False Positive: Method v6が'Yes'と予測 BUT Ground Truthに存在しない")
    print("5. False Negative: Method v6が'No'と予測 BUT Ground Truthに存在する")
    print(f"{'='*60}")

if __name__ == "__main__":
    main() 