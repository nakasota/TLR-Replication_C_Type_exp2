#!/usr/bin/env python3
"""
Ground Truth版の詳細比較スクリプト
merged_onlyとcontent_validatedの違いを詳細に分析する
"""

import json
import os
from pathlib import Path
from collections import defaultdict, Counter

def load_ground_truth_data(file_path):
    """Ground Truthデータを読み込み"""
    if not os.path.exists(file_path):
        print(f"❌ ファイルが見つかりません: {file_path}")
        return None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    
    # データ形式を確認して適切に処理
    if isinstance(raw_data, dict) and 'ground_truth' in raw_data:
        # {ground_truth: [...]} 形式
        return raw_data['ground_truth']
    elif isinstance(raw_data, list):
        # [...] 形式
        return raw_data
    else:
        print(f"❌ 不明なデータ形式: {file_path}")
        return None

def analyze_ground_truth(data, version_name):
    """Ground Truthデータを分析"""
    print(f"\n📊 {version_name} の分析:")
    
    if not data:
        print("❌ データが空です")
        return {}
    
    total_proposals = len(data)
    total_files = sum(len(item.get('files', [])) for item in data)
    total_functions = sum(len(item.get('detected_functions', [])) for item in data)
    
    # 提案別統計
    proposal_stats = []
    for item in data:
        proposal_id = item.get('proposal_id', 'unknown')
        files_count = len(item.get('files', []))
        functions_count = len(item.get('detected_functions', []))
        proposal_stats.append({
            'proposal_id': proposal_id,
            'files_count': files_count,
            'functions_count': functions_count
        })
    
    # 基本統計
    print(f"├─ 提案数: {total_proposals}")
    print(f"├─ 総ファイル数: {total_files}")
    print(f"├─ 総関数数: {total_functions}")
    print(f"├─ 平均ファイル数/提案: {total_files/total_proposals:.2f}")
    print(f"└─ 平均関数数/提案: {total_functions/total_proposals:.2f}")
    
    return {
        'total_proposals': total_proposals,
        'total_files': total_files,
        'total_functions': total_functions,
        'proposal_stats': proposal_stats,
        'data': data
    }

def compare_ground_truth_versions(merged_only_data, content_validated_data):
    """2つのGround Truth版を比較"""
    print(f"\n🔍 詳細比較分析:")
    
    # 提案IDをキーとした辞書を作成
    merged_only_dict = {item['proposal_id']: item for item in merged_only_data['data']}
    content_validated_dict = {item['proposal_id']: item for item in content_validated_data['data']}
    
    # 提案の差分
    merged_only_proposals = set(merged_only_dict.keys())
    content_validated_proposals = set(content_validated_dict.keys())
    
    removed_proposals = merged_only_proposals - content_validated_proposals
    remaining_proposals = merged_only_proposals & content_validated_proposals
    
    print(f"├─ merged_onlyにのみ存在する提案: {len(removed_proposals)}")
    print(f"├─ 両方に存在する提案: {len(remaining_proposals)}")
    print(f"└─ 除外された提案: {len(removed_proposals)}")
    
    # 除外された提案の詳細
    if removed_proposals:
        print(f"\n❌ 除外された提案一覧:")
        for proposal_id in sorted(removed_proposals):
            item = merged_only_dict[proposal_id]
            files_count = len(item.get('files', []))
            functions_count = len(item.get('detected_functions', []))
            print(f"   └─ {proposal_id}: {files_count}ファイル, {functions_count}関数")
    
    # 残った提案での関数数の変化
    function_changes = []
    
    for proposal_id in remaining_proposals:
        merged_item = merged_only_dict[proposal_id]
        validated_item = content_validated_dict[proposal_id]
        
        merged_files = len(merged_item.get('files', []))
        validated_files = len(validated_item.get('files', []))
        file_diff = validated_files - merged_files
        
        merged_functions = len(merged_item.get('detected_functions', []))
        validated_functions = len(validated_item.get('detected_functions', []))
        function_diff = validated_functions - merged_functions
        
        if file_diff != 0 or function_diff != 0:
            function_changes.append({
                'proposal_id': proposal_id,
                'file_diff': file_diff,
                'function_diff': function_diff,
                'merged_files': merged_files,
                'validated_files': validated_files,
                'merged_functions': merged_functions,
                'validated_functions': validated_functions
            })
    
    print(f"\n📈 関数・ファイル数の変化がある提案: {len(function_changes)}")
    
    if function_changes:
        print(f"\n📉 関数・ファイル数が減少した提案:")
        for change in sorted(function_changes, key=lambda x: x['function_diff']):
            if change['function_diff'] < 0 or change['file_diff'] < 0:
                print(f"   └─ {change['proposal_id']}: "
                      f"ファイル {change['merged_files']}→{change['validated_files']} "
                      f"({change['file_diff']:+d}), "
                      f"関数 {change['merged_functions']}→{change['validated_functions']} "
                      f"({change['function_diff']:+d})")
    
    return {
        'removed_proposals': removed_proposals,
        'remaining_proposals': remaining_proposals,
        'function_changes': function_changes
    }

