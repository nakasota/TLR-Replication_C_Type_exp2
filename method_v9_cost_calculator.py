#!/usr/bin/env python3
"""
Method v9 GPT-4o Cost Calculator and Instrumentation
Calculates and tracks costs for method_v9 GPT-4o usage:
1. directory_and_file_level/main.py (using repository_structure_2000)
2. directory_and_file_level/main_1000.py (using repository_structure_1000) 
3. function_level/main.py

GPT-4o Pricing:
- Input: $2.50 per 1M tokens
- Cached input: $1.25 per 1M tokens  
- Output: $10.00 per 1M tokens
"""

import json
import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime

# Import tiktoken for accurate token counting
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("Warning: tiktoken not available. Using fallback estimation.")

# GPT-4o pricing (per 1M tokens)
GPT4O_INPUT_PRICE = 2.50
GPT4O_CACHED_INPUT_PRICE = 1.25
GPT4O_OUTPUT_PRICE = 10.00

def count_tokens_gpt4o(text: str) -> int:
    """Count tokens for GPT-4o using tiktoken (most accurate)"""
    if TIKTOKEN_AVAILABLE:
        try:
            # GPT-4o uses the same tokenizer as GPT-4
            tokenizer = tiktoken.encoding_for_model("gpt-4")
            return len(tokenizer.encode(text))
        except:
            try:
                # Fallback to cl100k_base encoding
                tokenizer = tiktoken.get_encoding("cl100k_base")
                return len(tokenizer.encode(text))
            except Exception as e:
                print(f"Warning: tiktoken failed: {e}")
    
    # Fallback: rough estimation (4 chars per token for GPT-4 family)
    return len(text) // 4

def estimate_tokens_gpt4o(text: str) -> int:
    """Estimate tokens for GPT-4o (rough estimation: ~4 characters per token)"""
    return len(text) // 4

def estimate_repository_structure_tokens():
    """Estimate tokens in repository structure files"""
    print("=" * 60)
    print("📊 REPOSITORY STRUCTURE TOKEN ESTIMATION")
    print("=" * 60)
    
    base_dir = Path(__file__).parent.parent / 'method_v9' / 'directory_and_file_level' / 'prompt'
    
    # Check repository_structure_1000
    structure_1000_dir = base_dir / 'repository_structure_1000'
    structure_2000_dir = base_dir / 'repository_structure_2000'
    
    results = {}
    
    for name, structure_dir in [("1000", structure_1000_dir), ("2000", structure_2000_dir)]:
        if structure_dir.exists():
            structure_files = list(structure_dir.glob('simplified_repo_structure_separate*.txt'))
            print(f"\n📁 Repository Structure {name}:")
            print(f"   Files found: {len(structure_files)}")
            
            total_tokens = 0
            for sf in structure_files:
                with open(sf, 'r', encoding='utf-8') as f:
                    content = f.read()
                tokens = count_tokens_gpt4o(content)
                total_tokens += tokens
                print(f"   {sf.name}: {tokens:,} tokens")
            
            results[name] = {
                'files': len(structure_files),
                'total_tokens': total_tokens,
                'avg_tokens_per_file': total_tokens // len(structure_files) if structure_files else 0
            }
            print(f"   Total tokens: {total_tokens:,}")
            print(f"   Average per file: {total_tokens // len(structure_files):,}" if structure_files else "   No files found")
        else:
            print(f"\n❌ Repository Structure {name} directory not found: {structure_dir}")
            results[name] = {'files': 0, 'total_tokens': 0, 'avg_tokens_per_file': 0}
    
    return results

def estimate_proposal_tokens():
    """Estimate tokens in proposal files"""
    print("\n" + "=" * 60)
    print("📄 PROPOSAL TOKEN ESTIMATION")
    print("=" * 60)
    
    proposals_dir = Path(__file__).parent.parent / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals'
    
    if not proposals_dir.exists():
        print(f"❌ Proposals directory not found: {proposals_dir}")
        return {'count': 0, 'total_tokens': 0, 'avg_tokens': 0}
    
    proposal_files = list(proposals_dir.glob('*.md'))
    print(f"📄 Proposal files found: {len(proposal_files)}")
    
    total_tokens = 0
    token_counts = []
    
    for pf in proposal_files[:10]:  # Sample first 10 for detailed analysis
        with open(pf, 'r', encoding='utf-8') as f:
            content = f.read()
        tokens = count_tokens_gpt4o(content)
        total_tokens += tokens
        token_counts.append(tokens)
        print(f"   {pf.name}: {tokens:,} tokens")
    
    if len(proposal_files) > 10:
        print(f"   ... and {len(proposal_files) - 10} more files")
        # Estimate remaining files
        avg_so_far = total_tokens / min(10, len(proposal_files))
        estimated_remaining = avg_so_far * (len(proposal_files) - 10)
        total_tokens += estimated_remaining
    
    return {
        'count': len(proposal_files),
        'total_tokens': int(total_tokens),
        'avg_tokens': int(total_tokens / len(proposal_files)) if proposal_files else 0,
        'max_tokens': max(token_counts) if token_counts else 0,
        'min_tokens': min(token_counts) if token_counts else 0
    }

