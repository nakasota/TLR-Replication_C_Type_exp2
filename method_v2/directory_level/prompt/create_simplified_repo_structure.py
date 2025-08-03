#!/usr/bin/env python3
"""
Create simplified repository structure for LLM input from go_repo_structure.json

This script converts the detailed repository structure to a simplified tree format
that reduces token size while preserving directory hierarchy information.
"""

import json
import os
from pathlib import Path
from collections import defaultdict
import random


def build_directory_tree(file_paths, max_files_per_directory=None):
    """
    Build a directory tree structure from file paths, with optional random sampling of files per directory.
    
    Args:
        file_paths (list): List of file paths
        max_files_per_directory (int, optional): Max number of files to keep per directory
        
    Returns:
        dict: Nested dictionary representing directory tree
    """
    tree = {}
    dir_files = defaultdict(list)
    # Group files by directory
    for file_path in file_paths:
        parts = file_path.split('/')
        dir_path = '/'.join(parts[:-1])
        dir_files[dir_path].append(parts[-1])
    # Sample files per directory
    sampled_file_paths = []
    for dir_path, files in dir_files.items():
        if max_files_per_directory and len(files) > max_files_per_directory:
            sampled = random.sample(files, max_files_per_directory)
        else:
            sampled = files
        for f in sampled:
            if dir_path:
                sampled_file_paths.append(f"{dir_path}/{f}")
            else:
                sampled_file_paths.append(f)
    # Build tree from sampled files
    for file_path in sampled_file_paths:
        parts = file_path.split('/')
        current = tree
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        filename = parts[-1]
        current[filename] = None
    return tree


def format_tree_structure(tree, indent="", is_root=True):
    """
    Format the tree structure into a readable string format.
    
    Args:
        tree (dict): Directory tree structure
        indent (str): Current indentation level
        is_root (bool): Whether this is the root level
        
    Returns:
        str: Formatted tree structure
    """
    result = []
    
    # Don't add artificial "go/" root since paths don't start with it
    if is_root:
        indent = ""
    
    # Sort items: directories first, then files
    items = sorted(tree.items(), key=lambda x: (x[1] is None, x[0]))
    
    for name, subtree in items:
        if subtree is None:  # It's a file
            result.append(f"{indent}{name}")
        else:  # It's a directory
            result.append(f"{indent}{name}/")
            if subtree:  # If directory has contents
                result.append(format_tree_structure(subtree, indent + "    ", False))
    
    return "\n".join(filter(None, result))


def create_simplified_structure(input_file, output_file, max_depth=None, max_files_per_directory=None):
    """
    Create simplified repository structure from detailed JSON, with optional file sampling per directory.
    
    Args:
        input_file (str): Path to go_repo_structure.json
        output_file (str): Path to output simplified structure
        max_depth (int, optional): Maximum directory depth to include
        max_files_per_directory (int, optional): Max number of files to keep per directory
    """
    print(f"Reading repository structure from {input_file}...")
    
    # Read file paths from JSON (we only need the keys)
    file_paths = []
    
    # Since the file is very large (146MB), we'll read it in chunks
    # and extract only the keys (file paths)
    with open(input_file, 'r') as f:
        # Read the file and extract keys
        print("Extracting file paths...")
        data = json.load(f)
        file_paths = list(data.keys())
    
    print(f"Found {len(file_paths)} files")
    
    # Filter by depth if specified
    if max_depth:
        filtered_paths = []
        for path in file_paths:
            if path.count('/') <= max_depth:
                filtered_paths.append(path)
        file_paths = filtered_paths
        print(f"After depth filtering (max_depth={max_depth}): {len(file_paths)} files")
    
    # Build directory tree
    print("Building directory tree...")
    tree = build_directory_tree(file_paths, max_files_per_directory)
    
    # Format as tree structure
    print("Formatting tree structure...")
    formatted_structure = format_tree_structure(tree)
    
    # Write to output file
    with open(output_file, 'w') as f:
        f.write(formatted_structure)
    
    print(f"Simplified repository structure saved to {output_file}")
    
    # Print statistics
    lines = formatted_structure.split('\n')
    print(f"Generated structure has {len(lines)} lines")
    print(f"Estimated token count: ~{len(formatted_structure.split())} tokens")
    
    return formatted_structure


def create_multiple_versions():
    """Create multiple versions with different depth limits for comparison."""
    input_file = "../../../data/preprocess/go_repo_structure.json"
    versions = [
        (None, "simplified_repo_structure_full.txt"),
        (3, "simplified_repo_structure_depth3.txt"),
        (2, "simplified_repo_structure_depth2.txt"),
        (1, "simplified_repo_structure_depth1.txt"),
    ]
    # Add the limited version (no depth limit, but with file sampling)
    limited_output = "simplified_repo_structure_limited.txt"
    print(f"\n{'='*50}")
    print(f"Creating version: {limited_output}")
    print(f"Max depth: unlimited, max_files_per_directory: 5")
    try:
        structure = create_simplified_structure(input_file, limited_output, None, max_files_per_directory=5)
        lines = structure.split('\n')
        print(f"\nPreview (first 20 lines):")
        for i, line in enumerate(lines[:20]):
            print(line)
        if len(lines) > 20:
            print("...")
    except Exception as e:
        print(f"Error creating {limited_output}: {e}")
    # Now create the other versions (all with file sampling)
    for max_depth, output_file in versions:
        print(f"\n{'='*50}")
        print(f"Creating version: {output_file}")
        print(f"Max depth: {max_depth if max_depth else 'unlimited'}, max_files_per_directory: 5")
        try:
            structure = create_simplified_structure(input_file, output_file, max_depth, max_files_per_directory=5)
            lines = structure.split('\n')
            print(f"\nPreview (first 20 lines):")
            for i, line in enumerate(lines[:20]):
                print(line)
            if len(lines) > 20:
                print("...")
        except Exception as e:
            print(f"Error creating {output_file}: {e}")


if __name__ == "__main__":
    # Create the current directory if it doesn't exist
    os.makedirs(os.path.dirname(__file__) if os.path.dirname(__file__) else ".", exist_ok=True)
    
    print("Creating simplified repository structure versions...")
    create_multiple_versions() 