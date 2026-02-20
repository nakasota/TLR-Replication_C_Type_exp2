import json
import os
from pathlib import Path
from tree_sitter import Language, Parser

# Load repo structure globally to avoid loading it for each file (cached per REPO_SET)
_repo_structure_cache = {}
_c_parser = None

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


def _get_c_parser():
    global _c_parser
    if _c_parser is None:
        so_path = Path(__file__).parent.parent.parent.parent / 'third_party' / 'tree-sitter-c' / 'tree-sitter-c.so'
        if not so_path.exists():
            raise FileNotFoundError(f"tree-sitter-c.so not found: {so_path}")
        c_language = Language(str(so_path), 'c')
        parser = Parser()
        parser.set_language(c_language)
        _c_parser = parser
    return _c_parser

def analyze_file_with_skeleton(file_path):
    """Extract skeleton view and context for a C file."""
    try:
        repo_structure = get_repo_structure()
        
        # Get file data from repo structure
        if str(file_path) not in repo_structure:
            print(f"[ERROR] File {file_path} not found in repo structure (available files: {len(repo_structure)})")
            return None
        
        file_data = repo_structure[str(file_path)]
        file_content = file_data.get('content', '')
        
        if not file_content:
            print(f"[ERROR] No content found for file {file_path}")
            return None
        
        # Extract skeleton view
        skeleton_view = _extract_file_skeleton(file_content)

        # Extract file context
        context = _extract_file_context(file_content)
        
        return {
            "skeleton_view": skeleton_view,
            "context": context,
            "file_path": str(file_path)
        }
        
    except Exception as e:
        print(f"[ERROR] Failed to analyze file {file_path}: {e}")
        return None

def _extract_file_skeleton(file_content):
    """
    Extract skeleton view (includes, macros, types, function signatures).
    Fallback to regex if tree-sitter fails.
    """
    try:
        # Try to use tree-sitter first
        return _extract_skeleton_with_tree_sitter(file_content)
    except Exception as e:
        print(f"[WARNING] Tree-sitter extraction failed, falling back to regex: {e}")
        return _extract_skeleton_with_regex(file_content)

def _extract_skeleton_with_tree_sitter(file_content):
    parser = _get_c_parser()
    tree = parser.parse(bytes(file_content, "utf8"))
    root_node = tree.root_node

    skeleton_parts = []

    preprocessor = _extract_preprocessor_lines(file_content)
    if preprocessor:
        skeleton_parts.append("\n".join(preprocessor))

    types = _extract_types(root_node, file_content)
    if types:
        skeleton_parts.append("\n\n".join(types))

    signatures = _extract_function_signatures(root_node, file_content)
    if signatures:
        skeleton_parts.append("\n".join(signatures))

    declarations = _extract_function_declarations(root_node, file_content)
    if declarations:
        skeleton_parts.append("\n".join(declarations))

    return "\n\n".join(skeleton_parts)

def _extract_skeleton_with_regex(file_content):
    """Regex fallback for C skeleton extraction."""
    import re
    skeleton_parts = []

    preprocessor = _extract_preprocessor_lines(file_content)
    if preprocessor:
        skeleton_parts.append("\n".join(preprocessor))

    type_pattern = re.compile(r'^\s*(typedef\s+)?(struct|enum|union)\b.*$', re.MULTILINE)
    type_matches = [m.group(0) for m in type_pattern.finditer(file_content)]
    if type_matches:
        skeleton_parts.append("\n".join(type_matches))

    func_def_pattern = re.compile(r'^[\w\s\*]+\s+\w+\s*\([^;]*\)\s*\{', re.MULTILINE)
    func_matches = []
    for match in func_def_pattern.finditer(file_content):
        line = match.group(0)
        line = line[:line.index('{')].strip() + ' { ... }'
        func_matches.append(line)
    if func_matches:
        skeleton_parts.append("\n".join(func_matches))

    func_decl_pattern = re.compile(r'^[\w\s\*]+\s+\w+\s*\([^)]*\)\s*;', re.MULTILINE)
    decl_matches = [m.group(0).strip() for m in func_decl_pattern.finditer(file_content)]
    if decl_matches:
        skeleton_parts.append("\n".join(decl_matches))

    return "\n\n".join(skeleton_parts)


def _extract_includes(code):
    return [line.strip() for line in code.splitlines() if line.strip().startswith("#include")]


def _extract_macros(code):
    return [line.strip() for line in code.splitlines() if line.strip().startswith("#define")]


def _extract_preprocessor_lines(code):
    """Extract #ifndef, #define, #endif, #ifdef, etc. for full include-guard / macro skeleton."""
    return [line.strip() for line in code.splitlines() if line.strip().startswith("#")]


def _collect_nodes_by_type(node, target_type, results):
    if node.type == target_type:
        results.append(node)
    for child in node.children:
        _collect_nodes_by_type(child, target_type, results)


def _get_node_text(node, file_content):
    return file_content[node.start_byte:node.end_byte]


def _find_identifier(node, file_content):
    if node is None:
        return None
    if node.type == "identifier":
        return _get_node_text(node, file_content)
    for child in node.children:
        name = _find_identifier(child, file_content)
        if name:
            return name
    return None


def _extract_types(root_node, file_content):
    results = []
    def visit(node):
        if node.type in ("struct_specifier", "union_specifier", "enum_specifier", "type_definition"):
            results.append(_get_node_text(node, file_content).strip())
        for child in node.children:
            visit(child)
    visit(root_node)
    return results


def _has_function_declarator(node):
    """Return True if this declaration has a function_declarator (e.g. void foo(int x);)."""
    if node.type == "function_declarator":
        return True
    for child in node.children:
        if _has_function_declarator(child):
            return True
    return False


def _extract_function_declarations(root_node, file_content):
    """Extract function declarations (e.g. in .h files): void foo(int x);"""
    results = []
    def visit(node):
        if node.type == "declaration":
            if _has_function_declarator(node):
                results.append(_get_node_text(node, file_content).strip())
        for child in node.children:
            visit(child)
    visit(root_node)
    return results


def _extract_function_signatures(root_node, file_content):
    """Extract function definitions (body) and declarations (no body)."""
    results = []
    def visit(node):
        if node.type == "function_definition":
            body = node.child_by_field_name("body")
            signature = _get_node_text(node, file_content)
            if body is not None:
                signature = file_content[node.start_byte:body.start_byte].strip()
            results.append(signature)
        for child in node.children:
            visit(child)
    visit(root_node)
    return results


def _extract_file_context(file_content):
    context = {
        "includes": _extract_includes(file_content),
        "macros": _extract_macros(file_content),
    }
    return context
