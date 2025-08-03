#!/usr/bin/env python3
"""
Content-validated Ground Truthに含まれる提案ファイルをコピーするスクリプト
accepted_proposals_ground_truth_content_validated.jsonに含まれる提案IDに対応する
.mdファイルをcleaned_evaluable_proposals_content_validated/ディレクトリにコピーする
"""

import json
import os
import shutil
from pathlib import Path

def load_content_validated_ground_truth():
    """Content-validated Ground Truthデータを読み込み"""
    gt_path = "../data/ground_truth/accepted_proposals_ground_truth_content_validated.json"
    
    if not os.path.exists(gt_path):
        print(f"❌ Ground Truthファイルが見つかりません: {gt_path}")
        return None
    
    with open(gt_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # ground_truthキーからデータを取得
    if isinstance(data, dict) and 'ground_truth' in data:
        return data['ground_truth']
    elif isinstance(data, list):
        return data
    else:
        print(f"❌ 不明なデータ形式: {gt_path}")
        return None

def extract_proposal_ids(ground_truth_data):
    """Ground TruthからプロポーザルIDのセットを抽出"""
    proposal_ids = set()
    
    for entry in ground_truth_data:
        proposal_id = entry.get('proposal_id')
        if proposal_id:
            proposal_ids.add(proposal_id)
    
    return proposal_ids

def copy_proposal_files(proposal_ids, source_dir, target_dir):
    """指定されたプロポーザルIDに対応するファイルをコピー"""
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # ターゲットディレクトリを作成
    target_path.mkdir(parents=True, exist_ok=True)
    
    copied_files = []
    missing_files = []
    
    print(f"📁 ソースディレクトリ: {source_path}")
    print(f"📁 ターゲットディレクトリ: {target_path}")
    print(f"📋 コピー対象: {len(proposal_ids)}個の提案")
    
    for proposal_id in sorted(proposal_ids):
        source_file = source_path / f"{proposal_id}.md"
        target_file = target_path / f"{proposal_id}.md"
        
        if source_file.exists():
            try:
                shutil.copy2(source_file, target_file)
                copied_files.append(proposal_id)
                print(f"✅ コピー完了: {proposal_id}.md")
            except Exception as e:
                print(f"❌ コピー失敗: {proposal_id}.md - {str(e)}")
                missing_files.append(proposal_id)
        else:
            print(f"⚠️  ファイルが見つかりません: {source_file}")
            missing_files.append(proposal_id)
    
    return copied_files, missing_files

def create_summary_report(proposal_ids, copied_files, missing_files, target_dir):
    """コピー結果のサマリーレポートを作成"""
    report = {
        "summary": {
            "total_proposals_in_ground_truth": len(proposal_ids),
            "successfully_copied": len(copied_files),
            "missing_files": len(missing_files),
            "copy_success_rate": len(copied_files) / len(proposal_ids) if proposal_ids else 0
        },
        "copied_proposal_ids": sorted(copied_files),
        "missing_proposal_ids": sorted(missing_files)
    }
    
    # JSONレポートを保存
    report_path = Path(target_dir) / "copy_summary_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    # テキストサマリーも作成
    summary_path = Path(target_dir) / "COPY_SUMMARY.md"
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("# Content-Validated Proposals Copy Summary\n\n")
        f.write(f"## Statistics\n")
        f.write(f"- **Total proposals in ground truth**: {len(proposal_ids)}\n")
        f.write(f"- **Successfully copied**: {len(copied_files)}\n")
        f.write(f"- **Missing files**: {len(missing_files)}\n")
        f.write(f"- **Copy success rate**: {len(copied_files) / len(proposal_ids) * 100:.1f}%\n\n")
        
        if missing_files:
            f.write(f"## Missing Files ({len(missing_files)})\n")
            f.write("The following proposal IDs were in the ground truth but their corresponding .md files were not found:\n\n")
            for proposal_id in sorted(missing_files):
                f.write(f"- {proposal_id}.md\n")
            f.write("\n")
        
        f.write(f"## Successfully Copied Files ({len(copied_files)})\n")
        f.write("The following proposal files were successfully copied:\n\n")
        for i, proposal_id in enumerate(sorted(copied_files), 1):
            f.write(f"{i:3d}. {proposal_id}.md\n")
    
    print(f"📊 サマリーレポートを保存: {report_path}")
    print(f"📋 テキストサマリーを保存: {summary_path}")
    
    return report

def main():
    """メイン処理"""
    print("🚀 Content-validated提案ファイルのコピー開始")
    
    # Ground Truthデータを読み込み
    print("📖 Ground Truthデータを読み込み中...")
    ground_truth_data = load_content_validated_ground_truth()
    
    if not ground_truth_data:
        print("❌ Ground Truthデータの読み込みに失敗しました")
        return
    
    # プロポーザルIDを抽出
    proposal_ids = extract_proposal_ids(ground_truth_data)
    print(f"✅ {len(proposal_ids)}個のプロポーザルIDを抽出しました")
    
    # ファイルをコピー
    source_dir = "../data/preprocess/accepted_proposals/cleaned_evaluable_proposals"
    target_dir = "../data/preprocess/accepted_proposals/cleaned_evaluable_proposals_content_validated"
    
    print(f"\n📁 ファイルコピー実行中...")
    copied_files, missing_files = copy_proposal_files(proposal_ids, source_dir, target_dir)
    
    # サマリーレポートを作成
    print(f"\n📊 結果サマリー:")
    print(f"├─ 対象提案数: {len(proposal_ids)}")
    print(f"├─ コピー成功: {len(copied_files)}")
    print(f"├─ ファイル未発見: {len(missing_files)}")
    print(f"└─ 成功率: {len(copied_files) / len(proposal_ids) * 100:.1f}%")
    
    if missing_files:
        print(f"\n⚠️  未発見ファイル:")
        for proposal_id in sorted(missing_files)[:10]:  # 最初の10件のみ表示
            print(f"   └─ {proposal_id}.md")
        if len(missing_files) > 10:
            print(f"   └─ ... その他 {len(missing_files) - 10} 件")
    
    # レポート作成
    report = create_summary_report(proposal_ids, copied_files, missing_files, target_dir)
    
    print(f"\n✅ コピー処理完了！")
    print(f"📁 コピー先: {target_dir}")

if __name__ == "__main__":
    main()
