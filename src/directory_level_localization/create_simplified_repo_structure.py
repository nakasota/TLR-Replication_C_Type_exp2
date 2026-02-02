#!/usr/bin/env python3
"""
Create simplified repository structure for LLM input from repo_structure_{REPO_SET}.json.
"""

import json
import os
from pathlib import Path
from collections import defaultdict


def build_directory_tree(file_paths, max_files_per_directory=None):
    """
    Build a directory tree structure from file paths.
    """
    tree = {}
    dir_files = defaultdict(list)
    for file_path in file_paths:
        parts = file_path.split('/')
        dir_path = '/'.join(parts[:-1])
        dir_files[dir_path].append(parts[-1])
    for dir_path, files in dir_files.items():
        for f in sorted(files):
            file_path = f"{dir_path}/{f}" if dir_path else f
            parts = file_path.split('/')
            current = tree
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                current = current[part]
            filename = parts[-1]
            current[filename] = None
    return tree


def _format_structure_for_paths(file_paths):
    tree = build_directory_tree(file_paths)
    formatted_structure = format_tree_structure(tree)
    lines = formatted_structure.split('\n') if formatted_structure else []
    return formatted_structure, len(lines)


def _line_indent_level(line):
    return (len(line) - len(line.lstrip(" "))) // 4


def _compute_context_stacks(lines):
    stacks = []
    current = []
    for line in lines:
        indent_level = _line_indent_level(line)
        current = current[:indent_level]
        stacks.append(list(current))
        if line.rstrip().endswith("/"):
            current = current + [line.strip().rstrip("/")]
    return stacks


def _context_lines_from_stack(stack):
    return [("    " * idx) + f"{name}/" for idx, name in enumerate(stack)]


def _split_lines_with_context(lines, max_lines):
    stacks = _compute_context_stacks(lines)
    chunks = []
    index = 0
    while index < len(lines):
        context = _context_lines_from_stack(stacks[index])
        available = max_lines - len(context)
        if available <= 0:
            context = []
            available = max_lines
        chunk_lines = context + lines[index:index + available]
        chunks.append(chunk_lines)
        index += available
    return chunks


def format_tree_structure(tree, indent="", is_root=True):
    result = []
    if is_root:
        indent = ""
    items = sorted(tree.items(), key=lambda x: (x[1] is None, x[0]))
    for name, subtree in items:
        if subtree is None:
            result.append(f"{indent}{name}")
        else:
            result.append(f"{indent}{name}/")
            if subtree:
                result.append(format_tree_structure(subtree, indent + "    ", False))
    return "\n".join(filter(None, result))


def write_structure_files(file_paths, output_dir, max_lines=None):
    output_dir.mkdir(parents=True, exist_ok=True)
    for existing in output_dir.glob("simplified_repo_structure_*.txt"):
        existing.unlink()

    if max_lines is None:
        formatted_structure, _ = _format_structure_for_paths(file_paths)
        output_file = output_dir / "simplified_repo_structure_separate1.txt"
        with open(output_file, 'w') as f:
            f.write(formatted_structure)
        return [output_file]

    formatted_structure, _ = _format_structure_for_paths(file_paths)
    lines = formatted_structure.split('\n') if formatted_structure else []
    chunks = _split_lines_with_context(lines, max_lines)
    output_files = []
    for idx, chunk in enumerate(chunks, 1):
        output_file = output_dir / f"simplified_repo_structure_separate{idx}.txt"
        with open(output_file, 'w') as f:
            f.write("\n".join(chunk))
        output_files.append(output_file)
    return output_files


def create_multiple_versions():
    repo_set = os.environ.get("REPO_SET", "sample_repo").strip()
    input_file = Path(__file__).parent.parent.parent / "data" / "preprocess" / f"repo_structure_{repo_set}.json"
    output_root = Path(__file__).parent / "prompt"

    with open(input_file, 'r') as f:
        data = json.load(f)
    file_paths = sorted(
        path for path in data.keys()
        if path.endswith(".c") or path.endswith(".h")
    )
    if not file_paths:
        raise FileNotFoundError(f"No .c or .h files found in repo_structure_{repo_set}.json")

    versions = [
        ("repository_structure_full", None),
        ("repository_structure_2000", 2000),
        ("repository_structure_1000", 1000),
        ("repository_structure_500", 500),
    ]

    for dir_name, max_lines in versions:
        output_dir = output_root / dir_name
        label = "full" if max_lines is None else f"{max_lines}-line"
        print(f"\n{'='*50}")
        print(f"Creating version: {dir_name} ({label})")
        output_files = write_structure_files(file_paths, output_dir, max_lines=max_lines)
        print(f"Generated {len(output_files)} files in {output_dir}")


def create_single_version(output_dir_name, max_lines=2000):
    """Create one structure directory (e.g. repository_structure_2000_sample_repo) for the current repo."""
    repo_set = os.environ.get("REPO_SET", "sample_repo").strip()
    input_file = Path(__file__).parent.parent.parent / "data" / "preprocess" / f"repo_structure_{repo_set}.json"
    output_root = Path(__file__).parent / "prompt"
    output_dir = output_root / output_dir_name

    with open(input_file, 'r') as f:
        data = json.load(f)
    file_paths = sorted(
        path for path in data.keys()
        if path.endswith(".c") or path.endswith(".h")
    )
    if not file_paths:
        raise FileNotFoundError(f"No .c or .h files found in repo_structure_{repo_set}.json")

    output_files = write_structure_files(file_paths, output_dir, max_lines=max_lines)
    print(f"Generated {len(output_files)} files in {output_dir}")
    return output_files


if __name__ == "__main__":
    import argparse
    import re
    parser = argparse.ArgumentParser(description="Create simplified repo structure for LLM input.")
    parser.add_argument("--output", "-o", metavar="DIR", help="Output dir name (e.g. repository_structure_2000_sample_repo)")
    parser.add_argument("--max-lines", "-n", type=int, default=None, help="Max lines per chunk (default: parse from --output or 2000)")
    args = parser.parse_args()

    if args.output:
        max_lines = args.max_lines
        if max_lines is None:
            if "repository_structure_full_" in args.output:
                max_lines = None  # full = no split
            else:
                m = re.match(r"repository_structure_(\d+)_", args.output)
                max_lines = int(m.group(1)) if m else 2000
        print(f"Creating {args.output} (max_lines={max_lines})...")
        create_single_version(args.output, max_lines=max_lines)
    else:
        os.makedirs(os.path.dirname(__file__) if os.path.dirname(__file__) else ".", exist_ok=True)
        print("Creating simplified repository structure versions...")
        create_multiple_versions()