def analyze_removed_functions(merged_only_data, content_validated_data):
    """除外された関数の詳細分析"""
    print(f"\n🔬 除外された関数の詳細分析:")
    
    # 提案IDをキーとした辞書を作成
    merged_only_dict = {item['proposal_id']: item for item in merged_only_data['data']}
    content_validated_dict = {item['proposal_id']: item for item in content_validated_data['data']}
    
    # 全関数を収集
    merged_functions = {}  # (proposal_id, file_path, function_name) -> function_data
    validated_functions = {}
    
    for proposal_id, item in merged_only_dict.items():
        for func in item.get('detected_functions', []):
            key = (proposal_id, func.get('file_path'), func.get('function_name'))
            merged_functions[key] = func
    
    for proposal_id, item in content_validated_dict.items():
        for func in item.get('detected_functions', []):
            key = (proposal_id, func.get('file_path'), func.get('function_name'))
            validated_functions[key] = func
    
    # 除外された関数
    removed_functions = set(merged_functions.keys()) - set(validated_functions.keys())
    
    print(f"├─ merged_onlyの総関数数: {len(merged_functions)}")
    print(f"├─ content_validatedの総関数数: {len(validated_functions)}")
    print(f"└─ 除外された関数数: {len(removed_functions)}")
    
    if removed_functions:
        # ファイルパス別の集計
        file_counter = Counter()
        proposal_counter = Counter()
        
        print(f"\n📋 除外された関数の例（最初の20件）:")
        for i, (proposal_id, file_path, func_name) in enumerate(sorted(removed_functions)):
            if i < 20:
                print(f"   └─ {proposal_id}: {file_path} -> {func_name}")
            file_counter[file_path] += 1
            proposal_counter[proposal_id] += 1
        
        print(f"\n📂 除外関数が多いファイル（上位10件）:")
        for file_path, count in file_counter.most_common(10):
            print(f"   └─ {file_path}: {count}関数")
        
        print(f"\n📋 除外関数が多い提案（上位10件）:")
        for proposal_id, count in proposal_counter.most_common(10):
            print(f"   └─ {proposal_id}: {count}関数")
    
    return removed_functions

def save_comparison_report(analysis_results, output_path):
    """比較結果をJSONファイルに保存"""
    report = {
        'merged_only_stats': {
            'total_proposals': analysis_results['merged_only']['total_proposals'],
            'total_files': analysis_results['merged_only']['total_files'],
            'total_functions': analysis_results['merged_only']['total_functions']
        },
        'content_validated_stats': {
            'total_proposals': analysis_results['content_validated']['total_proposals'],
            'total_files': analysis_results['content_validated']['total_files'],
            'total_functions': analysis_results['content_validated']['total_functions']
        },
        'differences': {
            'removed_proposals_count': len(analysis_results['comparison']['removed_proposals']),
            'removed_proposals': list(analysis_results['comparison']['removed_proposals']),
            'function_changes_count': len(analysis_results['comparison']['function_changes']),
            'function_changes': analysis_results['comparison']['function_changes']
        },
        'removed_functions_count': len(analysis_results['removed_functions'])
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"💾 比較レポートを保存: {output_path}")

def main():
    """メイン処理"""
    print("🔍 Ground Truth版詳細比較開始")
    
    # データ読み込み
    merged_only_path = "../data/ground_truth/accepted_proposals_ground_truth_merged_only.json"
    content_validated_path = "../data/ground_truth/accepted_proposals_ground_truth_content_validated.json"
    
    print(f"📁 merged_only: {merged_only_path}")
    print(f"📁 content_validated: {content_validated_path}")
    
    merged_only_data = load_ground_truth_data(merged_only_path)
    content_validated_data = load_ground_truth_data(content_validated_path)
    
    if not merged_only_data or not content_validated_data:
        print("❌ データの読み込みに失敗しました")
        return
    
    # 各版の分析
    merged_only_analysis = analyze_ground_truth(merged_only_data, "merged_only")
    content_validated_analysis = analyze_ground_truth(content_validated_data, "content_validated")
    
    # 比較分析
    comparison_results = compare_ground_truth_versions(merged_only_analysis, content_validated_analysis)
    
    # 除外された関数の詳細分析
    removed_functions = analyze_removed_functions(merged_only_analysis, content_validated_analysis)
    
    # 結果をまとめてレポート保存
    analysis_results = {
        'merged_only': merged_only_analysis,
        'content_validated': content_validated_analysis,
        'comparison': comparison_results,
        'removed_functions': removed_functions
    }
    
    output_path = "../data/ground_truth/detailed_ground_truth_comparison_report.json"
    save_comparison_report(analysis_results, output_path)
    
    print(f"\n✅ 詳細比較分析完了！")

if __name__ == "__main__":
    main()