def estimate_function_level_costs():
    """Estimate costs for function_level processing"""
    print("\n" + "=" * 60)
    print("🔧 FUNCTION LEVEL COST ESTIMATION")
    print("=" * 60)
    
    # For function level, we need to check the go_repo_structure.json for function count
    repo_structure_file = Path(__file__).parent.parent / 'data' / 'preprocess' / 'go_repo_structure.json'
    
    if not repo_structure_file.exists():
        print(f"❌ Repository structure file not found: {repo_structure_file}")
        return {'functions': 0, 'estimated_input_tokens': 0, 'estimated_output_tokens': 0}
    
    with open(repo_structure_file, 'r') as f:
        repo_data = json.load(f)
    
    function_count = 0
    total_function_tokens = 0
    
    # Sample some functions to estimate token usage
    sample_functions = []
    for file_path, file_data in list(repo_data.items())[:10]:  # Sample first 10 files
        functions = file_data.get('functions', {})
        if isinstance(functions, dict):
            for func_name, func_info in functions.items():
                function_count += 1
                if len(sample_functions) < 50:  # Sample first 50 functions
                    func_body = func_info.get('content', '') if isinstance(func_info, dict) else ''
                    func_text = f"Function: {func_name} File: {file_path} Code: {func_body}"
                    tokens = count_tokens_gpt4o(func_text)
                    total_function_tokens += tokens
                    sample_functions.append(tokens)
    
    # Count total functions in entire repository
    total_functions = 0
    for file_path, file_data in repo_data.items():
        functions = file_data.get('functions', {})
        if isinstance(functions, dict):
            total_functions += len(functions)
        elif isinstance(functions, list):
            total_functions += len(functions)
    
    avg_tokens_per_function = total_function_tokens / len(sample_functions) if sample_functions else 500
    estimated_total_function_tokens = avg_tokens_per_function * total_functions
    
    print(f"🔧 Total functions in repository: {total_functions:,}")
    print(f"📊 Sample functions analyzed: {len(sample_functions)}")
    print(f"📈 Average tokens per function: {avg_tokens_per_function:.0f}")
    print(f"💭 Estimated total function tokens: {estimated_total_function_tokens:,.0f}")
    
    return {
        'functions': total_functions,
        'estimated_input_tokens': int(estimated_total_function_tokens),
        'estimated_output_tokens': total_functions * 100  # Assume ~100 tokens output per function
    }

def calculate_directory_and_file_level_costs():
    """Calculate costs for directory_and_file_level methods"""
    print("\n" + "=" * 60)
    print("💰 DIRECTORY & FILE LEVEL COST CALCULATION")
    print("=" * 60)
    
    repo_structure_tokens = estimate_repository_structure_tokens()
    proposal_tokens = estimate_proposal_tokens()
    
    costs = {}
    
    for variant in ["1000", "2000"]:
        print(f"\n--- main.py with repository_structure_{variant} ---")
        
        structure_data = repo_structure_tokens[variant]
        if structure_data['files'] == 0:
            print(f"❌ No structure files found for {variant}")
            costs[f"main_{variant}"] = {'input_cost': 0, 'output_cost': 0, 'total_cost': 0}
            continue
        
        # Input tokens: (proposal + structure) * number_of_structure_files * number_of_proposals
        proposals_count = proposal_tokens['count']
        structure_files_count = structure_data['files']
        avg_proposal_tokens = proposal_tokens['avg_tokens']
        avg_structure_tokens = structure_data['avg_tokens_per_file']
        
        # Each API call uses: proposal + one structure file
        tokens_per_api_call = avg_proposal_tokens + avg_structure_tokens
        total_api_calls = proposals_count * structure_files_count
        total_input_tokens = tokens_per_api_call * total_api_calls
        
        # Estimate output tokens (assume ~200 tokens per response for JSON with file paths)
        estimated_output_tokens = total_api_calls * 200
        
        input_cost = (total_input_tokens / 1_000_000) * GPT4O_INPUT_PRICE
        output_cost = (estimated_output_tokens / 1_000_000) * GPT4O_OUTPUT_PRICE
        total_cost = input_cost + output_cost
        
        costs[f"main_{variant}"] = {
            'input_tokens': total_input_tokens,
            'output_tokens': estimated_output_tokens,
            'api_calls': total_api_calls,
            'input_cost': input_cost,
            'output_cost': output_cost,
            'total_cost': total_cost
        }
        
        print(f"📊 Proposals: {proposals_count:,}")
        print(f"📁 Structure files: {structure_files_count}")
        print(f"🔄 Total API calls: {total_api_calls:,}")
        print(f"📥 Input tokens per call: {tokens_per_api_call:,}")
        print(f"📥 Total input tokens: {total_input_tokens:,}")
        print(f"📤 Estimated output tokens: {estimated_output_tokens:,}")
        print(f"💵 Input cost: ${input_cost:.4f}")
        print(f"💵 Output cost: ${output_cost:.4f}")
        print(f"💰 Total cost: ${total_cost:.4f}")
    
    return costs

