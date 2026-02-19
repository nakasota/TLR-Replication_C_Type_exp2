#!/usr/bin/env python3
"""
Coordinated workflow for C design documents: runs all phases based on granularity decisions.

Input: design documents in data/docs/ (e.g. api_logger.md).
Output: integrated_results.json, summary_report.txt, results_summary_*.csv.

Workflow:
  Phase 0: Granularity Decision (granularity_decision) → doc → "directory"|"file"|"function"
  Phase 1: Localization
    Step 1: Directory level (directory granularity only)
    Step 2: Directory and file level (file and function granularity)
    Step 3: File level link decision (file granularity only)
    Step 4: Function level localization (function granularity only)
  Phase 2: Function level link decision (function granularity only)

Granularity mapping:
  - "directory" → directory_level_localization
  - "file" → directory_and_file_level_localization → file_level_link_decision
  - "function" → directory_and_file_level_localization → function_level_localization → function_level_link_decision
"""

import os
import sys
import json
import subprocess
import csv
from pathlib import Path
from datetime import datetime

# Optional: base URL for code links (e.g. GitHub). If unset, CSV "Code Path" uses file path only.
REPO_URL = os.environ.get("REPO_URL", "").rstrip("/")
GITHUB_COMMIT_HASH = os.environ.get("COMMIT_HASH", "")
# Cache for repo structure to avoid loading it multiple times
_repo_structure_cache = {}

def _repo_structure_path(repo_set):
    """Path to repo structure JSON for the given dataset (REPO_SET)."""
    return Path(__file__).resolve().parent.parent / 'data' / 'preprocess' / f'repo_structure_{repo_set}.json'

def load_repo_structure(repo_set):
    """Load C repository structure (data/preprocess/repo_structure_{repo_set}.json) for file/function existence validation."""
    global _repo_structure_cache
    if repo_set not in _repo_structure_cache:
        repo_structure_path = _repo_structure_path(repo_set)
        try:
            with open(repo_structure_path, 'r') as f:
                _repo_structure_cache[repo_set] = json.load(f)
            print_progress(f"Loaded repo structure ({repo_set}) with {len(_repo_structure_cache[repo_set])} files for validation")
        except Exception as e:
            print_progress(f"Warning: Failed to load repo structure for validation: {e}")
            _repo_structure_cache[repo_set] = {}
    return _repo_structure_cache[repo_set]

def file_exists_in_repo(file_path, repo_set):
    """Check if a file exists in the C repository structure (repo_structure_{repo_set}.json)."""
    repo_structure = load_repo_structure(repo_set)
    return str(file_path) in repo_structure

def directory_exists_in_repo(directory_path, repo_set):
    """Check if a directory exists in the C repository structure."""
    repo_structure = load_repo_structure(repo_set)
    dir_path = str(directory_path).rstrip('/')
    
    # Check if any file in repo structure starts with this directory path
    for file_path in repo_structure.keys():
        if file_path.startswith(dir_path + '/') or file_path == dir_path:
            return True
    return False

def function_exists_in_file(file_path, function_name, repo_set):
    """Check if a function exists in a specific file using repo_structure_{repo_set}.json."""
    repo_structure = load_repo_structure(repo_set)
    file_data = repo_structure.get(str(file_path))
    
    if not file_data:
        return False
    
    functions = file_data.get('functions', {})
    declarations = file_data.get('function_declarations', {})
    return function_name in functions or function_name in declarations

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

def run_subprocess_with_progress(command, cwd, env=None, input_text=None):
    """Run subprocess with real-time output display."""
    import subprocess
    import sys
    
    # Use Popen for real-time output
    process = subprocess.Popen(
        command,
        cwd=cwd,
        env=env,
        stdin=subprocess.PIPE if input_text else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        universal_newlines=True
    )
    
    # Send input if provided
    if input_text:
        process.stdin.write(input_text)
        process.stdin.close()
    
    # Read and display output in real-time
    output_lines = []
    while True:
        line = process.stdout.readline()
        if not line:
            break
        output_lines.append(line)
        print(line.rstrip())  # Display in real-time
    
    # Wait for process completion
    return_code = process.wait()
    
    # Return result similar to subprocess.run
    class Result:
        def __init__(self, returncode, stdout):
            self.returncode = returncode
            self.stdout = stdout
    
    return Result(return_code, ''.join(output_lines))

def get_issue_url_from_original_proposal(proposal_name):
    """Return Issue URL for CSV. For C design docs (data/docs/*.md) there is no issue URL; returns N/A."""
    return "N/A"


def generate_code_url(granularity, found_files=None, found_directories=None, final_functions=None, final_files=None):
    """Generate code URL for report. Uses REPO_URL + COMMIT_HASH if set; otherwise path-only."""
    base = f"{REPO_URL}/tree/{GITHUB_COMMIT_HASH}" if (REPO_URL and GITHUB_COMMIT_HASH) else REPO_URL
    if not base:
        base = "path"
    if granularity == "directory" and found_directories and len(found_directories) > 0:
        d = found_directories[0]
        return f"{base}/{d}" if base != "path" else d
    if granularity == "file":
        if final_files and len(final_files) > 0:
            f = final_files[0]
            fp = f.get("file_path", "") if isinstance(f, dict) else f
            return f"{base}/{fp}" if base != "path" else fp
        if found_files and len(found_files) > 0:
            return f"{base}/{found_files[0]}" if base != "path" else found_files[0]
    if granularity == "function":
        if final_functions and len(final_functions) > 0:
            fp = final_functions[0].get("file_path", "")
            return f"{base}/{fp}" if base != "path" else fp
        if found_files and len(found_files) > 0:
            return f"{base}/{found_files[0]}" if base != "path" else found_files[0]
    return base if base != "path" else "."

