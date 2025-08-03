import sys
import json
from pathlib import Path

# Load repo structure globally to avoid loading it for each function
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

def analyze_function_relevance(file_path, function_name):
    """
    指定された関数のコードとコンテキストをgo_repo_structure.jsonから抽出する
    """
    try:
        repo_structure = get_repo_structure()
        
        # Get file data from repo structure
        if str(file_path) not in repo_structure:
            print(f"[ERROR] File {file_path} not found in repo structure")
            return None
        
        file_data = repo_structure[str(file_path)]
        
        # Get function data
        if 'functions' not in file_data or function_name not in file_data['functions']:
            print(f"[ERROR] Function {function_name} not found in {file_path}")
            return None
        
        function_data = file_data['functions'][function_name]
        function_code = function_data.get('content', '')
        
        if not function_code:
            print(f"[ERROR] No content found for function {function_name}")
            return None
        
        # Extract context from file content
        file_content = file_data.get('content', '')
        context = _extract_file_context(file_content, function_name)
        
        return {
            "function_code": function_code,
            "context": context
        }
        
    except Exception as e:
        print(f"[ERROR] Failed to analyze function {function_name} in {file_path}: {e}")
        return None

def _extract_file_context(file_content, target_function_name):
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
    
    # Extract type definitions (structs, interfaces, etc.)
    type_defs = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('type '):
            # Collect the type definition
            type_def_lines = [lines[i]]
            i += 1
            # Handle multi-line type definitions
            if i < len(lines) and '{' in lines[i-1]:
                brace_count = lines[i-1].count('{') - lines[i-1].count('}')
                while i < len(lines) and brace_count > 0:
                    type_def_lines.append(lines[i])
                    brace_count += lines[i].count('{') - lines[i].count('}')
                    i += 1
            type_def = '\n'.join(type_def_lines)
            if len(type_def) > 500:
                type_def = type_def[:500] + "..."
            type_defs.append(type_def)
        else:
            i += 1
    
    if type_defs:
        context_parts.append(f"Type Definitions:\n{chr(10).join(type_defs)}")
    
    # Extract constants and variables
    const_var_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('const ') or line.startswith('var '):
            if '(' in line:
                # Multi-line const/var block
                const_var_lines.append(lines[i])
                i += 1
                while i < len(lines) and not lines[i].strip().endswith(')'):
                    const_var_lines.append(lines[i])
                    i += 1
                if i < len(lines):
                    const_var_lines.append(lines[i])  # Add closing )
            else:
                # Single line const/var
                const_var_lines.append(lines[i])
        i += 1
    
    if const_var_lines:
        const_vars = '\n'.join(const_var_lines)
        if len(const_vars) > 300:
            const_vars = const_vars[:300] + "..."
        context_parts.append(f"Constants/Variables:\n{const_vars}")
    
    # Extract other function signatures (excluding the target function)
    other_functions = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('func '):
            # Extract function name to check if it's the target function
            func_name = _extract_func_name_from_line(line)
            if func_name != target_function_name:
                # Extract just the signature
                signature = line
                if '{' not in line and i + 1 < len(lines):
                    # Multi-line function signature
                    j = i + 1
                    while j < len(lines) and '{' not in lines[j]:
                        signature += '\n' + lines[j].strip()
                        j += 1
                    if j < len(lines) and '{' in lines[j]:
                        signature += '\n' + lines[j].split('{')[0] + '{ ... }'
                else:
                    signature = signature.split('{')[0] + '{ ... }'
                other_functions.append(signature)
        i += 1
    
    if other_functions:
        context_parts.append(f"Other Functions in File:\n{chr(10).join(other_functions)}")
    
    return "\n\n".join(context_parts)

def _extract_func_name_from_line(line):
    """Extract function name from a function declaration line"""
    try:
        # Handle regular functions: func FuncName(
        # Handle methods: func (receiver) MethodName(
        parts = line.split('(')
        if len(parts) >= 2:
            before_paren = parts[0].strip()
            if before_paren.startswith('func '):
                remaining = before_paren[5:].strip()  # Remove 'func '
                # Check if it's a method (starts with parentheses for receiver)
                if remaining.startswith('('):
                    # It's a method, find the method name after receiver
                    receiver_end = remaining.find(')')
                    if receiver_end != -1:
                        method_part = remaining[receiver_end+1:].strip()
                        return method_part.split()[0] if method_part else "unknown"
                else:
                    # Regular function
                    return remaining.split()[0] if remaining else "unknown"
        return "unknown"
    except:
        return "unknown"


