#!/usr/bin/env python3
"""
差分開発実験用ワークフロー: 仕様の一節2つ（ベース・変更後）から変更箇所のトレーサビリティリンクを生成する。

Input: data/docs_diff/{DOCS_DIFF_SET}/sample_pair_*/ 内の各ペア (base.md, changed.md)
Output: 変更されたディレクトリ・ファイル・関数を特定

coordinated_workflow.py に揃えた対話選択（DOCS_DIFF_SET, REPO_SET, 構造タイプ, バッチサイズ等）に対応。
本スクリプトは追加実験用。既存の coordinated_workflow.py（仕様1節→成果物リンク）は別途共有済み。
"""

import os
import re
import sys
import json
import subprocess
import time
import random
import requests
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parent))
from llm_client import get_llm_config, build_chat_payload

# Diff prompt imports
sys.path.append(str(Path(__file__).parent / 'granularity_decision' / 'prompt'))
from granularity_decision_prompt import generate_granularity_decision_diff_prompt

sys.path.append(str(Path(__file__).parent / 'directory_level_localization' / 'prompt'))
from directory_level_localization import generate_directory_level_localization_diff_prompt

sys.path.append(str(Path(__file__).parent / 'directory_and_file_level_localization' / 'prompt'))
from directory_and_file_level_localization import generate_directory_and_file_level_diff_prompt

sys.path.append(str(Path(__file__).parent / 'file_level_link_decision' / 'prompt'))
from file_level_prompt import generate_file_level_link_decision_diff_prompt

sys.path.append(str(Path(__file__).parent / 'function_level_localization' / 'prompt'))
from function_level_localization import extract_c_skeleton, generate_function_level_localization_diff_prompt

sys.path.append(str(Path(__file__).parent / 'function_level_link_decision' / 'prompt'))
from link_decision_prompt import generate_link_decision_diff_prompt
from link_decision_analyzer import analyze_function_relevance

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')


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


def make_api_request_with_retry(api_url, headers, payload, max_retries=3, base_delay=2):
    """Execute API request with retries."""
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)
            if response.status_code == 200:
                return True, response.json(), None
            elif response.status_code == 429:
                if attempt < max_retries:
                    time.sleep(base_delay * (2 ** attempt) + random.uniform(0, 1))
                    continue
            else:
                if attempt < max_retries:
                    time.sleep(base_delay * (2 ** attempt))
                    continue
        except requests.exceptions.SSLError:
            if attempt < max_retries:
                time.sleep(base_delay * (2 ** attempt) + random.uniform(0, 1))
                continue
        except requests.exceptions.ConnectionError:
            if attempt < max_retries:
                time.sleep(base_delay * (2 ** attempt) + random.uniform(0, 1))
                continue
        except requests.exceptions.Timeout:
            if attempt < max_retries:
                time.sleep(base_delay * (2 ** attempt))
                continue
        except Exception:
            if attempt < max_retries:
                time.sleep(base_delay * (2 ** attempt))
                continue
    return False, None, "Failed after retries"


def load_repo_structure(repo_set):
    """Load C repository structure (repo_structure_{repo_set}.json)."""
    repo_structure_path = Path(__file__).resolve().parent.parent / 'data' / 'preprocess' / f'repo_structure_{repo_set}.json'
    with open(repo_structure_path, 'r') as f:
        return json.load(f)


def get_simplified_repo_structure(repo_set, structure_type="2000"):
    """Get or create simplified repo structure for prompts. structure_type: full, 500, 1000, 2000."""
    structure_dir = Path(__file__).parent / 'directory_and_file_level_localization' / 'prompt'
    structure_name = f'repository_structure_{structure_type}_{repo_set}'
    structure_path = structure_dir / structure_name

    if not structure_path.exists():
        print_progress(f"Generating repository structure: {structure_name}...")
        create_script = Path(__file__).parent / 'directory_and_file_level_localization' / 'create_simplified_repo_structure.py'
        env = os.environ.copy()
        env['REPO_SET'] = repo_set
        subprocess.run(
            [sys.executable, str(create_script), '--output', structure_name],
            cwd=Path(__file__).parent / 'directory_and_file_level_localization',
            env=env,
            capture_output=True,
            check=True,
        )

    structure_files = sorted(structure_path.glob('simplified_repo_structure_separate*.txt'))
    if not structure_files:
        raise FileNotFoundError(f"No structure files in {structure_path}")

    chunks = []
    for sf in structure_files:
        with open(sf, 'r') as f:
            chunks.append(f.read())
    return chunks


def _parse_json_response(content):
    """Parse LLM JSON response, stripping markdown code blocks."""
    for prefix in ('```json', '```'):
        if content.startswith(prefix):
            content = content[len(prefix):].strip()
    if content.endswith('```'):
        content = content[:-3].strip()
    return json.loads(content)


