import os
import glob
import json
import sys
from pathlib import Path
from find_relative_func import EnhancedCLAnalyzer
from tqdm import tqdm


def main():
    # ディレクトリと出力ファイルのパス
    proposals_dir = Path("../data/preprocess/accepted_proposals")
    output_json = Path("../data/ground_truth/accepted_proposals_func_analysis.json")

    # .mdファイルをすべて取得
    md_files = sorted(proposals_dir.glob("*.md"))
    print(f"解析対象: {len(md_files)}件のmdファイル")

    analyzer = EnhancedCLAnalyzer()
    all_results = []
    failed_files = []

    for md_file in tqdm(md_files, desc="進捗", unit="file"):
        try:
            result = analyzer.analyze_proposal(str(md_file))
            all_results.append(result)
        except Exception as e:
            print(f"[ERROR] {md_file}: {e}")
            failed_files.append({"file": str(md_file), "error": str(e)})

    # 結果を保存
    output_json.parent.mkdir(parents=True, exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump({
            "results": all_results,
            "failed_files": failed_files
        }, f, ensure_ascii=False, indent=2)
    print(f"\n💾 全結果を保存: {output_json}")
    print(f"失敗: {len(failed_files)}件")

if __name__ == "__main__":
    main() 