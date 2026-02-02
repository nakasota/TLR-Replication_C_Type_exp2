import argparse
import json
import os
from pathlib import Path

from tree_sitter import Language, Parser


def _build_c_language(so_path: Path, grammar_dir: Path) -> Language:
    if not so_path.exists():
        if not grammar_dir.exists():
            raise FileNotFoundError(f"tree-sitter-c directory not found: {grammar_dir}")
        so_path.parent.mkdir(parents=True, exist_ok=True)
        Language.build_library(str(so_path), [str(grammar_dir)])
    return Language(str(so_path), "c")


def _iter_c_files(root_dir: Path, exts=(".c", ".h")):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(exts):
                yield Path(dirpath) / filename


def _node_text(node, code: str) -> str:
    return code[node.start_byte:node.end_byte]


def _find_identifier(node, code: str):
    if node is None:
        return None
    if node.type == "identifier":
        return _node_text(node, code)
    for child in node.children:
        name = _find_identifier(child, code)
        if name:
            return name
    return None


def _collect_nodes_by_type(node, target_type: str, results: list):
    if node.type == target_type:
        results.append(node)
    for child in node.children:
        _collect_nodes_by_type(child, target_type, results)


def _extract_function_definitions(root_node, code: str):
    functions = {}

    def visit(node):
        if node.type == "function_definition":
            declarator = node.child_by_field_name("declarator")
            name = _find_identifier(declarator, code)
            if name:
                body = node.child_by_field_name("body")
                signature = _node_text(node, code)
                if body is not None:
                    signature = code[node.start_byte:body.start_byte].strip()
                function_data = {
                    "name": name,
                    "signature": signature,
                    "content": _node_text(node, code),
                    "start_point": node.start_point,
                    "end_point": node.end_point,
                }
                functions.setdefault(name, []).append(function_data)
        for child in node.children:
            visit(child)

    visit(root_node)
    return functions


def _extract_function_declarations(root_node, code: str, defined_names: set):
    declarations = {}

    def visit(node):
        if node.type == "declaration":
            declarators = []
            _collect_nodes_by_type(node, "function_declarator", declarators)
            for declarator in declarators:
                name = _find_identifier(declarator, code)
                if not name or name in defined_names:
                    continue
                signature = _node_text(node, code).strip()
                if signature.endswith(";"):
                    signature = signature[:-1].strip()
                decl_data = {
                    "name": name,
                    "signature": signature,
                    "start_point": node.start_point,
                    "end_point": node.end_point,
                }
                declarations.setdefault(name, []).append(decl_data)
        for child in node.children:
            visit(child)

    visit(root_node)
    return declarations


def _process_file(file_path: Path, parser: Parser, root_dir: Path):
    try:
        code = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        code = file_path.read_text(encoding="utf-8", errors="replace")
    tree = parser.parse(bytes(code, "utf8"))
    root_node = tree.root_node
    functions = _extract_function_definitions(root_node, code)
    declarations = _extract_function_declarations(root_node, code, set(functions.keys()))
    rel_path = file_path.relative_to(root_dir).as_posix()
    return rel_path, {
        "content": code,
        "functions": functions,
        "function_declarations": declarations,
    }


def main():
    parser = argparse.ArgumentParser(description="Tree-sitterでCリポジトリ構造を出力")
    parser.add_argument("root_dir", help="Cプロジェクトのルートディレクトリ")
    parser.add_argument("-o", "--output", default="c_repo_structure.json", help="出力ファイル名")
    parser.add_argument(
        "--so",
        default=str(Path(__file__).parent.parent.parent / "third_party" / "tree-sitter-c" / "tree-sitter-c.so"),
        help="tree-sitter-cのビルド済みsoファイルパス",
    )
    parser.add_argument(
        "--grammar-dir",
        default=str(Path(__file__).parent.parent.parent / "third_party" / "tree-sitter-c" / "grammar"),
        help="tree-sitter-c grammarディレクトリ",
    )
    args = parser.parse_args()

    root_dir = Path(args.root_dir).resolve()
    if not root_dir.exists():
        raise FileNotFoundError(f"C repository root not found: {root_dir}")
    so_path = Path(args.so).resolve()
    grammar_dir = Path(args.grammar_dir).resolve()

    c_language = _build_c_language(so_path, grammar_dir)
    ts_parser = Parser()
    ts_parser.set_language(c_language)

    result = {}
    c_files = list(_iter_c_files(root_dir))
    if not c_files:
        raise FileNotFoundError(f"No .c or .h files found under: {root_dir}")
    for file_path in c_files:
        rel_path, file_data = _process_file(file_path, ts_parser, root_dir)
        result[rel_path] = file_data

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"構造を {args.output} に出力しました")


if __name__ == "__main__":
    main()
