import sys
import json
from pathlib import Path
from tree_sitter import Language, Parser

def collect_all_functions(node, all_functions):
    """Recursively collect function nodes using comprehensive create_ground_truth logic."""
    # Regular functions and methods
    if node.type in ("function_declaration", "method_declaration"):
        all_functions.append(node)
    
    # Named function literals from variable declarations
    if node.type == "var_declaration":
        for child in node.children:
            if child.type == "var_spec":
                var_name = None
                function_literal = None
                for vchild in child.children:
                    if vchild.type == "identifier":
                        var_name = vchild.text.decode('utf-8') if isinstance(vchild.text, bytes) else vchild.text
                    elif vchild.type == "expression_list":
                        for expr_child in vchild.children:
                            if expr_child.type == "function_literal":
                                function_literal = expr_child
                                break
                if var_name and function_literal:
                    all_functions.append({
                        'type': 'named_function_literal',
                        'name': var_name,
                        'node': function_literal,
                        'start_point': function_literal.start_point,
                        'end_point': function_literal.end_point
                    })
    
    # Interface methods
    if node.type == "type_declaration":
        for child in node.children:
            if child.type == "type_spec":
                for grandchild in child.children:
                    if grandchild.type == "interface_type":
                        for method in grandchild.children:
                            if method.type == "method_spec":
                                all_functions.append(method)
    
    # Recursively process child nodes
    for child in node.children:
        collect_all_functions(child, all_functions)

def extract_function_name(func_node):
    """Extract function name from function node (matching create_ground_truth logic)."""
    if isinstance(func_node, dict) and func_node.get('type') == 'named_function_literal':
        return func_node.get('name', 'unknown')
    
    if not isinstance(func_node, dict) and hasattr(func_node, 'type') and func_node.type == 'method_spec':
        for child in getattr(func_node, 'children', []):
            if child.type in ['identifier', 'field_identifier']:
                name = child.text
                if isinstance(name, bytes):
                    name = name.decode('utf-8')
                return name.strip()
    
    if not isinstance(func_node, dict) and hasattr(func_node, 'type') and func_node.type == 'function_declaration':
        for child in getattr(func_node, 'children', []):
            if child.type == 'identifier':
                name = child.text
                if isinstance(name, bytes):
                    name = name.decode('utf-8')
                return name.strip()
    
    elif not isinstance(func_node, dict) and hasattr(func_node, 'type') and func_node.type == 'method_declaration':
        found_receiver = False
        method_name = None
        for child in getattr(func_node, 'children', []):
            if child.type == 'parameter_list' and not found_receiver:
                found_receiver = True
                continue
            elif child.type in ['identifier', 'field_identifier'] and found_receiver:
                name = child.text
                if isinstance(name, bytes):
                    name = name.decode('utf-8')
                return name.strip()
    
    return "unknown"

def extract_go_skeleton(file_path, parser):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    tree = parser.parse(bytes(code, "utf8"))
    root = tree.root_node
    skeleton_lines = []
    
    # Collect all function nodes using comprehensive logic
    all_functions = []
    collect_all_functions(root, all_functions)
    
    # Process each function node
    for func_node in all_functions:
        func_name = extract_function_name(func_node)
        if func_name == "unknown":
            continue
            
        # Determine function type and format skeleton
        if isinstance(func_node, dict):
            # Named function literal
            skeleton_lines.append(f"var {func_name} = func(...) {{ ... }}")
        elif hasattr(func_node, 'type'):
            if func_node.type == 'function_declaration':
                skeleton_lines.append(f"func {func_name}(...) {{ ... }}")
            elif func_node.type == 'method_declaration':
                skeleton_lines.append(f"func (recv) {func_name}(...) {{ ... }}")
            elif func_node.type == 'method_spec':
                skeleton_lines.append(f"    {func_name}(...) // interface method")
    
    return "\n".join(skeleton_lines)

def main():
    if len(sys.argv) != 4:
        print("Usage: python function_level_localization.py <proposal_path> <directory_path> <file_path>")
        sys.exit(1)
    proposal_path = Path(sys.argv[1])
    directory_path = sys.argv[2]
    file_path = sys.argv[3]
    # Load Go parser
    GO_LANGUAGE = Language(str(Path(__file__).parent.parent.parent.parent / "build" / "my-languages.so"), "go")
    parser = Parser()
    parser.set_language(GO_LANGUAGE)
    # Extract skeleton view for this file only (per-file skeleton)
    skeleton = extract_go_skeleton(file_path, parser)
    # Limit skeleton to first 100 lines if too large
    MAX_SKELETON_LINES = 100
    skeleton_lines = skeleton.splitlines()
    if len(skeleton_lines) > MAX_SKELETON_LINES:
        skeleton = "\n".join(skeleton_lines[:MAX_SKELETON_LINES]) + "\n... (truncated) ..."
    # Load proposal text
    with open(proposal_path, 'r', encoding='utf-8') as f:
        proposal_text = f.read()
    # Compose prompt (for LLM, strict output format)
    prompt = f'''
You are analyzing a Go proposal and a Go source file to identify which functions are **most relevant** to the given proposal.

### Proposal Content ###
{proposal_text}

### File Information ###
File: {file_path}
Directory: {directory_path}

### File Skeleton (first 100 lines) ###
{skeleton}

**CRITICAL OBJECTIVE**: Identify the **most relevant functions** in this file that are closely related to the proposal topic and discussion.

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
    "FuncName1",
    "FuncName2"
  ]
}}

**MANDATORY SELECTION RULES:**
- Select only the most essential functions, not methods unrelated to the proposal.
- Only include functions that are directly related to the accepted proposal.
- The output must strictly follow the format.
- If you are unsure, make your best guess based on the file skeleton and proposal.
'''.strip()
    print(prompt)

if __name__ == "__main__":
    main()