def extract_document_id(doc_name):
    """Document id from filename (e.g. api_logger.md -> api_logger)."""
    return doc_name.replace(".md", "")


def _code_url_blob(file_path):
    """Code path/URL for a file (CSV/report). Uses REPO_URL + COMMIT_HASH if set; else file path."""
    if REPO_URL and GITHUB_COMMIT_HASH:
        return f"{REPO_URL}/blob/{GITHUB_COMMIT_HASH}/{file_path}"
    return file_path


def _code_url_tree(dir_path):
    """Code path/URL for a directory (CSV/report)."""
    if REPO_URL and GITHUB_COMMIT_HASH:
        return f"{REPO_URL}/tree/{GITHUB_COMMIT_HASH}/{dir_path}"
    return dir_path


def _code_url_fallback():
    return REPO_URL if REPO_URL else "N/A"

def run_granularity_decision(batch_size, start_from=0, workflow_env=None):
    """Run the granularity decision process and return the results. workflow_env: env for DOCS_SET, REPO_SET, etc."""
    print_phase_header(0, "GRANULARITY DECISION")
    print_progress(f"Starting granularity decision with batch size: {batch_size}, start from: {start_from}")

    granularity_dir = Path(__file__).parent / 'granularity_decision'
    print_progress(f"Working directory: {granularity_dir}")

    if batch_size != "all":
        batch_input = f"{batch_size}\n{start_from}\n"
    else:
        batch_input = f"all\n{start_from}\n"

    env = (os.environ.copy() if workflow_env is None else workflow_env.copy())

    print_progress("Executing granularity decision main.py...")
    venv_python = Path(__file__).resolve().parent.parent / 'venv' / 'bin' / 'python'
    python_cmd = str(venv_python) if venv_python.exists() else sys.executable
    result = run_subprocess_with_progress(
        [python_cmd, 'main.py'],
        cwd=granularity_dir,
        env=env,
        input_text=batch_input
    )

    if result.returncode != 0:
        print_progress(f"ERROR: Granularity decision failed with return code {result.returncode}")
        print(f"Output: {result.stdout}")
        sys.exit(1)

    print_progress("Granularity decision completed successfully")
    
    # Find the most recent output
    output_dir = granularity_dir / 'output'
    print_progress(f"Looking for output in: {output_dir}")
    
    try:
        latest_output = max(output_dir.glob('*/granularity_decisions.json'), key=lambda p: p.stat().st_mtime)
        print_progress(f"Found granularity results: {latest_output}")
    except ValueError:
        print_progress("ERROR: No granularity_decisions.json found")
        sys.exit(1)
    
    with open(latest_output, 'r') as f:
        granularity_results = json.load(f)
    
    print_progress(f"Loaded {len(granularity_results)} granularity decisions")
    return granularity_results, latest_output.parent

def run_directory_level_localization(granularity_results, repository_structure="repository_structure_2000", workflow_env=None):
    """Run directory level localization for directory granularity proposals only."""
    print_phase_header(1, "LOCALIZATION", 1, "DIRECTORY LEVEL LOCALIZATION")

    directory_proposals = [proposal for proposal, granularity in granularity_results.items()
                          if granularity == "directory"]

    if not directory_proposals:
        print_progress("No proposals require directory-level localization. Skipping directory_level_localization.")
        return None

    print_progress(f"Processing {len(directory_proposals)} directory granularity proposals: {directory_proposals}")

    directory_dir = Path(__file__).parent / 'directory_level_localization'
    print_progress(f"Working directory: {directory_dir}")

    env = (os.environ.copy() if workflow_env is None else workflow_env.copy())
    env['GRANULARITY_RESULTS'] = json.dumps(granularity_results)
    env['REPOSITORY_STRUCTURE'] = repository_structure
    print_progress(f"Setting environment variables: GRANULARITY_RESULTS, REPOSITORY_STRUCTURE={repository_structure}")
    print_progress("Executing directory_level_localization main.py...")
    result = run_subprocess_with_progress(
        [sys.executable, 'main.py'],
        cwd=directory_dir,
        env=env
    )

    if result.returncode != 0:
        print_progress(f"ERROR: Directory level localization failed with return code {result.returncode}")
        print(f"Output: {result.stdout}")
        sys.exit(1)

    print_progress("Directory level localization completed successfully")
    
    # Find the most recent output
    output_dir = directory_dir / 'output'
    print_progress(f"Looking for output in: {output_dir}")
    
    try:
        latest_output = max(output_dir.glob('*/llm_outputs.json'), key=lambda p: p.stat().st_mtime)
        print_progress(f"Found directory level results: {latest_output}")
    except ValueError:
        print_progress("ERROR: No directory level llm_outputs.json found")
        sys.exit(1)
    
    return latest_output.parent