def calculate_function_level_costs():
    """Calculate costs for function_level method"""
    print("\n" + "=" * 60)
    print("💰 FUNCTION LEVEL COST CALCULATION")
    print("=" * 60)
    
    proposal_tokens = estimate_proposal_tokens()
    function_data = estimate_function_level_costs()
    
    proposals_count = proposal_tokens['count']
    avg_proposal_tokens = proposal_tokens['avg_tokens']
    
    # Function level processes each proposal with function skeleton extraction
    # Estimate tokens for function skeleton (much smaller than full function content)
    estimated_skeleton_tokens = 50000  # Rough estimate for Go skeleton
    
    tokens_per_api_call = avg_proposal_tokens + estimated_skeleton_tokens
    total_api_calls = proposals_count
    total_input_tokens = tokens_per_api_call * total_api_calls
    
    # Estimate output tokens (function-level results, assume ~500 tokens per proposal)
    estimated_output_tokens = total_api_calls * 500
    
    input_cost = (total_input_tokens / 1_000_000) * GPT4O_INPUT_PRICE
    output_cost = (estimated_output_tokens / 1_000_000) * GPT4O_OUTPUT_PRICE
    total_cost = input_cost + output_cost
    
    print(f"📊 Proposals: {proposals_count:,}")
    print(f"🔄 Total API calls: {total_api_calls:,}")
    print(f"📥 Input tokens per call: {tokens_per_api_call:,}")
    print(f"📥 Total input tokens: {total_input_tokens:,}")
    print(f"📤 Estimated output tokens: {estimated_output_tokens:,}")
    print(f"💵 Input cost: ${input_cost:.4f}")
    print(f"💵 Output cost: ${output_cost:.4f}")
    print(f"💰 Total cost: ${total_cost:.4f}")
    
    return {
        'input_tokens': total_input_tokens,
        'output_tokens': estimated_output_tokens,
        'api_calls': total_api_calls,
        'input_cost': input_cost,
        'output_cost': output_cost,
        'total_cost': total_cost
    }

def main():
    print("💰 Method v9 GPT-4o Cost Calculator")
    print(f"💳 GPT-4o Pricing:")
    print(f"   Input: ${GPT4O_INPUT_PRICE} per 1M tokens")
    print(f"   Cached Input: ${GPT4O_CACHED_INPUT_PRICE} per 1M tokens")
    print(f"   Output: ${GPT4O_OUTPUT_PRICE} per 1M tokens")
    print()
    
    # Calculate costs for each method
    dir_file_costs = calculate_directory_and_file_level_costs()
    function_costs = calculate_function_level_costs()
    
    # Summary
    print("\n" + "=" * 60)
    print("💰 COST SUMMARY")
    print("=" * 60)
    
    total_all_costs = 0
    
    print("📁 Directory & File Level:")
    for variant, costs in dir_file_costs.items():
        total_all_costs += costs['total_cost']
        print(f"   {variant}: ${costs['total_cost']:.4f}")
    
    print("🔧 Function Level:")
    total_all_costs += function_costs['total_cost']
    print(f"   main.py: ${function_costs['total_cost']:.4f}")
    
    print(f"\n💰 GRAND TOTAL: ${total_all_costs:.4f}")
    
    # Save results
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    results = {
        'timestamp': timestamp,
        'pricing': {
            'input_per_1m': GPT4O_INPUT_PRICE,
            'cached_input_per_1m': GPT4O_CACHED_INPUT_PRICE,
            'output_per_1m': GPT4O_OUTPUT_PRICE
        },
        'directory_and_file_level': dir_file_costs,
        'function_level': function_costs,
        'total_cost': total_all_costs
    }
    
    output_file = Path(__file__).parent / f'method_v9_cost_estimate_{timestamp}.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 Detailed results saved to: {output_file}")

if __name__ == '__main__':
    main()
