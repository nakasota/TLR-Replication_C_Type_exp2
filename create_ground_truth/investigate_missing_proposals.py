#!/usr/bin/env python3
"""
除外された提案の詳細調査スクリプト
なぜmerged_onlyにのみ存在する提案があるのかを調査する
"""

import json
import os
from pathlib import Path

def load_json_data(file_path):
    """JSONデータを読み込み"""
    if not os.path.exists(file_path):
        print(f"❌ ファイルが見つかりません: {file_path}")
        return None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    
    if isinstance(raw_data, dict) and 'ground_truth' in raw_data:
        return raw_data['ground_truth']
    elif isinstance(raw_data, list):
        return raw_data
    else:
        return raw_data

def investigate_missing_proposals():
    """除外された提案を詳細調査"""
    
    print("🔍 除外された提案の詳細調査開始")
    
    # データ読み込み
    merged_only_path = "../data/ground_truth/accepted_proposals_ground_truth_merged_only.json"
    content_validated_path = "../data/ground_truth/accepted_proposals_ground_truth_content_validated.json"
    
    merged_only_data = load_json_data(merged_only_path)
    content_validated_data = load_json_data(content_validated_path)
    
    if not merged_only_data or not content_validated_data:
        print("❌ データの読み込みに失敗しました")
        return
    
    # 提案IDでインデックス作成
    merged_only_dict = {item['proposal_id']: item for item in merged_only_data}
    content_validated_dict = {item['proposal_id']: item for item in content_validated_data}
    
    # 除外された提案ID
    merged_only_proposals = set(merged_only_dict.keys())
    content_validated_proposals = set(content_validated_dict.keys())
    missing_proposals = merged_only_proposals - content_validated_proposals
    
    print(f"📋 除外された提案: {sorted(missing_proposals)}")
    
    # 各除外提案の詳細調査
    for proposal_id in sorted(missing_proposals):
        print(f"\n🔬 提案 {proposal_id} の詳細:")
        item = merged_only_dict[proposal_id]
        
        print(f"├─ ファイル数: {len(item.get('files', []))}")
        print(f"├─ 関数数: {len(item.get('detected_functions', []))}")
        print(f"├─ MERGED CL数: {item.get('merged_cl_count', 'N/A')}")
        print(f"└─ 関連ファイル: {item.get('files', [])}")
        
        # 関数の詳細
        functions = item.get('detected_functions', [])
        if functions:
            print(f"   📑 関数一覧:")
            for func in functions:
                func_name = func.get('function_name', 'unknown')
                file_path = func.get('file_path', 'unknown')
                cl_status = func.get('cl_status', 'unknown')
                print(f"      └─ {func_name} in {file_path} (CL status: {cl_status})")
    
    # 元の関数解析データも確認
    print(f"\n🔍 元の関数解析データでの確認:")
    func_analysis_merged_path = "../data/ground_truth/accepted_proposals_func_analysis_merged_validated.json"
    
    if os.path.exists(func_analysis_merged_path):
        with open(func_analysis_merged_path, 'r', encoding='utf-8') as f:
            func_analysis_data = json.load(f)
        
        results = func_analysis_data.get('results', [])
        
        for proposal_id in sorted(missing_proposals):
            print(f"\n📊 提案 {proposal_id} の元データ:")
            
            # 該当提案を検索
            proposal_found = False
            for proposal in results:
                proposal_file = proposal.get('proposal_file', '')
                if proposal_id in proposal_file:
                    proposal_found = True
                    print(f"├─ 見つかりました: {proposal_file}")
                    
                    cl_analyses = proposal.get('cl_analyses', [])
                    print(f"├─ CL数: {len(cl_analyses)}")
                    
                    for i, cl_analysis in enumerate(cl_analyses):
                        cl_status = cl_analysis.get('status', 'unknown')
                        cl_number = cl_analysis.get('cl_number', 'unknown')
                        files = cl_analysis.get('files', [])
                        print(f"├─ CL{i+1}: {cl_number} (status: {cl_status}, files: {len(files)})")
                        
                        # ファイル内の関数をチェック
                        for file_data in files:
                            file_path = file_data.get('file_path', 'unknown')
                            ast_analysis = file_data.get('ast_analysis', {})
                            detected_functions = ast_analysis.get('detected_functions', [])
                            
                            if detected_functions:
                                print(f"│  └─ {file_path}: {len(detected_functions)}関数")
                                for func in detected_functions:
                                    func_name = func.get('function_name', 'unknown')
                                    function_changes = func.get('function_changes', {})
                                    added_lines = function_changes.get('added_lines', [])
                                    print(f"│     └─ {func_name} (追加行: {len(added_lines)}行)")
                    break
            
            if not proposal_found:
                print(f"├─ ❌ 元データに見つかりませんでした")

def main():
    """メイン処理"""
    investigate_missing_proposals()

if __name__ == "__main__":
    main()
