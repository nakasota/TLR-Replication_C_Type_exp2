import sys
import json
from pathlib import Path
from tree_sitter import Language, Parser

def extract_go_skeleton(file_path, parser):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    tree = parser.parse(bytes(code, "utf8"))
    root = tree.root_node
    skeleton_lines = []
    
    # Ground Truthと同じロジックで全ての関数を収集
    all_functions = []
    _collect_all_functions(root, all_functions, code)
    
    # 収集した関数をスケルトン形式で出力
    for func_info in all_functions:
        if isinstance(func_info, dict) and func_info.get('type') == 'named_function_literal':
            # 名前付き関数リテラル
            func_name = func_info.get('name', 'unknown')
            skeleton_lines.append(f"var {func_name} = func(...) {{ ... }}")
        else:
            # 通常の関数・メソッド・インターフェースメソッド
            func_node = func_info if not isinstance(func_info, dict) else func_info.get('node')
            if func_node:
                func_name = _extract_function_name(func_node, code)
                
                if func_node.type == "function_declaration":
                    skeleton_lines.append(f"func {func_name}(...) {{ ... }}")
                elif func_node.type == "method_declaration":
                    # レシーバー情報を抽出
                    receiver_type = _extract_receiver_type(func_node, code)
                    recv_display = f"({receiver_type})" if receiver_type else "(recv)"
                    skeleton_lines.append(f"func {recv_display} {func_name}(...) {{ ... }}")
                elif func_node.type == "method_spec":
                    # インターフェースメソッド
                    skeleton_lines.append(f"{func_name}(...)")
    
    return "\n".join(skeleton_lines)

def _collect_all_functions(node, all_functions, code):
    """Ground Truthと同じロジックで関数ノードを収集"""
    # 通常の関数・メソッド
    if node.type in ("function_declaration", "method_declaration"):
        all_functions.append(node)
    
    # 変数宣言から名前付き関数リテラルを検出
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
    
    # インターフェースメソッド
    if node.type == "type_declaration":
        for child in node.children:
            if child.type == "type_spec":
                for grandchild in child.children:
                    if grandchild.type == "interface_type":
                        for method in grandchild.children:
                            if method.type == "method_spec":
                                all_functions.append(method)
    
    # 子ノードを再帰的に処理
    for child in node.children:
        _collect_all_functions(child, all_functions, code)

def _extract_function_name(func_node, code):
    """Ground Truthと同じロジックで関数名を抽出"""
    if hasattr(func_node, 'type') and func_node.type == 'method_spec':
        for child in getattr(func_node, 'children', []):
            if child.type in ['identifier', 'field_identifier']:
                name = child.text
                if isinstance(name, bytes):
                    name = name.decode('utf-8')
                return name.strip()
    elif hasattr(func_node, 'type') and func_node.type == 'function_declaration':
        for child in getattr(func_node, 'children', []):
            if child.type == 'identifier':
                name = child.text
                if isinstance(name, bytes):
                    name = name.decode('utf-8')
                return name.strip()
    elif hasattr(func_node, 'type') and func_node.type == 'method_declaration':
        found_receiver = False
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

def _extract_receiver_type(func_node, code):
    """メソッドのレシーバー型を抽出"""
    for child in func_node.children:
        if child.type == 'parameter_list':
            # 最初のparameter_listはレシーバー
            for param_child in child.children:
                if param_child.type == "parameter_declaration":
                    for type_child in param_child.children:
                        if type_child.type in ["type_identifier", "pointer_type"]:
                            name = type_child.text
                            if isinstance(name, bytes):
                                name = name.decode('utf-8')
                            return name.strip()
            break
    return None

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
    # Use full skeleton view without any truncation
    # Load proposal text
    with open(proposal_path, 'r', encoding='utf-8') as f:
        proposal_content = f.read()
    
    # Format proposal section (consistent with directory and file level)
    proposals_section = f"# Proposal: {proposal_path.name}\n" + proposal_content

    # Define the output format instructions (consistent with directory and file level)
    output_format = """
Return a JSON object with the following format.
The response MUST:
- Be a valid JSON block.
- Contain a key `relevant_functions` with a list of function/method names (strings).
- For methods, use the format "MethodName" (without receiver).
- For interface methods, use the format "MethodName" (method name only).
- For named function literals, use the variable name.
- Output ONLY the raw JSON object. Do NOT include any markdown formatting (no ```json or ```).
- Do NOT add any explanations or additional text.
- If you are unsure which functions apply, return an empty list.

Example of correct output when functions are found:
{
  "relevant_functions": [
    "RegularFunc",
    "MethodName",
    "InterfaceMethod",
    "funcLiteral"
  ]
}

Example of correct output when functions are not found:
{
  "relevant_functions": []
}
""".strip()

    
    # Compose prompt (consistent structure with directory and file level)
    prompt = f'''
You are analyzing a Go proposal and a Go source file to identify which functions and methods are **most relevant** to the given proposal.

### Proposal Content ###
{proposals_section}

### File Information ###
File: {file_path}
Directory: {directory_path}

### File Skeleton ###
```
{skeleton}
```

**CRITICAL OBJECTIVE**: Identify the **most relevant functions and methods** in this file that are closely related to the proposal topic and discussion.

**Step-by-step process:**
1. Read the proposal title and content.
2. Scan the file skeleton above for matching function/method names.
3. Include only those functions/methods you actually see listed.
4. If none match, return an empty list (`[]`).

**WHAT TO INCLUDE:**
- Regular functions (func FuncName(...))
- Methods (func (receiver) MethodName(...))
- Named function literals (var funcVar = func(...))
- Interface methods (methods defined in interface types)

Please output your answer in the following format:
{output_format}
'''.strip()
    print(prompt)

if __name__ == "__main__":
    main()
