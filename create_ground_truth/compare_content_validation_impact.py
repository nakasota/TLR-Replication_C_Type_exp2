#!/usr/bin/env python3
"""
content_validated版とmerged_only版のGround Truth比較スクリプト
変更内容検証の効果を詳細に分析する
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
        return raw_data['ground_truth']
    elif isinstance(raw_data, list):
        return raw_data
    else:
        print(f"❌ 不明なデータ形式: {file_path}")
        return None

def analyze_ground_truth_quality(data, version_name):
    """Ground Truth品質を分析"""
    print(f"\n📊 {version_name} の詳細分析:")
    
    if not data:
        print("❌ データが空です")
        return {}
    
    total_proposals = len(data)
    total_files = sum(len(item.get('files', [])) for item in data)
    total_functions = sum(len(item.get('detected_functions', [])) for item in data)
    
    # 提案別統計
    proposal_stats = []
    content_validation_count = 0
    validation_status_counts = Counter()
    
    for item in data:
        proposal_id = item.get('proposal_id', 'unknown')
        files_count = len(item.get('files', []))
        functions_count = len(item.get('detected_functions', []))
        
        # content_validation情報を分析
        functions_with_validation = 0
        for func in item.get('detected_functions', []):
            if 'content_validation' in func:
                functions_with_validation += 1
                content_validation_count += 1
                validation_status = func['content_validation'].get('validation_status', 'unknown')
                validation_status_counts[validation_status] += 1
        
        proposal_stats.append({
            'proposal_id': proposal_id,
            'files_count': files_count,
            'functions_count': functions_count,
            'functions_with_validation': functions_with_validation
        })
    
    # 基本統計
    print(f"├─ 提案数: {total_proposals}")
    print(f"├─ 総ファイル数: {total_files}")
    print(f"├─ 総関数数: {total_functions}")
    print(f"├─ 平均ファイル数/提案: {total_files/total_proposals:.2f}")
    print(f"├─ 平均関数数/提案: {total_functions/total_proposals:.2f}")
    print(f"├─ 変更内容検証済み関数: {content_validation_count}")
    
    if validation_status_counts:
        print(f"└─ 検証ステータス内訳:")
        for status, count in validation_status_counts.most_common():
            print(f"   └─ {status}: {count}関数")
    
    return {
        'total_proposals': total_proposals,
        'total_files': total_files,
        'total_functions': total_functions,
        'proposal_stats': proposal_stats,
        'content_validation_count': content_validation_count,
        'validation_status_counts': validation_status_counts,
        'data': data
    }

def compare_ground_truth_impact(merged_only_data, content_validated_data):
    """変更内容検証の影響を比較"""
    print(f"\n🔍 変更内容検証の影響分析:")
    
    # 提案IDをキーとした辞書を作成
    merged_only_dict = {item['proposal_id']: item for item in merged_only_data['data']}
    content_validated_dict = {item['proposal_id']: item for item in content_validated_data['data']}
    
    # 提案の差分
    merged_only_proposals = set(merged_only_dict.keys())
    content_validated_proposals = set(content_validated_dict.keys())
    
    removed_proposals = merged_only_proposals - content_validated_proposals
    remaining_proposals = merged_only_proposals & content_validated_proposals
    
    print(f"├─ merged_onlyの提案数: {len(merged_only_proposals)}")
    print(f"├─ content_validatedの提案数: {len(content_validated_proposals)}")
    print(f"├─ 除外された提案: {len(removed_proposals)}")
    print(f"└─ 残存した提案: {len(remaining_proposals)}")
    
    # 除外された提案の詳細
    if removed_proposals:
        print(f"\n❌ 変更内容検証で除外された提案:")
        for proposal_id in sorted(removed_proposals):
            item = merged_only_dict[proposal_id]
            files_count = len(item.get('files', []))
            functions_count = len(item.get('detected_functions', []))
            print(f"   └─ {proposal_id}: {files_count}ファイル, {functions_count}関数")
    
    # 残った提案での関数数の変化
    function_reductions = []
    total_functions_removed = 0
    
    for proposal_id in remaining_proposals:
        merged_item = merged_only_dict[proposal_id]
        validated_item = content_validated_dict[proposal_id]
        
        merged_functions = len(merged_item.get('detected_functions', []))
        validated_functions = len(validated_item.get('detected_functions', []))
        function_diff = validated_functions - merged_functions
        
        if function_diff < 0:
            function_reductions.append({
                'proposal_id': proposal_id,
                'function_diff': function_diff,
                'merged_functions': merged_functions,
                'validated_functions': validated_functions
            })
            total_functions_removed += abs(function_diff)
    
    print(f"\n📉 関数数が減少した提案: {len(function_reductions)}")
    print(f"📊 総除外関数数: {total_functions_removed}")
    
    if function_reductions:
        print(f"\n🔬 関数数減少の詳細（上位10件）:")
        for reduction in sorted(function_reductions, key=lambda x: x['function_diff'])[:10]:
            print(f"   └─ {reduction['proposal_id']}: "
                  f"{reduction['merged_functions']}→{reduction['validated_functions']} "
                  f"({reduction['function_diff']} 関数除外)")
    
    return {
        'removed_proposals': removed_proposals,
        'remaining_proposals': remaining_proposals,
        'function_reductions': function_reductions,
        'total_functions_removed': total_functions_removed
    }

def analyze_validation_quality(content_validated_data):
    """検証品質の詳細分析"""
    print(f"\n🎯 変更内容検証品質の詳細:")
    
    match_scores = []
    validation_details = Counter()
    
    for proposal in content_validated_data['data']:
        for func in proposal.get('detected_functions', []):
            if 'content_validation' in func:
                validation = func['content_validation']
                score = validation.get('content_match_score', 0.0)
                match_scores.append(score)
                
                status = validation.get('validation_status', 'unknown')
                validation_details[status] += 1
    
    if match_scores:
        avg_score = sum(match_scores) / len(match_scores)
        high_quality = sum(1 for score in match_scores if score >= 0.8)
        medium_quality = sum(1 for score in match_scores if 0.5 <= score < 0.8)
        low_quality = sum(1 for score in match_scores if score < 0.5)
        
        print(f"├─ 平均一致スコア: {avg_score:.3f}")
        print(f"├─ 高品質関数 (≥0.8): {high_quality}")
        print(f"├─ 中品質関数 (0.5-0.8): {medium_quality}")
        print(f"├─ 低品質関数 (<0.5): {low_quality}")
        print(f"└─ 総検証済み関数: {len(match_scores)}")
    
    return {
        'avg_score': avg_score if match_scores else 0,
        'match_scores': match_scores,
        'validation_details': validation_details
    }

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
        'validation_impact': {
            'removed_proposals_count': len(analysis_results['comparison']['removed_proposals']),
            'removed_proposals': list(analysis_results['comparison']['removed_proposals']),
            'total_functions_removed': analysis_results['comparison']['total_functions_removed'],
            'function_reductions_count': len(analysis_results['comparison']['function_reductions'])
        },
        'validation_quality': analysis_results['quality']
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"💾 比較レポートを保存: {output_path}")

def main():
    """メイン処理"""
    print("🔍 content_validated vs merged_only 比較開始")
    
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
    
    # 各版の詳細分析
    merged_only_analysis = analyze_ground_truth_quality(merged_only_data, "merged_only")
    content_validated_analysis = analyze_ground_truth_quality(content_validated_data, "content_validated")
    
    # 変更内容検証の影響分析
    comparison_results = compare_ground_truth_impact(merged_only_analysis, content_validated_analysis)
    
    # 検証品質の詳細分析
    quality_analysis = analyze_validation_quality(content_validated_analysis)
    
    # 結果をまとめてレポート保存
    analysis_results = {
        'merged_only': merged_only_analysis,
        'content_validated': content_validated_analysis,
        'comparison': comparison_results,
        'quality': quality_analysis
    }
    
    output_path = "../data/ground_truth/content_validation_impact_report.json"
    save_comparison_report(analysis_results, output_path)
    
    print(f"\n✅ 変更内容検証の影響分析完了！")

if __name__ == "__main__":
    main()