def run_file_level_localization(granularity_results, repository_structure="repository_structure_2000", workflow_env=None):
    """Run file level localization for file and function granularity proposals."""
    print_phase_header(1, "LOCALIZATION", 2, "DIRECTORY AND FILE LEVEL LOCALIZATION")

    file_function_proposals = [proposal for proposal, granularity in granularity_results.items()
                              if granularity in ["file", "function"]]

    if not file_function_proposals:
        print_progress("No proposals require file-level localization. Skipping directory_and_file_level_localization.")
        return None

    print_progress(f"Processing {len(file_function_proposals)} file/function granularity proposals: {file_function_proposals}")

    directory_file_dir = Path(__file__).parent / 'directory_and_file_level_localization'
    print_progress(f"Working directory: {directory_file_dir}")

    env = (os.environ.copy() if workflow_env is None else workflow_env.copy())
    env['GRANULARITY_RESULTS'] = json.dumps(granularity_results)
    env['REPOSITORY_STRUCTURE'] = repository_structure
    print_progress(f"Setting environment variables: GRANULARITY_RESULTS, REPOSITORY_STRUCTURE={repository_structure}")

    print_progress("Executing directory_and_file_level_localization main.py...")
    result = run_subprocess_with_progress(
        [sys.executable, 'main.py'],
        cwd=directory_file_dir,
        env=env
    )

    if result.returncode != 0:
        print_progress(f"ERROR: File level localization failed with return code {result.returncode}")
        print(f"Output: {result.stdout}")
        sys.exit(1)

    print_progress("File level localization completed successfully")
    
    # Find the most recent output
    output_dir = directory_file_dir / 'output'
    print_progress(f"Looking for output in: {output_dir}")
    
    try:
        latest_output = max(output_dir.glob('*/llm_outputs.json'), key=lambda p: p.stat().st_mtime)
        print_progress(f"Found file level results: {latest_output}")
    except ValueError:
        print_progress("ERROR: No file level llm_outputs.json found")
        sys.exit(1)
    
    return latest_output.parent

def run_function_level_localization(granularity_results, file_output_dir, workflow_env=None):
    """Run function level localization only for function granularity proposals."""
    print_phase_header(1, "LOCALIZATION", 4, "FUNCTION LEVEL LOCALIZATION")

    function_proposals = [proposal for proposal, granularity in granularity_results.items()
                         if granularity == "function"]

    if not function_proposals:
        print_progress("No proposals require function-level processing. Skipping function_level_localization.")
        return None

    print_progress(f"Processing {len(function_proposals)} function-granularity proposals")

    function_dir = Path(__file__).parent / 'function_level_localization'
    print_progress(f"Working directory: {function_dir}")

    env = (os.environ.copy() if workflow_env is None else workflow_env.copy())
    env['GRANULARITY_RESULTS'] = json.dumps(granularity_results)
    env['SELECTED_DIRECTORY_FILE_OUTPUT'] = str(file_output_dir.name)
    print_progress(f"Setting environment variables: GRANULARITY_RESULTS, SELECTED_DIRECTORY_FILE_OUTPUT={file_output_dir.name}")

    print_progress("Executing function_level_localization main.py...")
    result = run_subprocess_with_progress(
        [sys.executable, 'main.py'],
        cwd=function_dir,
        env=env
    )

    if result.returncode != 0:
        print_progress(f"ERROR: Function level localization failed with return code {result.returncode}")
        print(f"Output: {result.stdout}")
        sys.exit(1)

    print_progress("Function level localization completed successfully")    # Find the most recent output
    output_dir = function_dir / 'output'
    print_progress(f"Looking for output in: {output_dir}")
    
    try:
        latest_output = max(output_dir.glob('*/llm_outputs.json'), key=lambda p: p.stat().st_mtime)
        print_progress(f"Found function level localization results: {latest_output}")
    except ValueError:
        print_progress("ERROR: No function level localization llm_outputs.json found")
        sys.exit(1)
    
    return latest_output.parent

def run_file_level_link_decision(granularity_results, file_output_dir, workflow_env=None):
    """Run file level link decision only for file granularity proposals."""
    print_phase_header(1, "LOCALIZATION", 3, "FILE LEVEL LINK DECISION")

    file_proposals = [proposal for proposal, granularity in granularity_results.items()
                     if granularity == "file"]

    if not file_proposals:
        print_progress("No proposals require file-level link decision processing. Skipping file_level_link_decision.")
        return None

    print_progress(f"Processing {len(file_proposals)} file-granularity proposals")

    file_link_dir = Path(__file__).parent / 'file_level_link_decision'
    print_progress(f"Working directory: {file_link_dir}")

    env = (os.environ.copy() if workflow_env is None else workflow_env.copy())
    env['GRANULARITY_RESULTS'] = json.dumps(granularity_results)
    env['SELECTED_DIRECTORY_FILE_OUTPUT'] = str(file_output_dir.name)
    print_progress(f"Setting environment variables: GRANULARITY_RESULTS, SELECTED_DIRECTORY_FILE_OUTPUT={file_output_dir.name}")

    print_progress("Executing file_level_link_decision main.py...")
    result = run_subprocess_with_progress(
        [sys.executable, 'main.py'],
        cwd=file_link_dir,
        env=env
    )

    if result.returncode != 0:
        print_progress(f"ERROR: File level link decision failed with return code {result.returncode}")
        print(f"Output: {result.stdout}")
        sys.exit(1)

    print_progress("File level link decision completed successfully")
    
    # Find the most recent output
    output_dir = file_link_dir / 'output'
    print_progress(f"Looking for output in: {output_dir}")
    
    try:
        latest_output = max(output_dir.glob('*/llm_outputs.json'), key=lambda p: p.stat().st_mtime)
        print_progress(f"Found file level link decision results: {latest_output}")
    except ValueError:
        print_progress("ERROR: No file level link decision llm_outputs.json found")
        sys.exit(1)
    
    return latest_output.parent

