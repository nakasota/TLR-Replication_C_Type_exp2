"""
Extract C function code and file context from repo_structure_{REPO_SET}.json.
"""

import json
import os
import re
from pathlib import Path

_repo_structure_cache = {}


def get_repo_structure():
    """Load repo_structure_{REPO_SET}.json once per REPO_SET and cache it."""
    global _repo_structure_cache
    repo_set = os.environ.get('REPO_SET', 'sample_repo').strip()
    if repo_set not in _repo_structure_cache:
        repo_structure_path = Path(__file__).parent.parent.parent.parent / 'data' / 'preprocess' / f'repo_structure_{repo_set}.json'
        try:
            with open(repo_structure_path, 'r') as f:
                _repo_structure_cache[repo_set] = json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load repo structure: {e}")
            _repo_structure_cache[repo_set] = {}
    return _repo_structure_cache[repo_set]


def analyze_function_relevance(file_path, function_name):
    """
    Extract the given function's code and file context from repo_structure_{REPO_SET}.json.
    Returns {"function_code": str, "context": str} or None if not found.
    """
    try:
        repo_structure = get_repo_structure()
        file_path_str = str(file_path)

        if file_path_str not in repo_structure:
            print(f"[ERROR] File {file_path_str} not found in repo structure")
            return None

        file_data = repo_structure[file_path_str]
        file_content = file_data.get('content', '')

        # Prefer function definition (has body)
        functions = file_data.get('functions', {})
        if function_name in functions:
            defs = functions[function_name]
            if defs:
                function_code = defs[0].get('content', '').strip()
                if function_code:
                    context = _extract_c_file_context(file_content, function_name)
                    return {"function_code": function_code, "context": context}

        # Fallback: function declaration only
        declarations = file_data.get('function_declarations', {})
        if function_name in declarations:
            decls = declarations[function_name]
            if decls:
                sig = decls[0].get('signature', '').strip()
                if not sig.endswith(';'):
                    sig += ';'
                function_code = sig + " /* declaration only */"
                context = _extract_c_file_context(file_content, function_name)
                return {"function_code": function_code, "context": context}

        print(f"[ERROR] Function {function_name} not found in {file_path_str}")
        return None

    except Exception as e:
        print(f"[ERROR] Failed to analyze function {function_name} in {file_path}: {e}")
        return None


def _extract_c_file_context(file_content, target_function_name):
    """Extract C file context: includes, macros, other function signatures."""
    parts = []
    lines = file_content.split('\n')

    # Includes
    includes = [line.strip() for line in lines if line.strip().startswith('#include')]
    if includes:
        parts.append("Includes:\n" + "\n".join(includes))

    # Macros
    macros = [line.strip() for line in lines if line.strip().startswith('#define')]
    if macros:
        parts.append("Macros:\n" + "\n".join(macros[:30]))  # limit size

    # Other function signatures (regex-based to avoid re-parsing)
    other_sigs = []
    # Match function definition: return_type name(args) { ... }
    func_def = re.compile(r'^[\w\s\*]+\s+(\w+)\s*\([^)]*\)\s*\{', re.MULTILINE)
    for m in func_def.finditer(file_content):
        name = m.group(1)
        if name != target_function_name:
            start = m.start()
            brace = file_content.find('{', start)
            if brace != -1:
                sig = file_content[start:brace].strip() + ' { ... }'
                other_sigs.append(sig)
    if other_sigs:
        parts.append("Other functions in file:\n" + "\n".join(other_sigs[:20]))

    return "\n\n".join(parts)
