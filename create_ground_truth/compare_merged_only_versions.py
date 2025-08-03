#!/usr/bin/env python3
"""
新旧merged_only版の違いを調査するスクリプト
210→211の増加を詳細に分析する
"""

import json
import os

def load_ground_truth_data(file_path):
    """Ground Truthデータを読み込み"""
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

def compare_versions():
    """新旧merged_only版を比較"""
    
    print("🔍 新旧merged_only版の比較開始")
    
    # データ読み込み
    old_path = "../data/ground_truth/accepted_proposals_ground_truth_merged_only.json"
    new_path = "../data/ground_truth/accepted_proposals_ground_truth_merged_only_fixed.json"
    
    print(f"📁 旧版: {old_path}")
    print(f"📁 新版: {new_path}")
    
    old_data = load_ground_truth_data(old_path)
    new_data = load_ground_truth_data(new_path)
    
    if not old_data or not new_data:
        print("❌ データの読み込みに失敗しました")
        return
    
    # 提案IDでセット作成
    old_proposals = {item['proposal_id'] for item in old_data}
    new_proposals = {item['proposal_id'] for item in new_data}
    
    print(f"\n📊 基本統計:")
    print(f"├─ 旧版提案数: {len(old_proposals)}")
    print(f"├─ 新版提案数: {len(new_proposals)}")
    print(f"└─ 差分: {len(new_proposals) - len(old_proposals)}")
    
    # 差分分析
    added_proposals = new_proposals - old_proposals
    removed_proposals = old_proposals - new_proposals
    common_proposals = old_proposals & new_proposals
    
    print(f"\n🔍 詳細分析:")
    print(f"├─ 共通提案: {len(common_proposals)}")
    print(f"├─ 新版のみ: {len(added_proposals)}")
    print(f"└─ 旧版のみ: {len(removed_proposals)}")
    
    if added_proposals:
        print(f"\n✅ 新版で追加された提案:")
        for proposal_id in sorted(added_proposals):
            # 新版から詳細を取得
            for item in new_data:
                if item['proposal_id'] == proposal_id:
                    files_count = len(item.get('files', []))
                    functions_count = len(item.get('detected_functions', []))
                    print(f"   └─ {proposal_id}: {files_count}ファイル, {functions_count}関数")
                    
                    # ファイルパスをチェック
                    files = item.get('files', [])
                    vendor_files = [f for f in files if '/vendor/' in f]
                    if vendor_files:
                        print(f"      └─ vendorファイル: {vendor_files}")
                    break
    
    if removed_proposals:
        print(f"\n❌ 新版で削除された提案:")
        for proposal_id in sorted(removed_proposals):
            # 旧版から詳細を取得
            for item in old_data:
                if item['proposal_id'] == proposal_id:
                    files_count = len(item.get('files', []))
                    functions_count = len(item.get('detected_functions', []))
                    print(f"   └─ {proposal_id}: {files_count}ファイル, {functions_count}関数")
                    break
    
    # 共通提案での関数数変化
    print(f"\n📈 共通提案での変化:")
    function_changes = []
    
    old_dict = {item['proposal_id']: item for item in old_data}
    new_dict = {item['proposal_id']: item for item in new_data}
    
    for proposal_id in common_proposals:
        old_item = old_dict[proposal_id]
        new_item = new_dict[proposal_id]
        
        old_functions = len(old_item.get('detected_functions', []))
        new_functions = len(new_item.get('detected_functions', []))
        function_diff = new_functions - old_functions
        
        if function_diff != 0:
            function_changes.append({
                'proposal_id': proposal_id,
                'old_functions': old_functions,
                'new_functions': new_functions,
                'diff': function_diff
            })
    
    print(f"├─ 関数数が変化した提案: {len(function_changes)}")
    
    if function_changes:
        # 最も変化の大きい提案を表示
        function_changes.sort(key=lambda x: abs(x['diff']), reverse=True)
        print(f"└─ 最も変化の大きい提案（上位5件）:")
        for change in function_changes[:5]:
            print(f"   └─ {change['proposal_id']}: {change['old_functions']}→{change['new_functions']} ({change['diff']:+d})")

def main():
    """メイン処理"""
    compare_versions()

if __name__ == "__main__":
    main()
