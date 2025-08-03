import sys
import json
from pathlib import Path
from tree_sitter import Language, Parser

# Load repo structure globally to avoid loading it for each file
_repo_structure = None

def get_repo_structure():
    """Load repo structure once and cache it"""
    global _repo_structure
    if _repo_structure is None:
        repo_structure_path = Path(__file__).parent.parent.parent.parent / 'data' / 'preprocess' / 'go_repo_structure.json'
        try:
            with open(repo_structure_path, 'r') as f:
                _repo_structure = json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load repo structure: {e}")
            _repo_structure = {}
    return _repo_structure

def analyze_file_with_skeleton(file_path):
    """
    指定されたファイルのskeleton viewとコンテキストを抽出する
    """
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
        
        # Extract file context (package, imports, type definitions)
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
    ファイルのskeleton viewを生成する（function_level_localizationと同じロジック）
    関数シグネチャのみを抽出
    """
    # Tree-sitterを使用してGoコードを解析
    try:
        # Load Go language
        language_path = Path(__file__).parent.parent.parent.parent / 'my-languages.so'
        GO_LANGUAGE = Language(str(language_path), "go")
        parser = Parser()
        parser.set_language(GO_LANGUAGE)
        
        tree = parser.parse(bytes(file_content, "utf8"))
        root = tree.root_node
        
        skeleton_lines = []
        
        # Ground Truthと同じロジックで全ての関数を収集
        all_functions = []
        _collect_all_functions(root, all_functions, file_content)
        
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
                    func_name = _extract_function_name(func_node, file_content)
                    
                    if func_node.type == "function_declaration":
                        skeleton_lines.append(f"func {func_name}(...) {{ ... }}")
                    elif func_node.type == "method_declaration":
                        # レシーバー情報を抽出
                        receiver_type = _extract_receiver_type(func_node, file_content)
                        recv_display = f"({receiver_type})" if receiver_type else "(recv)"
                        skeleton_lines.append(f"func {recv_display} {func_name}(...) {{ ... }}")
                    elif func_node.type == "method_spec":
                        # インターフェースメソッド
                        skeleton_lines.append(f"{func_name}(...)")
        
        return "\n".join(skeleton_lines)
        
    except Exception as e:
        print(f"[ERROR] Failed to extract skeleton: {e}")
        return _fallback_skeleton_extraction(file_content)

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

def _fallback_skeleton_extraction(file_content):
    """Tree-sitterが失敗した場合のフォールバック"""
    lines = file_content.split('\n')
    result_lines = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('func '):
            # Extract function name and create skeleton
            if '(' in line and ')' in line:
                func_part = line.split('(')[0]
                if 'func ' in func_part:
                    func_name = func_part.split('func ')[-1].strip()
                    result_lines.append(f"func {func_name}(...) {{ ... }}")
    
    return '\n'.join(result_lines)

def _extract_file_context(file_content):
    """
    ファイルの内容から関数のコンテキスト（パッケージ、インポート、型定義など）を抽出
    """
    context_parts = []
    lines = file_content.split('\n')
    
    # Extract package declaration
    for line in lines[:10]:  # Package should be in first few lines
        if line.strip().startswith('package '):
            context_parts.append(f"Package: {line.strip()}")
            break
    
    # Extract imports
    import_lines = []
    in_import_block = False
    for line in lines:
        line = line.strip()
        if line.startswith('import '):
            if '(' in line:
                in_import_block = True
                import_lines.append(line)
            else:
                import_lines.append(line)
        elif in_import_block:
            import_lines.append(line)
            if line == ')':
                in_import_block = False
        elif line.startswith('import') and not line.startswith('import '):
            continue
    
    if import_lines:
        context_parts.append(f"Imports:\n{chr(10).join(import_lines)}")
    
    return '\n'.join(context_parts)
