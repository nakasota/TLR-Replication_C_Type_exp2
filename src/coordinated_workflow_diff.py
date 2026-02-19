#!/usr/bin/env python3
"""
差分開発実験用ワークフロー: 仕様の一節2つ（ベース・変更後）から変更箇所のトレーサビリティリンクを生成する。

Input: data/docs_diff/{DOCS_DIFF_SET}/sample_pair_*/ 内の各ペア (base.md, changed.md)
Output: 変更されたディレクトリ・ファイル・関数を特定
"""

import csv
import os
import re
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parent))
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')

# Import phase runners and integration from coordinated_workflow
from coordinated_workflow import (
    run_granularity_decision,
    run_directory_level_localization,
    run_file_level_localization,
    run_file_level_link_decision,
    run_function_level_localization,
    run_function_level_link_decision,
    create_integrated_results,
)


def print_phase_header(phase_num, phase_name, step_num=None, step_name=None):
    """Print a formatted phase/step header."""
    print("=" * 70)
    if step_num is not None:
        print(f"PHASE {phase_num} - {phase_name} | STEP {step_num}: {step_name}")
    else:
        print(f"PHASE {phase_num}: {phase_name}")
    print("=" * 70)


def print_progress(message):
    """Print a progress message with timestamp."""
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"[{timestamp}] {message}")


def print_phase_progress(current, total, item_name="items"):
    """Print phase progress with percentage."""
    if total > 0:
        percentage = (current / total) * 100
        print_progress(f"Progress: {current}/{total} {item_name} ({percentage:.1f}%)")


