import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path
import json
from datetime import datetime
import time
import random

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_client import get_llm_config, build_chat_payload

# Import the function analysis function and prompt generator
sys.path.append(str(Path(__file__).parent / 'prompt'))
from link_decision_analyzer import analyze_function_relevance
from link_decision_prompt import generate_link_decision_prompt

def make_api_request_with_retry(api_url, headers, payload, max_retries=3, base_delay=2):
    """
    APIリクエストをリトライ機能付きで実行
    """
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)
            
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

try:
    API_URL, headers, model_for_payload = get_llm_config()
except ValueError as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)

# Load granularity results if provided (for coordinated workflow)
granularity_results = {}
selected_function_output = None
if 'GRANULARITY_RESULTS' in os.environ:
    try:
        granularity_results = json.loads(os.environ['GRANULARITY_RESULTS'])
        print(f"Loaded granularity results for {len(granularity_results)} proposals")
    except Exception as e:
        print(f"Warning: Failed to parse granularity results: {e}")
        granularity_results = {}

if 'SELECTED_FUNCTION_OUTPUT' in os.environ:
    selected_function_output = os.environ['SELECTED_FUNCTION_OUTPUT']
    print(f"Using coordinated function output: {selected_function_output}")

# Design documents: data/docs/{DOCS_SET} (default sample_doc)
docs_set = os.environ.get('DOCS_SET', 'sample_doc').strip()
docs_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'docs' / docs_set

# Select function-level output directory: env var or latest under src/function_level_localization/output
function_level_output_root = Path(__file__).resolve().parent.parent / 'function_level_localization' / 'output'
if not function_level_output_root.exists() or not any(d.is_dir() for d in function_level_output_root.iterdir()):
    print('No function-level output found. Run function_level_localization first.', file=sys.stderr)
    print(f'  Looked at: {function_level_output_root}', file=sys.stderr)
    sys.exit(1)

if selected_function_output:
    function_level_output_dir = function_level_output_root / selected_function_output
    if not function_level_output_dir.exists():
        print(f'Coordinated function output not found: {selected_function_output}', file=sys.stderr)
        sys.exit(1)
    print(f"Using coordinated function output: {selected_function_output}")
else:
    # Use latest output (by directory name, e.g. 20260202_xxxxxx) so C/docs run does not prompt old list
    function_level_output_dirs = sorted([d for d in function_level_output_root.iterdir() if d.is_dir()], key=lambda d: d.name, reverse=True)
    function_level_output_dir = function_level_output_dirs[0]
    print(f'Using latest function-level output: {function_level_output_dir.name}')

function_level_llm_outputs = function_level_output_dir / 'llm_outputs.json'

# Output directory with timestamp
output_root = Path(__file__).parent / 'output'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = output_root / timestamp
output_dir.mkdir(parents=True, exist_ok=True)
output_json = output_dir / 'llm_outputs.json'

llm_outputs = {}

# Load function-level results
with open(function_level_llm_outputs, 'r') as f:
    function_level_results = json.load(f)

# Remove metadata if present
if "selected_file_level_output" in function_level_results:
    del function_level_results["selected_file_level_output"]

# If granularity results are available, only process function-granularity proposals
if granularity_results:
    original_proposals = list(function_level_results.keys())
    function_proposals = [p for p in original_proposals if granularity_results.get(p) == "function"]
    
    # Filter function_level_results to only include function-granularity proposals
    filtered_results = {p: function_level_results[p] for p in function_proposals if p in function_level_results}
    skipped_count = len(original_proposals) - len(function_proposals)
    
    if skipped_count > 0:
        print(f"Granularity filtering: Processing {len(function_proposals)} function-granularity proposals, skipping {skipped_count} others")
    
    function_level_results = filtered_results

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
if selected_function_output:
    # In coordinated mode, process all functions
    max_functions = total_functions
    print(f"Coordinated mode: Processing all {max_functions} functions...")
else:
    # Manual mode: ask user for batch size
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
    proposal_file = docs_dir / proposal_id

    if not proposal_file.exists():
        print(f"[SKIP] Document file {proposal_id} not found")
        continue

    # Load document text
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
                
                # Log prompt if LOG_PROMPTS is enabled
                if os.environ.get('LOG_PROMPTS', '0') == '1':
                    print(f"\n{'='*70}")
                    print(f"[PROMPT LOG] Document: {proposal_id}, File: {file_path}, Function: {function_name}")
                    print(f"{'='*70}")
                    print(prompt)
                    print(f"{'='*70}\n")
                    sys.stdout.flush()
                
                payload = build_chat_payload(
                    [{"role": "user", "content": prompt}],
                    temperature=0.0,
                    model_for_payload=model_for_payload,
                )
                
                # Use retry logic for API calls
                success, response_data, error_msg = make_api_request_with_retry(API_URL, headers, payload, max_retries=3, base_delay=2)
                
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
