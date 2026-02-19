"""
C source skeleton and prompt for function-level localization.
Uses repo_structure_{REPO_SET}.json (no tree-sitter dependency here).
"""

import json
import os
from pathlib import Path

_repo_structure_cache = {}


def get_repo_structure():
    """Load repo_structure_{REPO_SET}.json once per REPO_SET and cache it."""
    global _repo_structure_cache
    repo_set = os.environ.get("REPO_SET", "sample_repo").strip()
    if repo_set not in _repo_structure_cache:
        repo_structure_path = Path(__file__).parent.parent.parent.parent / "data" / "preprocess" / f"repo_structure_{repo_set}.json"
        try:
            with open(repo_structure_path, "r") as f:
                _repo_structure_cache[repo_set] = json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load repo structure: {e}")
            _repo_structure_cache[repo_set] = {}
    return _repo_structure_cache[repo_set]


def build_c_skeleton_from_repo_structure(file_path):
    """
    Build a C file skeleton string from repo_structure_{REPO_SET}.json for the given file path.
    Returns (skeleton_string, True) if found, (empty_string, False) otherwise.
    """
    repo = get_repo_structure()
    file_data = repo.get(str(file_path))
    if not file_data:
        return "", False
    lines = []
    # Function definitions
    for name, defs in file_data.get("functions", {}).items():
        for d in defs:
            sig = d.get("signature", "").strip()
            if sig:
                lines.append(sig + " { ... }")
            break
    # Function declarations (no body)
    for name, decls in file_data.get("function_declarations", {}).items():
        for d in decls:
            sig = d.get("signature", "").strip()
            if sig and not sig.endswith(";"):
                sig = sig + ";"
            if sig:
                lines.append(sig)
            break
    return "\n".join(lines), True


def extract_c_skeleton(file_path):
    """
    Return C skeleton for the given repo-relative file path.
    Uses repo_structure_{REPO_SET}.json. Returns empty string if file not in structure.
    """
    skeleton, ok = build_c_skeleton_from_repo_structure(file_path)
    return skeleton


def generate_function_level_localization_prompt(doc_text, file_path, directory, skeleton):
    """
    Generate prompt for function-level localization: design document + one C file skeleton → relevant function names.
    """
    return f'''You are analyzing a design document and a C source file to identify which functions are **most relevant** to the given document.

### Design Document ###
{doc_text}

### File Information ###
File: {file_path}
Directory: {directory}

### File Skeleton ###
{skeleton}

**CRITICAL OBJECTIVE**: Identify the **most relevant functions** in this file that are closely related to the design document.

**WHAT TO INCLUDE:**
- C functions (definitions and declarations shown in the skeleton).

**MANDATORY OUTPUT FORMAT:**
Return a JSON object with the following format.
The response MUST:
- Be a valid JSON block.
- Contain a key `relevant_functions` with a list of function names (strings).
- Output ONLY the raw JSON object. Do NOT include any markdown formatting (no ```json or ```).
- Do NOT add any explanations or additional text.

Example of correct output:
{{
  "relevant_functions": [
    "function_name_one",
    "function_name_two"
  ]
}}

**MANDATORY SELECTION RULES:**
- Select only the most essential functions that are directly related to the design document.
- The output must strictly follow the format.
- If you are unsure, make your best guess based on the file skeleton and document.
'''.strip()


def generate_function_level_localization_diff_prompt(base_spec_text: str, changed_spec_text: str, file_path: str, directory: str, skeleton: str) -> str:
    """
    Generate prompt for function-level localization in diff (change-driven) mode.
    Given base and changed spec sections, identify which function(s) in the file were modified.
    """
    return f'''You are analyzing a specification change to identify which function(s) in a C source file were **modified** to implement the change. Two specification sections are given: the base (before) and the changed (after) version. Exactly one function in this file was modified.

### Base Specification (Before Change) ###
{base_spec_text}

### Changed Specification (After Change) ###
{changed_spec_text}

### File Information ###
File: {file_path}
Directory: {directory}

### File Skeleton ###
{skeleton}

**CRITICAL OBJECTIVE**: Identify the **function(s)** in this file that were modified to implement the specification change.

**WHAT TO INCLUDE:**
- C functions (definitions and declarations shown in the skeleton) that correspond to the changed specification.

**MANDATORY OUTPUT FORMAT:**
Return a JSON object with the following format.
The response MUST:
- Be a valid JSON block.
- Contain a key `relevant_functions` with a list of function names (strings).
- Output ONLY the raw JSON object. Do NOT include any markdown formatting (no ```json or ```).
- Do NOT add any explanations or additional text.

Example of correct output:
{{
  "relevant_functions": [
    "function_name_one"
  ]
}}

**MANDATORY SELECTION RULES:**
- Select only the function(s) that were modified to implement the specification change.
- The output must strictly follow the format.
- If you are unsure, make your best guess based on the file skeleton and the spec diff.
'''.strip()
