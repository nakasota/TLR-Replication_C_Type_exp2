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
    def visit(node, indent=0):
        if node.type == "function_declaration":
            func_name = None
            for child in node.children:
                if child.type == "identifier":
                    func_name = code[child.start_byte:child.end_byte]
            skeleton_lines.append(" " * indent + f"func {func_name}(...) {{ ... }}")
        elif node.type == "method_declaration":
            method_name = None
            for child in node.children:
                if child.type == "field_identifier":
                    method_name = code[child.start_byte:child.end_byte]
            skeleton_lines.append(" " * indent + f"func (recv) {method_name}(...) {{ ... }}")
        for child in node.children:
            visit(child, indent)
    visit(root)
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
