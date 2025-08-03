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

# Import the updated skeleton extraction function
sys.path.append(str(Path(__file__).parent / 'prompt'))
from function_level_localization import extract_go_skeleton
from tree_sitter import Language, Parser

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
proposals_dir = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals_with_state'

# Prompt user to select file-level output directory
file_level_output_root = Path(__file__).parent.parent / 'directory_and_file_level' / 'output'
if not file_level_output_root.exists() or not any(d.is_dir() for d in file_level_output_root.iterdir()):
    print('No file-level output found.', file=sys.stderr)
    sys.exit(1)
file_level_output_dirs = sorted([d for d in file_level_output_root.iterdir() if d.is_dir()], reverse=True)
print('Available file-level output directories:')
for i, d in enumerate(file_level_output_dirs):
    print(f"[{i}] {d.name}")
selected_idx = input(f"Select file-level output index [0-{len(file_level_output_dirs)-1}]: ")
try:
    selected_idx = int(selected_idx)
    if not (0 <= selected_idx < len(file_level_output_dirs)):
        raise ValueError
except Exception:
    print('Invalid selection.', file=sys.stderr)
    sys.exit(1)
file_level_output_dir = file_level_output_dirs[selected_idx]
file_level_llm_outputs = file_level_output_dir / 'llm_outputs.json'

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

proposal_files = list(proposals_dir.glob('*.md'))
# Only process proposals that exist in the selected file-level output
with open(file_level_llm_outputs, 'r') as f:
    file_level_results = json.load(f)
proposal_files = [p for p in proposal_files if p.name in file_level_results]
total = len(proposal_files)

if total == 0:
    print('No proposals to process for the selected file-level output.')
    sys.exit(0)

# Load repo structure mapping (nested dict)
repo_structure_path = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'go_repo_structure.json'
with open(repo_structure_path, 'r') as f:
    repo_structure = json.load(f)

# Initialize the Go parser for skeleton extraction
GO_LANGUAGE = Language(str(Path(__file__).parent.parent.parent / "build" / "my-languages.so"), "go")
parser = Parser()
parser.set_language(GO_LANGUAGE)

for idx, proposal_file in enumerate(proposal_files, 1):
    print(f"[Progress] {idx}/{total}: {proposal_file.name}")
    proposal_id = proposal_file.name
    v = file_level_results.get(proposal_id)
    if not v or "found_files" not in v or not v["found_files"]:
        print(f"[SKIP] No found_files for {proposal_id}")
        continue
    found_files = v["found_files"]
    for file_path in found_files:
        if not file_path.endswith('.go'):
            print(f"[SKIP] {file_path} is not a Go source file")
            continue
        directory = os.path.dirname(file_path)
        # Check if file exists in the actual Go repository
        go_repo_path = Path(__file__).parent.parent.parent / 'data' / 'repos' / 'go'
        abs_file_path = go_repo_path / file_path
        if not abs_file_path.exists():
            print(f"[SKIP] {file_path} not found in Go repository")
            continue
        
        # Use the updated skeleton extraction function directly
        try:
            skeleton = extract_go_skeleton(abs_file_path, parser)
            
            # Use full skeleton view without any truncation
            
            # Load proposal text
            with open(proposal_file, 'r', encoding='utf-8') as f:
                proposal_text = f.read()
            
            # Compose prompt directly
            prompt = f'''
You are analyzing a Go proposal and a Go source file to identify which functions and methods are **most relevant** to the given proposal.

### Proposal Content ###
{proposal_text}

### File Information ###
File: {file_path}
Directory: {directory}

### File Skeleton (first 100 lines) ###
{skeleton}

**CRITICAL OBJECTIVE**: Identify the **most relevant functions and methods** in this file that are closely related to the proposal topic and discussion.

**WHAT TO INCLUDE:**
- Regular functions (func FuncName(...))
- Methods (func (receiver) MethodName(...))
- Named function literals (var funcVar = func(...))
- Interface methods (methods defined in interface types)

**MANDATORY OUTPUT FORMAT:**
Return a JSON object with the following format.
The response MUST:
- Be a valid JSON block.
- Contain a key `relevant_functions` with a list of function/method names (strings).
- For methods, use the format "MethodName" (without receiver).
- For interface methods, use the format "MethodName" (method name only).
- For named function literals, use the variable name.
- Output ONLY the raw JSON object. Do NOT include any markdown formatting (no ```json or ```).
- Do NOT add any explanations or additional text.

Example of correct output:
{{
  "relevant_functions": [
    "RegularFunc",
    "MethodName",
    "InterfaceMethod",
    "funcLiteral"
  ]
}}

**MANDATORY SELECTION RULES:**
- Select only the most essential functions and methods that are directly related to the accepted proposal.
- Include both regular functions AND methods that are relevant.
- Consider all types of callable entities shown in the skeleton.
- The output must strictly follow the format.
- If you are unsure, make your best guess based on the file skeleton and proposal.
'''.strip()
            
        except Exception as e:
            print(f"[SKIP] Skeleton extraction failed for {proposal_id} in {file_path}: {e}")
            continue
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
                content = response_data['choices'][0]['message']['content']
                print(f"[LLM RAW OUTPUT] {proposal_id} | {file_path} | {content[:200]}")
                if content.startswith('```json'):
                    content = content[len('```json'):].strip()
                if content.startswith('```'):
                    content = content[len('```'):].strip()
                if content.endswith('```'):
                    content = content[:-3].strip()
                parsed = json.loads(content)
                functions = parsed.get('relevant_functions', [])
                if proposal_id not in llm_outputs:
                    llm_outputs[proposal_id] = {}
                llm_outputs[proposal_id][file_path] = functions
            except Exception as parse_error:
                print(f"[ERROR] Failed to parse LLM output for {proposal_id} in {file_path}: {parse_error}")
                # Record empty result but continue processing
                if proposal_id not in llm_outputs:
                    llm_outputs[proposal_id] = {}
                llm_outputs[proposal_id][file_path] = []
        else:
            print(f"[ERROR] LLM API call failed for {proposal_id} in {file_path}: {error_msg}")
            # Record empty result but continue processing
            if proposal_id not in llm_outputs:
                llm_outputs[proposal_id] = {}
            llm_outputs[proposal_id][file_path] = []

with open(output_json, 'w') as f:
    output_data = {"selected_file_level_output": file_level_output_dir.name}
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

print(f"\n=== COST SUMMARY ===")
print(f"Model: deepseek-chat")
print(f"Total API calls: {len(cost_details)}")
print(f"Total input tokens: {total_input_tokens:,}")
print(f"Total output tokens: {total_output_tokens:,}")
print(f"Total tokens: {total_input_tokens + total_output_tokens:,}")
print(f"Total cost: ${total_cost:.6f}")
print(f"Average cost per call: ${(total_cost / len(cost_details) if cost_details else 0):.6f}")
print(f"Cost report saved to: {cost_report_path}")
print(f"Results saved to: {output_json}")