def main():
    """Run the diff workflow for change-driven traceability (data/docs_diff/{DOCS_DIFF_SET}/) and repo (data/repos/{REPO_SET})."""
    project_root = Path(__file__).resolve().parent.parent
    docs_diff_base = project_root / "data" / "docs_diff"
    repos_base = project_root / "data" / "repos"

    print_progress("Starting diff experiment: change-driven traceability link workflow")

    # DOCS_DIFF_SET: which diff pair set (data/docs_diff/{DOCS_DIFF_SET}/)
    docs_diff_set = os.environ.get("DOCS_DIFF_SET", "").strip()
    # Only list dirs that contain at least one pair (subdir with base.md + changed.md)
    available_diff_sets = []
    if docs_diff_base.exists():
        for d in docs_diff_base.iterdir():
            if d.is_dir():
                for sub in d.iterdir():
                    if sub.is_dir() and (sub / "base.md").exists() and (sub / "changed.md").exists():
                        available_diff_sets.append(d.name)
                        break
        available_diff_sets = sorted(set(available_diff_sets))
    default_diff = "sample_doc_diff" if "sample_doc_diff" in available_diff_sets else (available_diff_sets[0] if available_diff_sets else "sample_doc_diff")
    if not docs_diff_set:
        if available_diff_sets:
            print(f"\nAvailable diff pair sets (data/docs_diff/): {available_diff_sets}")
        try:
            docs_diff_set = input(f"Diff pair set (DOCS_DIFF_SET) [default: {default_diff}]: ").strip() or default_diff
        except (EOFError, KeyboardInterrupt):
            docs_diff_set = default_diff
            print(f"Using default diff pair set: {docs_diff_set}")
    docs_diff_dir = docs_diff_base / docs_diff_set
    if not docs_diff_dir.exists() or not docs_diff_dir.is_dir():
        print(f"Error: Diff pair set not found: {docs_diff_dir}", file=sys.stderr)
        sys.exit(1)

    # REPO_SET: which repository (data/repos/{REPO_SET})
    repo_set = os.environ.get("REPO_SET", "").strip()
    available_repos = sorted([d.name for d in repos_base.iterdir() if d.is_dir()]) if repos_base.exists() else []
    default_repo = "sample_repo" if "sample_repo" in available_repos else (available_repos[0] if available_repos else "sample_repo")
    if not repo_set:
        if available_repos:
            print(f"Available repositories (data/repos/): {available_repos}")
        try:
            repo_set = input(f"Repository (REPO_SET) [default: {default_repo}]: ").strip() or default_repo
        except (EOFError, KeyboardInterrupt):
            repo_set = default_repo
            print(f"Using default repository: {repo_set}")
    repo_dir = repos_base / repo_set
    if not repo_dir.exists() or not repo_dir.is_dir():
        print(f"Error: Repository not found: {repo_dir}", file=sys.stderr)
        sys.exit(1)

    print_progress(f"Using diff pairs: data/docs_diff/{docs_diff_set}  repository: data/repos/{repo_set}")

    # Load pairs from data/docs_diff/{DOCS_DIFF_SET}/ 内の base.md + changed.md を持つサブディレクトリ
    # 自然順ソート: pair_1, pair_2, ..., pair_10（任意のディレクトリ名に対応）
    def _natural_sort_key(p):
        name = p.name if hasattr(p, "name") else str(p)
        return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", name)]

    pair_dirs = [d for d in docs_diff_dir.iterdir() if d.is_dir() and (d / "base.md").exists() and (d / "changed.md").exists()]
    pairs = [(d.name, d) for d in sorted(pair_dirs, key=_natural_sort_key)]

    if not pairs:
        print(f"Error: No (base.md, changed.md) pairs found in {docs_diff_dir}", file=sys.stderr)
        sys.exit(1)

    # Structure type: full, 500, 1000, 2000 (aligned with coordinated_workflow)
    valid_types = ("full", "500", "1000", "2000")
    structure_type = os.environ.get("REPOSITORY_STRUCTURE_TYPE", "").strip().lower()
    if structure_type not in valid_types:
        print("Repository structure type (prompt size): full, 500, 1000, 2000")
        try:
            structure_type = input("Structure type [default: 2000]: ").strip().lower() or "2000"
        except (EOFError, KeyboardInterrupt):
            structure_type = "2000"
        if structure_type not in valid_types:
            structure_type = "2000"
    print_progress(f"Repository structure: repository_structure_{structure_type}_{repo_set}")

    # Batch size and start from (aligned with coordinated_workflow)
    batch_size = os.environ.get("BATCH_SIZE", "").strip()
    start_from = os.environ.get("START_FROM", "").strip()
    if not batch_size or not start_from:
        print("Select number of pairs to process:")
        print("  - Enter a number (e.g., 3, 5) or 'all' for all")
        try:
            batch_size = (batch_size or input("Batch size [default: all]: ").strip()) or "all"
            print("Start from index (0-based). Press Enter for 0.")
            start_from = (start_from or input("Start from index [default: 0]: ").strip()) or "0"
        except (EOFError, KeyboardInterrupt):
            batch_size = "all"
            start_from = "0"
            print(f"Using default: batch_size={batch_size}, start_from={start_from}")

    if batch_size.lower() != "all":
        try:
            n = int(batch_size)
            batch_size = str(n) if n >= 1 else "all"
        except ValueError:
            batch_size = "all"
    if not start_from:
        start_from = "0"
    try:
        start_from_int = max(0, int(start_from))
    except ValueError:
        start_from_int = 0

    if batch_size.lower() == "all":
        max_pairs = len(pairs) - start_from_int
    else:
        max_pairs = min(int(batch_size), len(pairs) - start_from_int)
        if max_pairs < 1:
            max_pairs = len(pairs) - start_from_int

    # workflow_env for all phase subprocesses (coordinated_workflow.py と同様)
    repository_structure = f"repository_structure_{structure_type}_{repo_set}"
    workflow_env = os.environ.copy()
    workflow_env["DOCS_DIFF_SET"] = docs_diff_set
    workflow_env["REPO_SET"] = repo_set
    workflow_env["C_REPO_ROOT"] = str(repo_dir)
    workflow_env["REPOSITORY_STRUCTURE"] = repository_structure
    workflow_env["BATCH_SIZE"] = batch_size
    workflow_env["START_FROM"] = str(start_from_int)

    # repo_structure_{repo_set}.json がなければ自動作成
    repo_structure_json = project_root / "data" / "preprocess" / f"repo_structure_{repo_set}.json"
    if not repo_structure_json.exists():
        print_progress(f"Generating repo_structure_{repo_set}.json from: {repo_dir}")
        create_repo_script = Path(__file__).parent / "directory_and_file_level_localization" / "create_c_repo_structure.py"
        result = subprocess.run(
            [sys.executable, str(create_repo_script), str(repo_dir), "-o", str(repo_structure_json)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"Error: Failed to create repo structure: {result.stderr}", file=sys.stderr)
            sys.exit(1)
        print_progress(f"Created {repo_structure_json}")

    print_phase_header("DIFF", "Change-driven Traceability Link Generation")
    print_progress(f"Processing {max_pairs} pair(s) starting from index {start_from_int}")

    # Phase 0: Granularity Decision (diff mode via DOCS_DIFF_SET)
    granularity_results, granularity_output_dir = run_granularity_decision(batch_size, str(start_from_int), workflow_env)

    # Phase 1: Localization
    directory_output_dir = run_directory_level_localization(granularity_results, repository_structure, workflow_env)
    file_output_dir = run_file_level_localization(granularity_results, repository_structure, workflow_env)

    # Phase 1 Step 3: File Level Link Decision
    file_link_decision_output_dir = None
    if file_output_dir:
        file_link_decision_output_dir = run_file_level_link_decision(granularity_results, file_output_dir, workflow_env)

    # Phase 1 Step 4: Function Level Localization
    function_output_dir = None
    if file_output_dir:
        function_output_dir = run_function_level_localization(granularity_results, file_output_dir, workflow_env)

    # Phase 2: Function Level Link Decision
    function_link_decision_output_dir = run_function_level_link_decision(granularity_results, function_output_dir, workflow_env)

    # Create integrated results (output to output_diff/)
    output_diff_root = Path(__file__).parent / "output_diff"
    integrated_output_dir = create_integrated_results(
        granularity_results, granularity_output_dir, directory_output_dir, file_output_dir,
        file_link_decision_output_dir, function_output_dir, function_link_decision_output_dir,
        batch_size, repo_set, output_root=output_diff_root
    )

    # Summary (coordinated_workflow.py と同様)
    print("=" * 70)
    print("WORKFLOW COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("Output directory:")
    print(f"  Integrated Results: {integrated_output_dir}")
    print(f"    - JSON: {integrated_output_dir / 'integrated_results.json'}")
    print(f"    - Summary: {integrated_output_dir / 'summary_report.txt'}")
    csv_files = list(integrated_output_dir.glob('results_summary_*.csv'))
    if csv_files:
        print(f"    - CSV: {csv_files[0]}")
    print("")
    dir_count = sum(1 for g in granularity_results.values() if g == "directory")
    file_count = sum(1 for g in granularity_results.values() if g == "file")
    fn_count = sum(1 for g in granularity_results.values() if g == "function")
    print("Final Statistics:")
    print(f"  Batch size: {batch_size}, Total: {len(granularity_results)} pairs")
    print(f"  Directory: {dir_count}, File: {file_count}, Function: {fn_count}")
    print("=" * 70)


if __name__ == "__main__":
    main()
