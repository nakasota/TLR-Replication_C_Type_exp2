import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path
import json
import subprocess
from datetime import datetime
import ijson
import time
import random

# Cost tracking imports
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("[WARNING] tiktoken not available. Token counts will be estimated.")

# Import the function analysis function and prompt generator
sys.path.append(str(Path(__file__).parent / 'prompt'))
from link_decision_analyzer import analyze_function_relevance
from link_decision_prompt import generate_link_decision_prompt

# Cost tracking configuration for deepseek-chat
DEEPSEEK_INPUT_CACHE_HIT_COST = 0.07 / 1_000_000    # $0.07 per 1M tokens
DEEPSEEK_INPUT_CACHE_MISS_COST = 0.27 / 1_000_000   # $0.27 per 1M tokens
DEEPSEEK_OUTPUT_COST = 1.10 / 1_000_000             # $1.10 per 1M tokens

# Global cost tracking variables
total_cost = 0.0
total_input_tokens = 0
total_output_tokens = 0
cost_details = []

def count_tokens(text, model="gpt-4"):
    """Count tokens in text using tiktoken or estimate if not available"""
    if TIKTOKEN_AVAILABLE:
        try:
            # Use gpt-4 tokenizer as approximation for deepseek-chat
            encoding = tiktoken.encoding_for_model("gpt-4")
            return len(encoding.encode(str(text)))
        except Exception as e:
            print(f"[WARNING] tiktoken error: {e}, falling back to estimation")
    
    # Fallback estimation: roughly 4 characters per token
    return len(str(text)) // 4

def calculate_deepseek_cost(input_tokens, output_tokens, cache_hit_ratio=0.0):
    """Calculate cost for deepseek-chat with cache considerations"""
    cache_hit_tokens = int(input_tokens * cache_hit_ratio)
    cache_miss_tokens = input_tokens - cache_hit_tokens
    
    input_cost = (cache_hit_tokens * DEEPSEEK_INPUT_CACHE_HIT_COST + 
                  cache_miss_tokens * DEEPSEEK_INPUT_CACHE_MISS_COST)
    output_cost = output_tokens * DEEPSEEK_OUTPUT_COST
    
    return input_cost + output_cost, {
        'cache_hit_tokens': cache_hit_tokens,
        'cache_miss_tokens': cache_miss_tokens,
        'input_cost': input_cost,
        'output_cost': output_cost
    }

