#!/usr/bin/env python3
"""
cleaned_evaluable_proposals_for_embeddingとcleaned_evaluable_proposals_content_validatedの
ファイル名重複確認スクリプト
"""

import os
from pathlib import Path
import json

def get_files_in_directory(directory_path):
    """指定されたディレクトリ内の.mdファイルの一覧を取得"""
    dir_path = Path(directory_path)
    
    if not dir_path.exists():
        print(f"❌ ディレクトリが存在しません: {directory_path}")
        return set(), []
    
    md_files = list(dir_path.glob("*.md"))
    file_names = {f.stem for f in md_files}  # 拡張子なしのファイル名
    
    return file_names, [f.name for f in md_files]

def analyze_overlap(dir1_path, dir2_path):
    """2つのディレクトリ間のファイル重複を分析"""
    print(f"🔍 ファイル重複分析開始")
    print(f"📁 ディレクトリ1: {dir1_path}")
    print(f"📁 ディレクトリ2: {dir2_path}")
    
    # 各ディレクトリのファイルを取得
    files1, file_list1 = get_files_in_directory(dir1_path)
    files2, file_list2 = get_files_in_directory(dir2_path)
    
    if not files1 and not files2:
        print("❌ 両方のディレクトリにファイルが見つかりません")
        return
    
    print(f"\n📊 基本統計:")
    print(f"├─ {Path(dir1_path).name}: {len(files1)}ファイル")
    print(f"└─ {Path(dir2_path).name}: {len(files2)}ファイル")
    
    # 重複分析
    common_files = files1 & files2  # 両方に存在
    only_in_dir1 = files1 - files2  # dir1のみに存在
    only_in_dir2 = files2 - files1  # dir2のみに存在
    
    print(f"\n🔍 重複分析結果:")
    print(f"├─ 共通ファイル: {len(common_files)}")
    print(f"├─ {Path(dir1_path).name}のみ: {len(only_in_dir1)}")
    print(f"└─ {Path(dir2_path).name}のみ: {len(only_in_dir2)}")
    
    # 重複率計算
    if files1 or files2:
        total_unique = len(files1 | files2)
        overlap_rate_dir1 = (len(common_files) / len(files1) * 100) if files1 else 0
        overlap_rate_dir2 = (len(common_files) / len(files2) * 100) if files2 else 0
        
        print(f"\n📈 重複率:")
        print(f"├─ {Path(dir1_path).name}に対する重複率: {overlap_rate_dir1:.1f}% ({len(common_files)}/{len(files1)})")
        print(f"├─ {Path(dir2_path).name}に対する重複率: {overlap_rate_dir2:.1f}% ({len(common_files)}/{len(files2)})")
        print(f"└─ 総ユニークファイル数: {total_unique}")
    
    # 詳細レポート
    if common_files:
        print(f"\n📋 共通ファイル（最初の20件）:")
        for i, file_name in enumerate(sorted(common_files)[:20], 1):
            print(f"   {i:2d}. {file_name}.md")
        if len(common_files) > 20:
            print(f"   ... 他 {len(common_files) - 20} 件")
    
    if only_in_dir1:
        print(f"\n📋 {Path(dir1_path).name}のみに存在（最初の10件）:")
        for i, file_name in enumerate(sorted(only_in_dir1)[:10], 1):
            print(f"   {i:2d}. {file_name}.md")
        if len(only_in_dir1) > 10:
            print(f"   ... 他 {len(only_in_dir1) - 10} 件")
    
    if only_in_dir2:
        print(f"\n📋 {Path(dir2_path).name}のみに存在（最初の10件）:")
        for i, file_name in enumerate(sorted(only_in_dir2)[:10], 1):
            print(f"   {i:2d}. {file_name}.md")
        if len(only_in_dir2) > 10:
            print(f"   ... 他 {len(only_in_dir2) - 10} 件")
    
    return {
        'dir1_name': Path(dir1_path).name,
        'dir2_name': Path(dir2_path).name,
        'dir1_count': len(files1),
        'dir2_count': len(files2),
        'common_count': len(common_files),
        'only_dir1_count': len(only_in_dir1),
        'only_dir2_count': len(only_in_dir2),
        'total_unique': len(files1 | files2),
        'overlap_rate_dir1': overlap_rate_dir1 if 'overlap_rate_dir1' in locals() else 0,
        'overlap_rate_dir2': overlap_rate_dir2 if 'overlap_rate_dir2' in locals() else 0,
        'common_files': sorted(common_files),
        'only_in_dir1': sorted(only_in_dir1),
        'only_in_dir2': sorted(only_in_dir2)
    }

def save_analysis_report(analysis_result, output_path):
    """分析結果をJSONファイルに保存"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(analysis_result, f, ensure_ascii=False, indent=2)
    print(f"💾 分析レポートを保存: {output_path}")

def main():
    """メイン処理"""
    print("🔍 ディレクトリ間ファイル重複分析開始")
    
    # ディレクトリパスを設定
    dir1_path = "../data/preprocess/accepted_proposals/cleaned_evaluable_proposals_for_embedding"
    dir2_path = "../data/preprocess/accepted_proposals/cleaned_evaluable_proposals_content_validated"
    
    # 重複分析実行
    analysis_result = analyze_overlap(dir1_path, dir2_path)
    
    if analysis_result:
        # 結果をファイルに保存
        output_path = "../data/preprocess/accepted_proposals/directory_overlap_analysis.json"
        save_analysis_report(analysis_result, output_path)
        
        print(f"\n✅ 分析完了！")
        
        # サマリー表示
        print(f"\n📝 サマリー:")
        print(f"├─ {analysis_result['dir1_name']}: {analysis_result['dir1_count']}ファイル")
        print(f"├─ {analysis_result['dir2_name']}: {analysis_result['dir2_count']}ファイル")
        print(f"├─ 共通: {analysis_result['common_count']}ファイル")
        print(f"├─ 重複率（for_embedding基準): {analysis_result['overlap_rate_dir1']:.1f}%")
        print(f"├─ 重複率（content_validated基準): {analysis_result['overlap_rate_dir2']:.1f}%")
        print(f"└─ 総ユニーク: {analysis_result['total_unique']}ファイル")

if __name__ == "__main__":
    main()