def run_function_level_link_decision(granularity_results, function_output_dir, workflow_env=None):
    """Run function level link decision only for function granularity proposals."""
    print_phase_header(2, "FUNCTION LEVEL LINK DECISION")

    function_proposals = [proposal for proposal, granularity in granularity_results.items()
                         if granularity == "function"]

    if not function_proposals:
        print_progress("No proposals require link decision processing. Skipping function_level_link_decision.")
        return None

    if function_output_dir is None:
        print_progress("No function level output available. Skipping function_level_link_decision.")
        return None

    print_progress(f"Processing {len(function_proposals)} function-granularity proposals")

    link_decision_dir = Path(__file__).parent / 'function_level_link_decision'
    print_progress(f"Working directory: {link_decision_dir}")

    env = (os.environ.copy() if workflow_env is None else workflow_env.copy())
    env['GRANULARITY_RESULTS'] = json.dumps(granularity_results)
    env['SELECTED_FUNCTION_OUTPUT'] = str(function_output_dir.name)
    print_progress(f"Setting environment variables: GRANULARITY_RESULTS, SELECTED_FUNCTION_OUTPUT={function_output_dir.name}")

    print_progress("Executing function_level_link_decision main.py...")
    result = run_subprocess_with_progress(
        [sys.executable, 'main.py'],
        cwd=link_decision_dir,
        env=env
    )

    if result.returncode != 0:
        print_progress(f"ERROR: Function level link decision failed with return code {result.returncode}")
        print(f"Output: {result.stdout}")
        sys.exit(1)

    print_progress("Function level link decision completed successfully")    # Find the most recent output
    output_dir = link_decision_dir / 'output'
    print_progress(f"Looking for output in: {output_dir}")
    
    try:
        latest_output = max(output_dir.glob('*/llm_outputs.json'), key=lambda p: p.stat().st_mtime)
        print_progress(f"Found function level link decision results: {latest_output}")
    except ValueError:
        print_progress("ERROR: No function level link decision llm_outputs.json found")
        sys.exit(1)
    
    return latest_output.parent