def make_api_request_with_retry(payload, max_retries=3, base_delay=2):
    """
    APIリクエストをリトライ機能付きで実行 (with cost tracking)
    """
    global total_cost, total_input_tokens, total_output_tokens, cost_details
    
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                response_data = response.json()
                
                # Extract token usage and calculate cost
                usage = response_data.get('usage', {})
                input_tokens = usage.get('prompt_tokens', 0)
                output_tokens = usage.get('completion_tokens', 0)
                
                # If no usage data, estimate from content
                if input_tokens == 0 or output_tokens == 0:
                    messages = payload.get('messages', [])
                    input_text = ' '.join([msg.get('content', '') for msg in messages])
                    input_tokens = count_tokens(input_text)
                    
                    content = response_data.get('choices', [{}])[0].get('message', {}).get('content', '')
                    output_tokens = count_tokens(content)
                
                # Calculate cost (assuming no cache hits for conservative estimation)
                call_cost, cost_breakdown = calculate_deepseek_cost(input_tokens, output_tokens)
                
                # Update global tracking
                total_cost += call_cost
                total_input_tokens += input_tokens
                total_output_tokens += output_tokens
                
                # Record detailed cost info
                cost_detail = {
                    'timestamp': datetime.now().isoformat(),
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                    'cost': call_cost,
                    'breakdown': cost_breakdown
                }
                cost_details.append(cost_detail)
                
                # Print running totals
                print(f"[COST] Tokens: {input_tokens}in/{output_tokens}out | "
                      f"Cost: ${call_cost:.6f} | "
                      f"Total: ${total_cost:.6f}")
                
                return True, response_data, None
            elif response.status_code == 429:  # Rate limit
                print(f"[RETRY] Rate limit hit, attempt {attempt + 1}/{max_retries + 1}")
                if attempt < max_retries:
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    time.sleep(delay)
                    continue
            else:
                print(f"[ERROR] API returned status {response.status_code}, attempt {attempt + 1}/{max_retries + 1}")
                if attempt < max_retries:
                    delay = base_delay * (2 ** attempt)
                    time.sleep(delay)
                    continue
                    
        except requests.exceptions.SSLError as e:
            print(f"[RETRY] SSL error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                time.sleep(delay)
                continue
                
        except requests.exceptions.ConnectionError as e:
            print(f"[RETRY] Connection error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                time.sleep(delay)
                continue
                
        except requests.exceptions.Timeout as e:
            print(f"[RETRY] Timeout on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
                continue
                
        except Exception as e:
            print(f"[RETRY] Unexpected error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
                continue
    
    return False, None, f"Failed after {max_retries + 1} attempts"

# Load environment variables from .env
load_dotenv(dotenv_path=Path(__file__).parent.parent.parent / '.env')

API_KEY = os.getenv('DEEPSEEK_API_KEY')
if not API_KEY:
    print("Error: DEEPSEEK_API_KEY not found in .env file.", file=sys.stderr)
    sys.exit(1)

# Directory containing accepted proposals
proposals_dir = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals'

# Prompt user to select function-level output directory
function_level_output_root = Path(__file__).parent.parent / 'function_level' / 'output'
if not function_level_output_root.exists() or not any(d.is_dir() for d in function_level_output_root.iterdir()):
    print('No function-level output found.', file=sys.stderr)
    sys.exit(1)
function_level_output_dirs = sorted([d for d in function_level_output_root.iterdir() if d.is_dir()], reverse=True)
print('Available function-level output directories:')
for i, d in enumerate(function_level_output_dirs):
    print(f"[{i}] {d.name}")
selected_idx = input(f"Select function-level output index [0-{len(function_level_output_dirs)-1}]: ")
try:
    selected_idx = int(selected_idx)
    if not (0 <= selected_idx < len(function_level_output_dirs)):
        raise ValueError
except Exception:
    print('Invalid selection.', file=sys.stderr)
    sys.exit(1)
function_level_output_dir = function_level_output_dirs[selected_idx]
function_level_llm_outputs = function_level_output_dir / 'llm_outputs.json'

# Output directory with timestamp
output_root = Path(__file__).parent / 'output'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = output_root / timestamp
output_dir.mkdir(parents=True, exist_ok=True)
output_json = output_dir / 'llm_outputs.json'

API_URL = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

llm_outputs = {}

# Load function-level results
with open(function_level_llm_outputs, 'r') as f:
    function_level_results = json.load(f)

# Remove metadata if present
if "selected_file_level_output" in function_level_results:
    del function_level_results["selected_file_level_output"]

# Count total functions to process
total_functions = 0
for proposal_id, file_data in function_level_results.items():
    for file_path, functions in file_data.items():
        total_functions += len(functions)

if total_functions == 0:
    print('No functions to process for the selected function-level output.')
    sys.exit(0)

print(f"Total functions to process: {total_functions}")

# Allow user to set a batch size limit for testing
batch_size = input(f"Enter batch size (1-{total_functions}, or 'all' for all functions): ").strip()
if batch_size.lower() == 'all':
    max_functions = total_functions
else:
    try:
        max_functions = int(batch_size)
        if max_functions < 1 or max_functions > total_functions:
            raise ValueError
    except ValueError:
        print("Invalid batch size. Using default of 10 functions.")
        max_functions = 10

print(f"Processing up to {max_functions} functions...")

# Process each function individually
current_function = 0
for proposal_id, file_data in function_level_results.items():
    proposal_file = proposals_dir / proposal_id
    
    if not proposal_file.exists():
        print(f"[SKIP] Proposal file {proposal_id} not found")
        continue
    
    # Load proposal text
    with open(proposal_file, 'r', encoding='utf-8') as f:
        proposal_text = f.read()
    
    # Initialize output for this proposal
    if proposal_id not in llm_outputs:
        llm_outputs[proposal_id] = {}
    
    for file_path, functions in file_data.items():
        if proposal_id not in llm_outputs:
            llm_outputs[proposal_id] = {}
        if file_path not in llm_outputs[proposal_id]:
            llm_outputs[proposal_id][file_path] = {}
        
        for function_name in functions:
            current_function += 1
            print(f"[Progress] {current_function}/{total_functions}: {proposal_id} | {file_path} | {function_name}")
            
            try:
                # Extract function code and context using the file path directly (no need to check file existence)
                function_info = analyze_function_relevance(file_path, function_name)
                
                if not function_info:
                    print(f"[SKIP] Function {function_name} not found in {file_path}")
                    llm_outputs[proposal_id][file_path][function_name] = "No"
                    continue
                
                # Generate prompt using the prompt module
                prompt = generate_link_decision_prompt(
                    proposal_text=proposal_text,
                    file_path=file_path,
                    function_name=function_name,
                    function_code=function_info["function_code"],
                    function_context=function_info["context"]
                )
                
                payload = {
                    "model": "deepseek-chat",
                    "temperature": 0.0,
                    "messages": [
                        {"role": "user", "content": prompt}
                    ]
                }
                
                # Use retry logic for API calls
                success, response_data, error_msg = make_api_request_with_retry(payload, max_retries=3, base_delay=2)
                
                if success:
                    try:
                        content = response_data['choices'][0]['message']['content'].strip()
                        print(f"[LLM OUTPUT] {content}")
                        
                        # Validate response is either "Yes" or "No"
                        if content.lower() in ["yes", "no"]:
                            decision = content.capitalize()  # "Yes" or "No"
                        else:
                            print(f"[WARNING] Invalid LLM response '{content}', defaulting to 'No'")
                            decision = "No"
                        
                        llm_outputs[proposal_id][file_path][function_name] = decision
                        
                    except Exception as parse_error:
                        print(f"[ERROR] Failed to parse LLM output for {function_name}: {parse_error}")
                        llm_outputs[proposal_id][file_path][function_name] = "No"
                else:
                    print(f"[ERROR] LLM API call failed for {function_name}: {error_msg}")
                    llm_outputs[proposal_id][file_path][function_name] = "No"
                    
            except Exception as e:
                print(f"[ERROR] Function analysis failed for {function_name}: {e}")
                llm_outputs[proposal_id][file_path][function_name] = "No"

# Save results
with open(output_json, 'w') as f:
    output_data = {"selected_function_level_output": function_level_output_dir.name}
    output_data.update(llm_outputs)
    json.dump(output_data, f, indent=2)

# Save cost tracking report
cost_report = {
    'model': 'deepseek-chat',
    'total_cost': total_cost,
    'total_input_tokens': total_input_tokens,
    'total_output_tokens': total_output_tokens,
    'total_tokens': total_input_tokens + total_output_tokens,
    'pricing': {
        'input_cache_hit_per_1m': DEEPSEEK_INPUT_CACHE_HIT_COST * 1_000_000,
        'input_cache_miss_per_1m': DEEPSEEK_INPUT_CACHE_MISS_COST * 1_000_000,
        'output_per_1m': DEEPSEEK_OUTPUT_COST * 1_000_000
    },
    'summary': {
        'total_api_calls': len(cost_details),
        'average_cost_per_call': total_cost / len(cost_details) if cost_details else 0,
        'average_input_tokens_per_call': total_input_tokens / len(cost_details) if cost_details else 0,
        'average_output_tokens_per_call': total_output_tokens / len(cost_details) if cost_details else 0
    },
    'details': cost_details
}

cost_report_path = output_dir / 'cost_report.json'
with open(cost_report_path, 'w') as f:
    json.dump(cost_report, f, indent=2)

print(f"Link decision analysis completed. Results saved to {output_json}")

# Print summary statistics
total_yes = 0
total_no = 0
for proposal_id, file_data in llm_outputs.items():
    for file_path, function_data in file_data.items():
        for function_name, decision in function_data.items():
            if decision == "Yes":
                total_yes += 1
            elif decision == "No":
                total_no += 1

print(f"Summary: {total_yes} functions marked as 'Yes', {total_no} functions marked as 'No'")

print(f"\n=== COST SUMMARY ===")
print(f"Model: deepseek-chat")
print(f"Total API calls: {len(cost_details)}")
print(f"Total input tokens: {total_input_tokens:,}")
print(f"Total output tokens: {total_output_tokens:,}")
print(f"Total tokens: {total_input_tokens + total_output_tokens:,}")
print(f"Total cost: ${total_cost:.6f}")
print(f"Average cost per call: ${(total_cost / len(cost_details) if cost_details else 0):.6f}")
print(f"Cost report saved to: {cost_report_path}")