def run_diff_workflow_for_pair(pair_name, base_text, changed_text, repo_set, structure_type, api_url, headers, model_for_payload, pair_idx=None, total_pairs=None):
    """Run the full diff workflow for one (base, changed) spec pair. Branches by granularity."""
    result = {
        "pair": pair_name, "granularity": None,
        "found_directories": [], "found_files": [], "found_functions": [],
        "final_directory": None, "final_files": [], "final_function": None
    }

    if pair_idx is not None and total_pairs is not None:
        print_phase_progress(pair_idx + 1, total_pairs, "pairs")
    print_progress(f"Processing pair: {pair_name}")

    # Phase 0: Granularity decision
    print_progress("Phase 0: Granularity decision...")
    prompt = generate_granularity_decision_diff_prompt(base_text, changed_text)
    payload = build_chat_payload([{"role": "user", "content": prompt}], temperature=0.0, model_for_payload=model_for_payload)
    success, resp, _ = make_api_request_with_retry(api_url, headers, payload)
    if success:
        content = resp['choices'][0]['message']['content'].strip().lower()
        result["granularity"] = content if content in ("directory", "file", "function") else "function"
    else:
        result["granularity"] = "function"
    time.sleep(1)

    structure_chunks = get_simplified_repo_structure(repo_set, structure_type)

    if result["granularity"] == "directory":
        # Directory granularity: directory_level_localization only
        print_progress(f"Phase 1: Directory level localization (granularity=directory)...")
        all_found_dirs = set()
        for chunk_idx, chunk in enumerate(structure_chunks):
            print_progress(f"  Directory localization: chunk {chunk_idx + 1}/{len(structure_chunks)}")
            prompt = generate_directory_level_localization_diff_prompt(base_text, changed_text, chunk)
            payload = build_chat_payload([{"role": "user", "content": prompt}], temperature=0.0, model_for_payload=model_for_payload)
            success, resp, _ = make_api_request_with_retry(api_url, headers, payload)
            if success:
                try:
                    parsed = _parse_json_response(resp['choices'][0]['message']['content'])
                    all_found_dirs.update(parsed.get('found_directories', []))
                except Exception:
                    pass
            time.sleep(1)
        result["found_directories"] = list(all_found_dirs)
        if result["found_directories"]:
            result["final_directory"] = result["found_directories"][0]
        print_progress(f"  Found {len(result['found_directories'])} directories")
        return result

    # File or function granularity: directory_and_file_level_localization
    print_progress(f"Phase 1: Directory and file level localization (granularity={result['granularity']})...")
    all_found_files = set()
    for chunk_idx, chunk in enumerate(structure_chunks):
        print_progress(f"  File localization: chunk {chunk_idx + 1}/{len(structure_chunks)}")
        prompt = generate_directory_and_file_level_diff_prompt(base_text, changed_text, chunk)
        payload = build_chat_payload([{"role": "user", "content": prompt}], temperature=0.0, model_for_payload=model_for_payload)
        success, resp, _ = make_api_request_with_retry(api_url, headers, payload)
        if success:
            try:
                parsed = _parse_json_response(resp['choices'][0]['message']['content'])
                all_found_files.update(parsed.get('found_files', []))
            except Exception:
                pass
        time.sleep(1)

    result["found_files"] = [f for f in all_found_files if f.endswith('.c') or f.endswith('.h')]
    print_progress(f"  Found {len(result['found_files'])} files")
    if not result["found_files"]:
        return result

    if result["granularity"] == "file":
        # File granularity: file_level_link_decision
        print_progress("Phase 2: File level link decision...")
        for file_path in result["found_files"][:10]:
            skeleton = extract_c_skeleton(file_path)
            if not skeleton:
                continue
            prompt = generate_file_level_link_decision_diff_prompt(base_text, changed_text, file_path, skeleton)
            payload = build_chat_payload([{"role": "user", "content": prompt}], temperature=0.0, model_for_payload=model_for_payload)
            success, resp, _ = make_api_request_with_retry(api_url, headers, payload)
            if success:
                content = resp['choices'][0]['message']['content'].strip().upper()
                if content.startswith("YES"):
                    result["final_files"].append({"file_path": file_path})
                    break
            time.sleep(1)
        if not result["final_files"] and result["found_files"]:
            result["final_files"] = [{"file_path": result["found_files"][0]}]
        return result

    # Function granularity: function_level_localization → function_level_link_decision
    print_progress("Phase 2: Function level localization...")
    for file_path in result["found_files"][:10]:
        skeleton = extract_c_skeleton(file_path)
        if not skeleton:
            continue
        directory = str(Path(file_path).parent) if '/' in file_path else '.'
        prompt = generate_function_level_localization_diff_prompt(base_text, changed_text, file_path, directory, skeleton)
        payload = build_chat_payload([{"role": "user", "content": prompt}], temperature=0.0, model_for_payload=model_for_payload)
        success, resp, _ = make_api_request_with_retry(api_url, headers, payload)
        if success:
            try:
                parsed = _parse_json_response(resp['choices'][0]['message']['content'])
                for fn in parsed.get('relevant_functions', []):
                    result["found_functions"].append({"file_path": file_path, "function_name": fn})
            except Exception:
                pass
        time.sleep(1)

    print_progress(f"  Found {len(result['found_functions'])} function candidates")
    print_progress("Phase 3: Function level link decision...")
    for fn_info in result["found_functions"][:5]:
        analysis = analyze_function_relevance(fn_info["file_path"], fn_info["function_name"])
        if not analysis:
            continue
        function_code = analysis.get("function_code", "")
        prompt = generate_link_decision_diff_prompt(
            base_text, changed_text,
            fn_info["file_path"], fn_info["function_name"],
            function_code
        )
        payload = build_chat_payload([{"role": "user", "content": prompt}], temperature=0.0, model_for_payload=model_for_payload)
        success, resp, _ = make_api_request_with_retry(api_url, headers, payload)
        if success:
            content = resp['choices'][0]['message']['content'].strip().upper()
            if content.startswith("YES"):
                result["final_function"] = fn_info
                break
        time.sleep(1)

    if not result["final_function"] and result["found_functions"]:
        result["final_function"] = result["found_functions"][0]

    return result


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

    pairs_to_process = pairs[start_from_int:start_from_int + max_pairs]

    try:
        API_URL, headers, model_for_payload = get_llm_config()
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    os.environ["REPO_SET"] = repo_set  # Required by link_decision_analyzer, function_level_localization
    results = []

    print_phase_header("DIFF", "Change-driven Traceability Link Generation")
    print_progress(f"Processing {len(pairs_to_process)} pair(s) starting from index {start_from_int}")

    for pair_idx, (pair_name, pair_dir) in enumerate(pairs_to_process):
        with open(pair_dir / "base.md", "r", encoding="utf-8") as f:
            base_text = f.read()
        with open(pair_dir / "changed.md", "r", encoding="utf-8") as f:
            changed_text = f.read()

        result = run_diff_workflow_for_pair(
            pair_name, base_text, changed_text, repo_set, structure_type,
            API_URL, headers, model_for_payload,
            pair_idx=pair_idx, total_pairs=len(pairs_to_process)
        )
        results.append(result)

        g = result["granularity"]
        if g == "directory" and result.get("final_directory"):
            print_progress(f"  → Found (directory): {result['final_directory']}")
        elif g == "file" and result.get("final_files"):
            print_progress(f"  → Found (file): {result['final_files'][0]['file_path']}")
        elif g == "function" and result.get("final_function"):
            fn = result["final_function"]
            print_progress(f"  → Found (function): {fn['file_path']}:{fn['function_name']}")
        else:
            print_progress(f"  → No match. granularity={g}, found: {result.get('found_directories') or result.get('found_files', [])[:3]}...")

    # Output
    print_phase_header("FINAL", "RESULT INTEGRATION")
    output_root = Path(__file__).parent / "output_diff"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = output_root / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)

    output_json = output_dir / "diff_results.json"
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump({"pairs": results, "timestamp": timestamp}, f, indent=2, ensure_ascii=False)

    print_progress("Creating integrated results from all phases...")
    print_progress(f"Created output directory: {output_dir}")
    print_progress(f"Integrated results saved to: {output_json}")

    # Summary
    print("=" * 70)
    print("WORKFLOW COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("Output directory:")
    print(f"  Integrated Results: {output_dir}")
    print(f"    - JSON: {output_json}")
    print("")
    print("Phase outputs by pair:")
    print("-" * 70)
    for r in results:
        pair = r["pair"]
        g = r["granularity"]
        print(f"\n{pair} (granularity={g}):")
        print(f"  Phase 0 (Granularity Decision): decided_granularity = {g}")
        if g == "directory":
            fd = r.get("found_directories", [])
            print(f"  Phase 1 (Directory Level Localization): found_directories = {fd}")
            print(f"  Final: final_directory = {r.get('final_directory', 'N/A')}")
        elif g == "file":
            ff = r.get("found_files", [])
            print(f"  Phase 1 (Directory and File Level): found_files = {ff}")
            final_f = r.get("final_files", [])
            print(f"  Phase 2 (File Level Link Decision): final_files = {[x.get('file_path') for x in final_f]}")
        elif g == "function":
            ff = r.get("found_files", [])
            print(f"  Phase 1 (Directory and File Level): found_files = {ff}")
            fn_list = r.get("found_functions", [])
            fn_str = [f"{x['file_path']}:{x['function_name']}" for x in fn_list[:5]]
            if len(fn_list) > 5:
                fn_str.append(f"... and {len(fn_list) - 5} more")
            print(f"  Phase 2 (Function Level Localization): found_functions = {fn_str}")
            fn_final = r.get("final_function")
            fn_final_str = f"{fn_final['file_path']}:{fn_final['function_name']}" if fn_final else "N/A"
            print(f"  Phase 3 (Function Level Link Decision): final_function = {fn_final_str}")
    print("")
    print("-" * 70)
    print("Final Statistics:")
    print(f"  Batch size: {len(pairs_to_process)}, Total: {len(results)} pairs")
    dir_count = sum(1 for r in results if r.get("final_directory"))
    file_count = sum(1 for r in results if r.get("final_files"))
    fn_count = sum(1 for r in results if r.get("final_function"))
    print(f"  Directory matches: {dir_count}, File matches: {file_count}, Function matches: {fn_count}")
    print("=" * 70)


if __name__ == "__main__":
    main()