def create_integrated_results(granularity_results, granularity_output_dir, 
                            directory_output_dir, file_output_dir, file_link_decision_output_dir, 
                            function_output_dir, function_link_decision_output_dir, batch_size, repo_set,
                            output_root=None):
    """Create integrated results combining all phases. repo_set: REPO_SET for loading repo_structure_{repo_set}.json.
    output_root: optional; if None, uses Path(__file__).parent / 'output'."""
    print_phase_header("FINAL", "RESULT INTEGRATION")
    print_progress("Creating integrated results from all phases...")
    
    # Create output directory with timestamp
    if output_root is None:
        output_root = Path(__file__).parent / 'output'
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = output_root / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print_progress(f"Created output directory: {output_dir}")
    
    # Initialize integrated results
    integrated_results = {
        "workflow_info": {
            "timestamp": timestamp,
            "batch_size": batch_size,
            "total_documents": len(granularity_results),
            "granularity_breakdown": {
                "directory": sum(1 for g in granularity_results.values() if g == "directory"),
                "file": sum(1 for g in granularity_results.values() if g == "file"),
                "function": sum(1 for g in granularity_results.values() if g == "function")
            }
        },
        "documents": {}
    }
    
    # Load directory and file level results
    directory_file_results = {}
    
    print_progress(f"DEBUG: directory_output_dir = {directory_output_dir}")
    print_progress(f"DEBUG: file_output_dir = {file_output_dir}")
    
    # Load directory level results
    if directory_output_dir:
        directory_json = directory_output_dir / 'llm_outputs.json'
        print_progress(f"DEBUG: Looking for directory JSON at: {directory_json}")
        if directory_json.exists():
            with open(directory_json, 'r') as f:
                directory_data = json.load(f)
            directory_file_results.update(directory_data)
            print_progress(f"Loaded directory results: {len(directory_data)} documents")
        else:
            print_progress(f"WARNING: Directory JSON file not found: {directory_json}")
    
    # Load file level results  
    if file_output_dir:
        file_json = file_output_dir / 'llm_outputs.json'
        print_progress(f"DEBUG: Looking for file JSON at: {file_json}")
        if file_json.exists():
            with open(file_json, 'r') as f:
                file_data = json.load(f)
            directory_file_results.update(file_data)
            print_progress(f"Loaded file results: {len(file_data)} documents")
        else:
            print_progress(f"WARNING: File JSON file not found: {file_json}")

    print_progress(f"Loaded directory/file results: {len(directory_file_results)} documents")
    
    # Load function level results
    function_results = {}
    if function_output_dir:
        function_json = function_output_dir / 'llm_outputs.json'
        if function_json.exists():
            with open(function_json, 'r') as f:
                function_results = json.load(f)
            print_progress(f"Loaded function results: {len(function_results)} documents")
    
    # Load file level link decision results
    file_link_decision_results = {}
    if file_link_decision_output_dir:
        file_link_json = file_link_decision_output_dir / 'llm_outputs.json'
        if file_link_json.exists():
            with open(file_link_json, 'r') as f:
                file_link_decision_results = json.load(f)
            print_progress(f"Loaded file link decision results: {len(file_link_decision_results)} entries")
    
    # Load function level link decision results
    function_link_decision_results = {}
    if function_link_decision_output_dir:
        function_link_json = function_link_decision_output_dir / 'llm_outputs.json'
        if function_link_json.exists():
            with open(function_link_json, 'r') as f:
                function_link_decision_results = json.load(f)
            print_progress(f"Loaded function link decision results: {len(function_link_decision_results)} entries")
    
    # Integrate results for each document
    total_docs = len(granularity_results)
    for idx, (doc_name, granularity) in enumerate(granularity_results.items(), 1):
        print_phase_progress(idx, total_docs, "documents")
        print_progress(f"Integrating results for {doc_name} (granularity: {granularity})")

        doc_result = {
            "document": doc_name,
            "granularity": granularity,
            "phase_results": {}
        }

        # Phase 0: Granularity Decision
        doc_result["phase_results"]["granularity_decision"] = {
            "decided_granularity": granularity
        }

        # Phase 1: Directory and File Level
        if doc_name in directory_file_results:
            df_result = directory_file_results[doc_name]
            doc_result["phase_results"]["directory_file_level"] = df_result

            print_progress(f"DEBUG: Processing {doc_name} with granularity {granularity}")
            print_progress(f"DEBUG: df_result keys: {list(df_result.keys()) if df_result else 'None'}")

            if granularity == "directory":
                found_directories = df_result.get("found_directories", [])
                found_files = df_result.get("found_files", [])
                doc_result["found_directories"] = found_directories
                doc_result["found_files"] = found_files
                print_progress(f"DEBUG: Directory granularity - found {len(found_directories)} directories, {len(found_files)} files")
            else:
                found_files = df_result.get("found_files", [])
                doc_result["found_files"] = found_files
                print_progress(f"DEBUG: File/Function granularity - found {len(found_files)} files")
        else:
            print_progress(f"WARNING: Document {doc_name} not found in directory_file_results")

        # Phase 1: Function Level (only for function granularity)
        if granularity == "function" and doc_name in function_results:
            func_result = function_results[doc_name]
            doc_result["phase_results"]["function_level_localization"] = func_result

            total_functions = []
            for file_path, functions in func_result.items():
                if file_path != "selected_file_level_output":
                    for func in functions:
                        total_functions.append({
                            "file_path": file_path,
                            "function_name": func
                        })
            doc_result["found_functions"] = total_functions

        # Phase 1 Step 3: File Level Link Decision (only for file granularity)
        if granularity == "file" and doc_name in file_link_decision_results:
            file_link_data = file_link_decision_results[doc_name]
            doc_files = []

            for file_path, file_decision_data in file_link_data.items():
                file_entry = {
                    "file_path": file_path,
                    "link_decision": file_decision_data.get("decision", "Unknown")
                }
                doc_files.append(file_entry)

            if doc_files:
                doc_result["phase_results"]["file_level_link_decision"] = {
                    "total_files": len(doc_files),
                    "files_with_yes": sum(1 for f in doc_files if f["link_decision"] == "Yes"),
                    "files_with_no": sum(1 for f in doc_files if f["link_decision"] == "No"),
                    "detailed_results": doc_files
                }
                doc_result["final_files"] = [f for f in doc_files if f["link_decision"] == "Yes"]

        # Phase 2: Function Level Link Decision (only for function granularity)
        if granularity == "function" and doc_name in function_link_decision_results:
            link_data = function_link_decision_results[doc_name]
            doc_functions = []

            for file_path, file_functions in link_data.items():
                if file_path != "selected_function_level_localization_output":
                    for function_name, link_decision in file_functions.items():
                        doc_functions.append({
                            "file_path": file_path,
                            "function_name": function_name,
                            "link_decision": link_decision
                        })

            if doc_functions:
                doc_result["phase_results"]["function_level_link_decision"] = {
                    "total_functions": len(doc_functions),
                    "functions_with_yes": sum(1 for f in doc_functions if f["link_decision"] == "Yes"),
                    "functions_with_no": sum(1 for f in doc_functions if f["link_decision"] == "No"),
                    "detailed_results": doc_functions
                }
                doc_result["final_functions"] = [f for f in doc_functions if f["link_decision"] == "Yes"]

        integrated_results["documents"][doc_name] = doc_result
    
    # Save integrated results
    integrated_json = output_dir / 'integrated_results.json'
    with open(integrated_json, 'w') as f:
        json.dump(integrated_results, f, indent=2)
    
    # Create summary report
    summary_report = output_dir / 'summary_report.txt'
    with open(summary_report, 'w') as f:
        f.write("C Design Document Link Workflow - Summary Report\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Execution Time: {timestamp}\n")
        f.write(f"Batch Size: {batch_size}\n")
        f.write(f"Total Documents: {len(granularity_results)}\n\n")
        
        f.write("Granularity Breakdown:\n")
        for granularity, count in integrated_results["workflow_info"]["granularity_breakdown"].items():
            f.write(f"  {granularity.capitalize()}: {count} documents\n")
        f.write("\n")
        
        f.write("Results by Document:\n")
        f.write("-" * 30 + "\n")
        for doc_name, result in integrated_results["documents"].items():
            f.write(f"\n{doc_name} ({result['granularity']} granularity):\n")
            
            if "found_files" in result:
                f.write(f"  Found Files: {len(result['found_files'])}\n")
                for file_path in result['found_files'][:5]:  # Show first 5
                    f.write(f"    - {file_path}\n")
                if len(result['found_files']) > 5:
                    f.write(f"    ... and {len(result['found_files']) - 5} more\n")
            
            if "found_functions" in result:
                f.write(f"  Found Functions: {len(result['found_functions'])}\n")
            
            if "final_files" in result:
                f.write(f"  Final Files (Yes): {len(result['final_files'])}\n")
                for file_info in result['final_files'][:3]:  # Show first 3
                    file_path = file_info.get('file_path', '') if isinstance(file_info, dict) else file_info
                    f.write(f"    - {file_path}\n")
                if len(result['final_files']) > 3:
                    f.write(f"    ... and {len(result['final_files']) - 3} more\n")
            
            if "final_functions" in result:
                f.write(f"  Final Functions (Yes): {len(result['final_functions'])}\n")
                for func in result['final_functions'][:3]:  # Show first 3
                    f.write(f"    - {func['file_path']}:{func['function_name']}\n")
                if len(result['final_functions']) > 3:
                    f.write(f"    ... and {len(result['final_functions']) - 3} more\n")
    
    print_progress(f"Integrated results saved to: {integrated_json}")
    print_progress(f"Summary report saved to: {summary_report}")
    
    # Create CSV report with detailed breakdown
    csv_report = output_dir / f'results_summary_{timestamp}.csv'
    with open(csv_report, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'Document',
            'Granularity',
            'Directory Level',
            'File Level',
            'Function Level',
            'Code Path'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        all_rows = []
        total_docs_for_csv = len(integrated_results["documents"])
        for idx, (doc_name, result) in enumerate(integrated_results["documents"].items(), 1):
            print_phase_progress(idx, total_docs_for_csv, "documents for CSV")
            doc_id = extract_document_id(doc_name)
            granularity = result["granularity"]
            
            # Generate rows based on granularity level
            if granularity == "directory":
                # For directory granularity, show each directory (with existence validation)
                found_directories = result.get('found_directories', [])
                valid_directories = []
                
                if found_directories:
                    for directory in found_directories:
                        if directory_exists_in_repo(directory, repo_set):
                            valid_directories.append(directory)
                        else:
                            print_progress(f"WARNING: Directory {directory} does not exist in repository, excluding from output")
                    
                    if valid_directories:
                        for directory in valid_directories:
                            all_rows.append({
                                'Document': doc_id,
                                'Granularity': granularity,
                                'Directory Level': directory,
                                'File Level': 'N/A',
                                'Function Level': 'N/A',
                                'Code Path': _code_url_tree(directory)
                            })
                    else:
                        # All directories were invalid
                        all_rows.append({
                            'Document': doc_id,
                            'Granularity': granularity,
                            'Directory Level': 'No valid directories found',
                            'File Level': 'N/A',
                            'Function Level': 'N/A',
                            'Code Path': _code_url_fallback()
                        })
                else:
                    # Fallback if no directories found
                    all_rows.append({
                        'Document': doc_id,
                        'Granularity': granularity,
                        'Directory Level': 'No directories found',
                        'File Level': 'N/A',
                        'Function Level': 'N/A',
                        'Code Path': _code_url_fallback()
                    })
            
            elif granularity == "file":
                # For file granularity, show directories and files (with existence validation)
                # Priority 1: Use final_files (files with "Yes" decision from file_level_link_decision)
                final_files = result.get('final_files', [])
                found_files = result.get('found_files', [])
                
                if final_files:
                    # final_files have already been validated through file_level_link_decision
                    for file_info in final_files:
                        file_path = file_info.get('file_path', '')
                        
                        # Extract directory from file path
                        directory = str(Path(file_path).parent) if '/' in file_path else '.'
                        
                        all_rows.append({
                            'Document': doc_id,
                            'Granularity': granularity,
                            'Directory Level': directory,
                            'File Level': file_path,
                            'Function Level': 'N/A',
                            'Code Path': _code_url_blob(file_path)
                        })
                elif found_files:
                    # Fallback to found_files with existence validation
                    valid_files = []
                    for file_path in found_files:
                        if file_exists_in_repo(file_path, repo_set):
                            valid_files.append(file_path)
                        else:
                            print_progress(f"WARNING: File {file_path} does not exist in repository, excluding from output")
                    
                    if valid_files:
                        for file_path in valid_files:
                            # Extract directory from file path
                            directory = str(Path(file_path).parent) if '/' in file_path else '.'
                            
                            all_rows.append({
                                'Document': doc_id,
                                'Granularity': granularity,
                                'Directory Level': directory,
                                'File Level': file_path,
                                'Function Level': 'N/A',
                                'Code Path': _code_url_blob(file_path)
                            })
                    else:
                        # All files were invalid
                        all_rows.append({
                            'Document': doc_id,
                            'Granularity': granularity,
                            'Directory Level': 'No valid files found',
                            'File Level': 'No valid files found',
                            'Function Level': 'N/A',
                            'Code Path': _code_url_fallback()
                        })
                else:
                    # Fallback if no files found
                    all_rows.append({
                        'Document': doc_id,
                        'Granularity': granularity,
                        'Directory Level': 'No files found',
                        'File Level': 'No files found',
                        'Function Level': 'N/A',
                        'Code Path': _code_url_fallback()
                    })
            
            elif granularity == "function":
                # For function granularity, show directories, files, and functions (with existence validation)
                final_functions = result.get('final_functions', [])
                found_functions = result.get('found_functions', [])
                found_files = result.get('found_files', [])
                
                # Priority 1: Use final_functions (functions with "Yes" decision)
                if final_functions:
                    # Validate final_functions for file and function existence
                    valid_final_functions = []
                    for func_info in final_functions:
                        file_path = func_info.get('file_path', '')
                        function_name = func_info.get('function_name', '')
                        
                        if file_exists_in_repo(file_path, repo_set):
                            if function_exists_in_file(file_path, function_name, repo_set):
                                valid_final_functions.append(func_info)
                            else:
                                print_progress(f"WARNING: Function {function_name} does not exist in file {file_path}, excluding from output")
                        else:
                            print_progress(f"WARNING: File {file_path} (for function {function_name}) does not exist in repository, excluding from output")
                    
                    if valid_final_functions:
                        for func_info in valid_final_functions:
                            file_path = func_info.get('file_path', '')
                            function_name = func_info.get('function_name', '')
                            
                            # Extract directory from file path
                            directory = str(Path(file_path).parent) if '/' in file_path else '.'
                            
                            all_rows.append({
                                'Document': doc_id,
                                'Granularity': granularity,
                                'Directory Level': directory,
                                'File Level': file_path,
                                'Function Level': function_name,
                                'Code Path': _code_url_blob(file_path)
                            })
                    else:
                        # No valid final functions found
                        all_rows.append({
                            'Document': doc_id,
                            'Granularity': granularity,
                            'Directory Level': 'No valid functions found',
                            'File Level': 'No valid functions found',
                            'Function Level': 'No valid functions found',
                            'Code Path': _code_url_fallback()
                        })
                
                # Priority 2: Use found_functions with existence validation
                elif found_functions:
                    # Group functions by file and validate both files and functions
                    files_with_functions = {}
                    for func_info in found_functions:
                        file_path = func_info.get('file_path', '')
                        function_name = func_info.get('function_name', '')
                        
                        if file_exists_in_repo(file_path, repo_set):
                            if function_exists_in_file(file_path, function_name, repo_set):
                                if file_path not in files_with_functions:
                                    files_with_functions[file_path] = []
                                files_with_functions[file_path].append(function_name)
                            else:
                                print_progress(f"WARNING: Function {function_name} does not exist in file {file_path}, excluding from output")
                        else:
                            print_progress(f"WARNING: File {file_path} (with function {function_name}) does not exist in repository, excluding from output")
                    
                    # Create one row per valid file with "not selected"
                    if files_with_functions:
                        for file_path in files_with_functions:
                            directory = str(Path(file_path).parent) if '/' in file_path else '.'
                            
                            all_rows.append({
                                'Document': doc_id,
                                'Granularity': granularity,
                                'Directory Level': directory,
                                'File Level': file_path,
                                'Function Level': 'not selected',
                                'Code Path': _code_url_blob(file_path)
                            })
                    else:
                        # All files with functions were invalid
                        all_rows.append({
                            'Document': doc_id,
                            'Granularity': granularity,
                            'Directory Level': 'No valid files with functions',
                            'File Level': 'No valid files with functions',
                            'Function Level': 'No valid functions found',
                            'Code Path': _code_url_fallback()
                        })
                
                # Priority 3: Fallback to file level with existence validation
                elif found_files:
                    valid_files = []
                    for file_path in found_files:
                        if file_exists_in_repo(file_path, repo_set):
                            valid_files.append(file_path)
                        else:
                            print_progress(f"WARNING: File {file_path} does not exist in repository, excluding from output")
                    
                    if valid_files:
                        for file_path in valid_files:
                            directory = str(Path(file_path).parent) if '/' in file_path else '.'
                            
                            all_rows.append({
                                'Document': doc_id,
                                'Granularity': granularity,
                                'Directory Level': directory,
                                'File Level': file_path,
                                'Function Level': 'Function analysis failed',
                                'Code Path': _code_url_blob(file_path)
                            })
                    else:
                        # All files were invalid
                        all_rows.append({
                            'Document': doc_id,
                            'Granularity': granularity,
                            'Directory Level': 'No valid files found',
                            'File Level': 'No valid files found',
                            'Function Level': 'Function analysis failed',
                            'Code Path': _code_url_fallback()
                        })
                
                # Priority 4: Ultimate fallback (avoid "No results found")
                else:
                    all_rows.append({
                        'Document': doc_id,
                        'Granularity': granularity,
                        'Directory Level': 'Analysis incomplete',
                        'File Level': 'Analysis incomplete',
                        'Function Level': 'Analysis incomplete',
                        'Code Path': _code_url_fallback()
                    })
        
        # Now process rows to remove duplicates (except Code Path)
        fields_to_check = ['Document', 'Granularity', 'Directory Level', 'File Level', 'Function Level']
        previous_values = {}
        
        for i, row in enumerate(all_rows):
            # Check if this is a new document (Document changed)
            is_new_proposal = (i == 0 or row['Document'] != previous_values.get('Document', ''))
            
            if is_new_proposal:
                # For new document, show all values and reset previous_values
                for field in fields_to_check:
                    previous_values[field] = row[field]
            else:
                # For same document, apply duplicate removal logic
                for field in fields_to_check:
                    if field == 'Function Level':
                        # Special handling for Function Level
                        if row[field] == 'not selected':
                            # Always show "not selected" for each file, don't remove duplicates
                            previous_values[field] = row[field]
                        elif row[field] == '' and previous_values.get(field, '') == 'not selected':
                            # If this row has empty Function Level but previous was "not selected",
                            # this is likely a function granularity with no selected functions
                            row[field] = 'not selected'
                            previous_values[field] = row[field]
                        elif row[field] == previous_values.get(field, ''):
                            row[field] = ''
                        else:
                            previous_values[field] = row[field]
                    elif row[field] == previous_values.get(field, ''):
                        row[field] = ''
                    else:
                        previous_values[field] = row[field]
            
            # Write the processed row
            writer.writerow(row)
    
    print_progress(f"CSV report saved to: {csv_report}")
    
    return output_dir

def main():
    """Run the complete coordinated workflow for C design documents (data/docs/{DOCS_SET}) and repo (data/repos/{REPO_SET})."""
    project_root = Path(__file__).resolve().parent.parent
    docs_base = project_root / "data" / "docs"
    repos_base = project_root / "data" / "repos"

    print("Starting C design document link workflow")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # DOCS_SET: which document set (data/docs/{DOCS_SET})
    docs_set = os.environ.get("DOCS_SET", "").strip()
    available_docs = sorted([d.name for d in docs_base.iterdir() if d.is_dir()]) if docs_base.exists() else []
    default_docs = "sample_doc" if "sample_doc" in available_docs else (available_docs[0] if available_docs else "sample_doc")
    if not docs_set:
        if available_docs:
            print(f"\nAvailable document sets (data/docs/): {available_docs}")
        try:
            docs_set = input(f"Document set (DOCS_SET) [default: {default_docs}]: ").strip() or default_docs
        except (EOFError, KeyboardInterrupt):
            docs_set = default_docs
            print(f"Using default document set: {docs_set}")
    docs_dir = docs_base / docs_set
    if not docs_dir.exists() or not docs_dir.is_dir():
        print(f"Error: Document set not found: {docs_dir}", file=sys.stderr)
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

    print(f"Using documents: data/docs/{docs_set}  repository: data/repos/{repo_set}\n")

    # Structure type: full, 500, 1000, 2000 (max lines per chunk; full = no split). Env: REPOSITORY_STRUCTURE_TYPE.
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
    # Full name: repository_structure_{type}_{repo_set} (or use REPOSITORY_STRUCTURE env as-is)
    repository_structure = os.environ.get("REPOSITORY_STRUCTURE", "").strip()
    if not repository_structure:
        repository_structure = f"repository_structure_{structure_type}_{repo_set}"
    print(f"Repository structure: {repository_structure}\n")

    # Non-interactive: use env BATCH_SIZE, START_FROM
    batch_size = os.environ.get("BATCH_SIZE", "").strip()
    start_from = os.environ.get("START_FROM", "").strip()

    if not batch_size or not start_from:
        print("Select number of documents to process:")
        print("  - Enter a number (e.g., 5, 10) or 'all' for all")
        batch_size = (batch_size or input("Batch size [default: all]: ").strip()) or "all"
        print("Start from index (0-based). Press Enter for 0.")
        start_from = (start_from or input("Start from index [default: 0]: ").strip()) or "0"

    if batch_size.lower() != "all":
        try:
            n = int(batch_size)
            batch_size = str(n) if n >= 1 else "all"
        except ValueError:
            batch_size = "all"
    if not start_from:
        start_from = "0"
    try:
        start_from = str(max(0, int(start_from)))
    except ValueError:
        start_from = "0"

    print(f"Processing {batch_size} document(s) starting from index {start_from} ({repository_structure})...\n")

    # Env passed to all subprocesses: DOCS_SET, REPO_SET, C_REPO_ROOT, REPOSITORY_STRUCTURE
    workflow_env = os.environ.copy()
    workflow_env["DOCS_SET"] = docs_set
    workflow_env["REPO_SET"] = repo_set
    workflow_env["C_REPO_ROOT"] = str(repo_dir)
    workflow_env["REPOSITORY_STRUCTURE"] = repository_structure
    # Enable prompt logging by default
    workflow_env["LOG_PROMPTS"] = os.environ.get("LOG_PROMPTS", "0")

    # Phase 0: Granularity Decision
    granularity_results, granularity_output_dir = run_granularity_decision(batch_size, start_from, workflow_env)
    
    # Phase 1 Step 1: Directory Level and Step 2: Directory and File Level
    # Phase 1: Localization
    print_progress("Starting Phase 1: Localization")
    
    # Count proposals by granularity
    directory_count = sum(1 for g in granularity_results.values() if g == "directory")
    file_count = sum(1 for g in granularity_results.values() if g == "file")
    function_count = sum(1 for g in granularity_results.values() if g == "function")
    
    print_progress("Granularity breakdown:")
    print(f"  Directory: {directory_count}, File: {file_count}, Function: {function_count}")
    print(f"  Total: {len(granularity_results)} documents")
    
    # Run directory level localization for directory granularity proposals
    directory_output_dir = run_directory_level_localization(granularity_results, repository_structure, workflow_env)

    # Run file level localization for file and function granularity proposals
    file_output_dir = run_file_level_localization(granularity_results, repository_structure, workflow_env)

    # Phase 1 Step 3: File Level Link Decision (file granularity only)
    file_link_decision_output_dir = None
    if file_output_dir:
        file_link_decision_output_dir = run_file_level_link_decision(granularity_results, file_output_dir, workflow_env)

    # Phase 1 Step 4: Function Level (function granularity only)
    function_output_dir = None
    if file_output_dir:
        function_output_dir = run_function_level_localization(granularity_results, file_output_dir, workflow_env)

    # Phase 2: Function Level Link Decision (function granularity only)
    function_link_decision_output_dir = run_function_level_link_decision(granularity_results, function_output_dir, workflow_env)
    
    # Create integrated results
    integrated_output_dir = create_integrated_results(
        granularity_results, granularity_output_dir, directory_output_dir, file_output_dir, 
        file_link_decision_output_dir, function_output_dir, function_link_decision_output_dir, batch_size, repo_set
    )
    
    # Summary
    print("=" * 70)
    print("WORKFLOW COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("Output directories:")
    print(f"  Phase 0 (Granularity): {granularity_output_dir}")
    print(f"  Phase 1 Step 1 (Directory): {directory_output_dir}")
    print(f"  Phase 1 Step 2 (Directory and File): {file_output_dir}")
    if file_link_decision_output_dir:
        print(f"  Phase 1 Step 3 (File Link Decision): {file_link_decision_output_dir}")
    if function_output_dir:
        print(f"  Phase 1 Step 4 (Function): {function_output_dir}")
    if function_link_decision_output_dir:
        print(f"  Phase 2 (Function Link Decision): {function_link_decision_output_dir}")
    print(f"  Integrated Results: {integrated_output_dir}")
    print(f"    - JSON: {integrated_output_dir / 'integrated_results.json'}")
    print(f"    - Summary: {integrated_output_dir / 'summary_report.txt'}")
    csv_files = list(integrated_output_dir.glob('results_summary_*.csv'))
    if csv_files:
        print(f"    - CSV: {csv_files[0]}")
    else:
        print(f"    - CSV: {integrated_output_dir / 'results_summary.csv'}")
    
    # Statistics
    directory_count = sum(1 for g in granularity_results.values() if g == "directory")
    file_count = sum(1 for g in granularity_results.values() if g == "file")
    function_count = sum(1 for g in granularity_results.values() if g == "function")
    
    print(f"\nFinal Statistics:")
    print(f"  Batch size: {batch_size}, Total: {len(granularity_results)} documents")
    print(f"  Directory: {directory_count}, File: {file_count}, Function: {function_count}")

if __name__ == "__main__":
    main() 