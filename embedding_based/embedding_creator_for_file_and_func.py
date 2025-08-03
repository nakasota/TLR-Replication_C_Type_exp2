#!/usr/bin/env python3
"""
Embedding Creator - Generate file-level and function-level embeddings in batches using OpenAI embedding models.
This script loads `go_repo_structure.json`, counts total files and functions,
then creates embeddings for each file and each function in batches of 1000, printing progress.
Embeddings are saved as pickle files, along with the corresponding file paths and function identifiers.

*Note:* No truncation of file or function content—everything is passed through to the embedder.
"""

import json
import sys
import pickle
from pathlib import Path
from openai_embedding_utils import create_openai_embedding_model


def load_repo_structure(path: Path):
    if not path.exists():
        print(f"❌ Repository structure file not found: {path}")
        sys.exit(1)
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def create_file_text(file_path: str, file_data: dict) -> str:
    text = f"File: {file_path}"
    content = file_data.get('content', '')
    if content:
        # No truncation: include full content
        text += f" Content: {content}"
    return text


def extract_functions(repo: dict) -> list:
    """Extract all functions as (file_path, func_name, func_body) tuples."""
    funcs = []
    for file_path, file_data in repo.items():
        fdict = file_data.get('functions', {})
        if isinstance(fdict, dict):
            for fname, finfo in fdict.items():
                body = finfo.get('content', '') if isinstance(finfo, dict) else ''
                funcs.append((file_path, fname, body))
        elif isinstance(fdict, list):
            for entry in fdict:
                if isinstance(entry, dict):
                    fname = entry.get('name', 'unknown')
                    body = entry.get('content', entry.get('body', ''))
                else:
                    fname = str(entry)
                    body = ''
                funcs.append((file_path, fname, body))
    return funcs


def create_function_text(file_path: str, func_name: str, func_body: str) -> str:
    text = f"Function: {func_name} File: {file_path}"
    if func_body:
        # No truncation: include full function body
        text += f" Code: {func_body}"
    return text


def batch_encode(texts: list, model, batch_size: int) -> list:
    embeddings = []
    total = len(texts)
    for i in range(0, total, batch_size):
        j = min(i + batch_size, total)
        print(f"🔄 Embedding items {i+1}-{j} of {total}...")
        embeddings.extend(model.encode(texts[i:j], show_progress_bar=False))
    return embeddings


def main():
    base = Path(__file__).parent.parent
    repo_file = base / 'data' / 'preprocess' / 'go_repo_structure.json'
    embedding_based_dir = Path(__file__).parent
    output_dir = embedding_based_dir / 'embeddings_cache_openai'
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load repository data
    repo = load_repo_structure(repo_file)
    files = list(repo.keys())
    functions = extract_functions(repo)
    print(f"📁 Total files: {len(files)}")
    print(f"🔧 Total functions: {len(functions)}")

    # Load model
    print(f"🤖 Loading embedding model: text-embedding-3-large")
    model = create_openai_embedding_model('text-embedding-3-large')

    # Batch parameters - smaller batch size to handle token limits better
    batch_size = 50  # Reduced from 1000 to handle large files better

    # File embeddings
    file_texts = [create_file_text(fp, repo[fp]) for fp in files]
    print("\n🏷️  Generating file embeddings...")
    file_embeddings = batch_encode(file_texts, model, batch_size)

    # Function embeddings
    func_texts = [create_function_text(fp, fn, fb) for fp, fn, fb in functions]
    print("\n🏷️  Generating function embeddings...")
    function_embeddings = batch_encode(func_texts, model, batch_size)

    # Save embeddings and identifiers
    with open(output_dir / 'file_embeddings.pkl', 'wb') as ef:
        pickle.dump(file_embeddings, ef)
    with open(output_dir / 'file_paths.pkl', 'wb') as pf:
        pickle.dump(files, pf)

    with open(output_dir / 'function_embeddings.pkl', 'wb') as ef2:
        pickle.dump(function_embeddings, ef2)
    with open(output_dir / 'function_identifiers.pkl', 'wb') as fi:
        # Save list of (file_path, func_name)
        pickle.dump([(fp, fn) for fp, fn, _ in functions], fi)

    print(f"\n💾 Saved {len(file_embeddings)} file embeddings and {len(function_embeddings)} function embeddings to {output_dir}")

if __name__ == '__main__':
    main()
