#!/usr/bin/env python3
"""
Cost Calculator for Embedding-Based Localization
Calculates the costs for running:
1. embedding_creator_for_file_and_func.py
2. embedding_based_localization_full.py

Based on text-embedding-3-large pricing: $0.13 per 1M tokens
"""

import json
import glob
import pickle
from pathlib import Path
from openai_embedding_utils import create_openai_embedding_model

# Import tiktoken for accurate token counting
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("Warning: tiktoken not available. Using fallback estimation.")

# Pricing information
PRICE_PER_1M_TOKENS = 0.13  # USD for text-embedding-3-large

# Global model instance to avoid repeated initialization
_model_instance = None
_tiktoken_encoder = None

def get_tiktoken_encoder():
    """Get tiktoken encoder for text-embedding-3-large"""
    global _tiktoken_encoder
    if _tiktoken_encoder is None and TIKTOKEN_AVAILABLE:
        try:
            # text-embedding-3-large uses the same encoding as gpt-4
            _tiktoken_encoder = tiktoken.encoding_for_model("text-embedding-3-large")
        except:
            try:
                # Fallback to cl100k_base
                _tiktoken_encoder = tiktoken.get_encoding("cl100k_base")
            except:
                _tiktoken_encoder = None
    return _tiktoken_encoder

def get_token_counter():
    """Get a shared model instance for token counting"""
    global _model_instance
    if _model_instance is None:
        try:
            _model_instance = create_openai_embedding_model('text-embedding-3-large')
        except Exception as e:
            print(f"Warning: Could not initialize OpenAI model for token counting: {e}")
            _model_instance = None
    return _model_instance

def count_tokens_accurate(text: str) -> int:
    """Count tokens using the most accurate method available"""
    # Method 1: Use tiktoken directly (most accurate)
    if TIKTOKEN_AVAILABLE:
        encoder = get_tiktoken_encoder()
        if encoder:
            try:
                return len(encoder.encode(text))
            except Exception as e:
                print(f"Warning: tiktoken encoding failed: {e}")
    
    # Method 2: Use OpenAI utils (also uses tiktoken internally)
    model = get_token_counter()
    if model:
        try:
            return model.count_tokens(text)
        except Exception as e:
            print(f"Warning: OpenAI utils token counting failed: {e}")
    
    # Method 3: Fallback estimation (4 chars per token)
    return len(text) // 4

def load_repo_structure(path: Path):
    """Load the repository structure"""
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)

def create_file_text(file_path: str, file_data: dict) -> str:
    """Create file text same as in embedding_creator_for_file_and_func.py"""
    text = f"File: {file_path}"
    content = file_data.get('content', '')
    if content:
        text += f" Content: {content}"
    return text

def extract_functions(repo: dict) -> list:
    """Extract functions same as in embedding_creator_for_file_and_func.py"""
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
    """Create function text same as in embedding_creator_for_file_and_func.py"""
    text = f"Function: {func_name} File: {file_path}"
    if func_body:
        text += f" Code: {func_body}"
    return text

def calculate_embedding_creation_cost():
    """Calculate cost for embedding_creator_for_file_and_func.py"""
    print("=" * 60)
    print("📊 COST CALCULATION: embedding_creator_for_file_and_func.py")
    print("=" * 60)
    
    # Load repository data
    base = Path(__file__).parent.parent
    repo_file = base / 'data' / 'preprocess' / 'go_repo_structure.json'
    repo = load_repo_structure(repo_file)
    
    files = list(repo.keys())
    functions = extract_functions(repo)
    
    print(f"📁 Total files: {len(files):,}")
    print(f"🔧 Total functions: {len(functions):,}")
    
    # Calculate file embedding costs
    print("\n--- FILE EMBEDDINGS ---")
    file_texts = [create_file_text(fp, repo[fp]) for fp in files]
    file_tokens = [count_tokens_accurate(text) for text in file_texts]
    
    total_file_tokens = sum(file_tokens)
    file_cost = (total_file_tokens / 1_000_000) * PRICE_PER_1M_TOKENS
    
    print(f"Total file tokens: {total_file_tokens:,}")
    print(f"Average tokens per file: {total_file_tokens // len(files):,}")
    print(f"Max tokens in a file: {max(file_tokens):,}")
    print(f"Min tokens in a file: {min(file_tokens):,}")
    print(f"File embedding cost: ${file_cost:.4f}")
    
    # Calculate function embedding costs
    print("\n--- FUNCTION EMBEDDINGS ---")
    func_texts = [create_function_text(fp, fn, fb) for fp, fn, fb in functions]
    func_tokens = [count_tokens_accurate(text) for text in func_texts]
    
    total_func_tokens = sum(func_tokens)
    func_cost = (total_func_tokens / 1_000_000) * PRICE_PER_1M_TOKENS
    
    print(f"Total function tokens: {total_func_tokens:,}")
    print(f"Average tokens per function: {total_func_tokens // len(functions):,}")
    print(f"Max tokens in a function: {max(func_tokens):,}")
    print(f"Min tokens in a function: {min(func_tokens):,}")
    print(f"Function embedding cost: ${func_cost:.4f}")
    
    # Total cost
    total_cost = file_cost + func_cost
    print(f"\n--- TOTAL EMBEDDING CREATION COST ---")
    print(f"File embeddings: ${file_cost:.4f}")
    print(f"Function embeddings: ${func_cost:.4f}")
    print(f"TOTAL: ${total_cost:.4f}")
    
    return {
        'file_count': len(files),
        'function_count': len(functions),
        'file_tokens': total_file_tokens,
        'function_tokens': total_func_tokens,
        'file_cost': file_cost,
        'function_cost': func_cost,
        'total_cost': total_cost
    }

