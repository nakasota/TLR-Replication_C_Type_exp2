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

# Import tiktoken for accurate token counting
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("⚠️  tiktoken not available, using token estimation")

# GPT-4o pricing (per 1M tokens)
GPT4O_INPUT_PRICE = 2.50
GPT4O_OUTPUT_PRICE = 10.00

# Global cost tracking variables
total_input_tokens = 0
total_output_tokens = 0
total_api_calls = 0
cost_details = []

def count_tokens_gpt4o(text: str) -> int:
    """Count tokens for GPT-4o using tiktoken"""
    if TIKTOKEN_AVAILABLE:
        try:
            tokenizer = tiktoken.encoding_for_model("gpt-4")
            return len(tokenizer.encode(text))
        except:
            try:
                tokenizer = tiktoken.get_encoding("cl100k_base")
                return len(tokenizer.encode(text))
            except:
                pass
    # Fallback: rough estimation (4 chars per token)
    return len(text) // 4

def track_api_call(prompt: str, response_data: dict, content: str, proposal_name: str):
    """Track API call costs"""
    global total_input_tokens, total_output_tokens, total_api_calls, cost_details
    
    # Count tokens
    input_tokens = count_tokens_gpt4o(prompt)
    output_tokens = count_tokens_gpt4o(content)
    
    # Get actual usage from OpenAI response if available
    actual_input = input_tokens
    actual_output = output_tokens
    if 'usage' in response_data:
        usage = response_data['usage']
        actual_input = usage.get('prompt_tokens', input_tokens)
        actual_output = usage.get('completion_tokens', output_tokens)
        print(f"    [COST] Actual tokens: {actual_input} input + {actual_output} output = {actual_input + actual_output} total")
    else:
        print(f"    [COST] Estimated tokens: {input_tokens} input + {output_tokens} output = {input_tokens + output_tokens} total")
    
    # Update totals
    total_input_tokens += actual_input
    total_output_tokens += actual_output
    total_api_calls += 1
    
    # Calculate costs for this call
    input_cost = (actual_input / 1_000_000) * GPT4O_INPUT_PRICE
    output_cost = (actual_output / 1_000_000) * GPT4O_OUTPUT_PRICE
    call_cost = input_cost + output_cost
    
    # Store details
    call_detail = {
        'proposal': proposal_name,
        'input_tokens': actual_input,
        'output_tokens': actual_output,
        'input_cost_usd': input_cost,
        'output_cost_usd': output_cost,
        'call_cost_usd': call_cost,
        'timestamp': datetime.now().isoformat()
    }
    cost_details.append(call_detail)
    
    # Print cost info
    print(f"    [COST] Call cost: ${call_cost:.6f} (${input_cost:.6f} input + ${output_cost:.6f} output)")
    
    # Print running totals
    total_cost = (total_input_tokens / 1_000_000 * GPT4O_INPUT_PRICE + 
                 total_output_tokens / 1_000_000 * GPT4O_OUTPUT_PRICE)
    print(f"    [COST] Running total: {total_api_calls} calls, ${total_cost:.6f} total cost")

def save_cost_report(output_dir: Path):
    """Save detailed cost report"""
    total_cost = (total_input_tokens / 1_000_000 * GPT4O_INPUT_PRICE + 
                 total_output_tokens / 1_000_000 * GPT4O_OUTPUT_PRICE)
    
    cost_report = {
        'script_info': {
            'script_name': 'function_level/main.py',
            'structure_type': 'function_level',
            'execution_time': datetime.now().isoformat(),
            'tiktoken_available': TIKTOKEN_AVAILABLE
        },
        'summary': {
            'total_api_calls': total_api_calls,
            'total_input_tokens': total_input_tokens,
            'total_output_tokens': total_output_tokens,
            'total_tokens': total_input_tokens + total_output_tokens,
            'total_cost_usd': total_cost,
            'input_cost_usd': (total_input_tokens / 1_000_000) * GPT4O_INPUT_PRICE,
            'output_cost_usd': (total_output_tokens / 1_000_000) * GPT4O_OUTPUT_PRICE,
            'avg_cost_per_call': total_cost / max(1, total_api_calls)
        },
        'pricing': {
            'gpt4o_input_per_1m_tokens': GPT4O_INPUT_PRICE,
            'gpt4o_output_per_1m_tokens': GPT4O_OUTPUT_PRICE
        },
        'call_details': cost_details
    }
    
    cost_file = output_dir / 'cost_report.json'
    with open(cost_file, 'w') as f:
        json.dump(cost_report, f, indent=2)
    
    print(f"\n💰 COST SUMMARY:")
    print(f"   Total API calls: {total_api_calls:,}")
    print(f"   Total input tokens: {total_input_tokens:,}")
    print(f"   Total output tokens: {total_output_tokens:,}")
    print(f"   Total cost: ${total_cost:.6f}")
    print(f"   Cost report saved: {cost_file}")
    
    return cost_file

# Import the updated skeleton extraction function
sys.path.append(str(Path(__file__).parent / 'prompt'))
from function_level_localization import extract_go_skeleton
from tree_sitter import Language, Parser

def make_api_request_with_retry(payload, max_retries=3, base_delay=2):
    """
    APIリクエストをリトライ機能付きで実行
    """
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                return True, response.json(), None
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

API_KEY = os.getenv('OPENAI_API_KEY')
if not API_KEY:
    print("Error: OPENAI_API_KEY not found in .env file.", file=sys.stderr)
    sys.exit(1)

# Directory containing accepted proposals
proposals_dir = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals'

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

API_URL = "https://api.openai.com/v1/chat/completions"
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
            "model": "gpt-4o",
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
                
                # Track API call cost
                track_api_call(prompt, response_data, content, f"{proposal_id}_{file_path}")
                
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

print(f"Function-level results saved to: {output_json}")

# Save cost report
cost_report_file = save_cost_report(output_dir)
print(f"Cost report saved to: {cost_report_file}")