def calculate_localization_cost():
    """Calculate cost for embedding_based_localization_full.py"""
    print("\n" + "=" * 60)
    print("📊 COST CALCULATION: embedding_based_localization_full.py")
    print("=" * 60)
    
    # Load proposals
    base = Path(__file__).parent.parent
    proposals_dir = base / 'data' / 'preprocess' / 'accepted_proposals'
    proposals = sorted(glob.glob(str(proposals_dir / '*.md')))
    
    print(f"📄 Total proposals: {len(proposals):,}")
    
    # Calculate proposal embedding costs
    proposal_texts = []
    for prop in proposals:
        with open(prop, 'r', encoding='utf-8') as f:
            proposal_texts.append(f.read())
    
    proposal_tokens = [count_tokens_accurate(text) for text in proposal_texts]
    total_proposal_tokens = sum(proposal_tokens)
    proposal_cost = (total_proposal_tokens / 1_000_000) * PRICE_PER_1M_TOKENS
    
    print(f"Total proposal tokens: {total_proposal_tokens:,}")
    print(f"Average tokens per proposal: {total_proposal_tokens // len(proposals):,}")
    print(f"Max tokens in a proposal: {max(proposal_tokens):,}")
    print(f"Min tokens in a proposal: {min(proposal_tokens):,}")
    print(f"Proposal embedding cost: ${proposal_cost:.4f}")
    
    return {
        'proposal_count': len(proposals),
        'proposal_tokens': total_proposal_tokens,
        'proposal_cost': proposal_cost
    }

def check_existing_embeddings():
    """Check if embeddings already exist and estimate saved costs"""
    print("\n" + "=" * 60)
    print("💾 EXISTING EMBEDDINGS CHECK")
    print("=" * 60)
    
    embedding_dir = Path(__file__).parent / 'embeddings_cache_openai'
    
    files_exist = (embedding_dir / 'file_embeddings.pkl').exists()
    functions_exist = (embedding_dir / 'function_embeddings.pkl').exists()
    
    if files_exist:
        print("✅ File embeddings already exist")
        with open(embedding_dir / 'file_paths.pkl', 'rb') as f:
            cached_files = pickle.load(f)
        print(f"   Cached files: {len(cached_files):,}")
    else:
        print("❌ File embeddings do not exist")
    
    if functions_exist:
        print("✅ Function embeddings already exist")
        with open(embedding_dir / 'function_identifiers.pkl', 'rb') as f:
            cached_functions = pickle.load(f)
        print(f"   Cached functions: {len(cached_functions):,}")
    else:
        print("❌ Function embeddings do not exist")
    
    # Check summary if available
    summary_file = embedding_dir / 'embedding_creation_summary.json'
    if summary_file.exists():
        print("\n📋 Previous embedding creation summary:")
        with open(summary_file, 'r') as f:
            summary = json.load(f)
        print(f"   Files processed: {summary.get('total_files_processed', 'N/A'):,}")
        print(f"   Functions processed: {summary.get('total_functions_processed', 'N/A'):,}")
        print(f"   Created at: {summary.get('created_at', 'N/A')}")
    
    return files_exist, functions_exist

def main():
    print("💰 OpenAI Embedding Cost Calculator")
    print(f"💳 Pricing: ${PRICE_PER_1M_TOKENS} per 1M tokens (text-embedding-3-large)")
    print()
    
    # Check existing embeddings
    files_exist, functions_exist = check_existing_embeddings()
    
    # Calculate embedding creation costs
    creation_costs = calculate_embedding_creation_cost()
    
    # Calculate localization costs
    localization_costs = calculate_localization_cost()
    
    # Summary
    print("\n" + "=" * 60)
    print("💰 COST SUMMARY")
    print("=" * 60)
    
    if files_exist and functions_exist:
        print("🎉 All embeddings already exist - no creation cost needed!")
        print(f"💸 Cost if recreated: ${creation_costs['total_cost']:.4f}")
    else:
        needed_cost = 0
        if not files_exist:
            needed_cost += creation_costs['file_cost']
            print(f"📁 File embeddings needed: ${creation_costs['file_cost']:.4f}")
        if not functions_exist:
            needed_cost += creation_costs['function_cost']
            print(f"🔧 Function embeddings needed: ${creation_costs['function_cost']:.4f}")
        print(f"💸 Total creation cost needed: ${needed_cost:.4f}")
    
    print(f"🔍 Localization cost per run: ${localization_costs['proposal_cost']:.4f}")
    
    # Breakdown
    print(f"\n📊 Detailed breakdown:")
    print(f"   Files to embed: {creation_costs['file_count']:,} ({creation_costs['file_tokens']:,} tokens)")
    print(f"   Functions to embed: {creation_costs['function_count']:,} ({creation_costs['function_tokens']:,} tokens)")
    print(f"   Proposals to process: {localization_costs['proposal_count']:,} ({localization_costs['proposal_tokens']:,} tokens)")
    
    total_tokens = creation_costs['file_tokens'] + creation_costs['function_tokens'] + localization_costs['proposal_tokens']
    print(f"   Total tokens: {total_tokens:,}")
    print(f"   Total potential cost: ${(total_tokens / 1_000_000) * PRICE_PER_1M_TOKENS:.4f}")

if __name__ == '__main__':
    main()
