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

# Import the file analysis function and prompt generator
sys.path.append(str(Path(__file__).parent / 'prompt'))
from file_level_analyzer import analyze_file_with_skeleton
from file_level_prompt import generate_file_level_link_decision_prompt

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

API_KEY = os.getenv('DEEPSEEK_API_KEY')
if not API_KEY:
    print("Error: DEEPSEEK_API_KEY not found in .env file.", file=sys.stderr)
    sys.exit(1)

# Directory containing accepted proposals
proposals_dir = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals'

# Prompt user to select directory_and_file_localization output directory
dir_file_output_root = Path(__file__).parent.parent / 'directory_and_file_localization' / 'output'
if not dir_file_output_root.exists() or not any(d.is_dir() for d in dir_file_output_root.iterdir()):
    print('No directory_and_file_localization output found.', file=sys.stderr)
    sys.exit(1)
dir_file_output_dirs = sorted([d for d in dir_file_output_root.iterdir() if d.is_dir()], reverse=True)
print('Available directory_and_file_localization output directories:')
for i, d in enumerate(dir_file_output_dirs):
    print(f"[{i}] {d.name}")
selected_idx = input(f"Select directory_and_file_localization output index [0-{len(dir_file_output_dirs)-1}]: ")
try:
    selected_idx = int(selected_idx)
    if not (0 <= selected_idx < len(dir_file_output_dirs)):
        raise ValueError
except Exception:
    print('Invalid selection.', file=sys.stderr)
    sys.exit(1)
dir_file_output_dir = dir_file_output_dirs[selected_idx]
dir_file_llm_outputs = dir_file_output_dir / 'llm_outputs.json'

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

# Load directory_and_file_localization results
with open(dir_file_llm_outputs, 'r') as f:
    dir_file_results = json.load(f)

# Remove metadata if present
metadata_keys = [k for k in dir_file_results.keys() if k.startswith("selected_")]
for key in metadata_keys:
    del dir_file_results[key]

# Count total files to process
total_files = 0
for proposal_id, proposal_data in dir_file_results.items():
    if isinstance(proposal_data, dict):
        file_paths = proposal_data.get('found_files', [])
        if isinstance(file_paths, list):
            total_files += len(file_paths)

if total_files == 0:
    print('No files to process for the selected directory_and_file_localization output.')
    sys.exit(0)

print(f"Total files to process: {total_files}")

# Process each file individually
current_file = 0
for proposal_id, proposal_data in dir_file_results.items():
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
    
    if isinstance(proposal_data, dict):
        file_paths = proposal_data.get('found_files', [])
        if isinstance(file_paths, list):
            for file_path in file_paths:
                current_file += 1
                print(f"[Progress] {current_file}/{total_files}: {proposal_id} | {file_path}")
                
                try:
                    # Analyze file with skeleton view
                    skeleton_data = analyze_file_with_skeleton(file_path)
                    
                    if not skeleton_data:
                        print(f"[SKIP] Could not analyze file {file_path}")
                        llm_outputs[proposal_id][file_path] = "No"
                        continue
                    
                    # Generate prompt using the prompt module
                    prompt = generate_file_level_link_decision_prompt(
                        proposal_text=proposal_text,
                        file_path=file_path,
                        skeleton_view=skeleton_data.get("skeleton_view", "")
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
                            
                            llm_outputs[proposal_id][file_path] = decision
                            
                        except Exception as parse_error:
                            print(f"[ERROR] Failed to parse LLM output for {file_path}: {parse_error}")
                            llm_outputs[proposal_id][file_path] = "No"
                    else:
                        print(f"[ERROR] LLM API call failed for {file_path}: {error_msg}")
                        llm_outputs[proposal_id][file_path] = "No"
                        
                except Exception as e:
                    print(f"[ERROR] File analysis failed for {file_path}: {e}")
                    llm_outputs[proposal_id][file_path] = "No"

# Save results
with open(output_json, 'w') as f:
    output_data = {"selected_directory_and_file_localization_output": dir_file_output_dir.name}
    output_data.update(llm_outputs)
    json.dump(output_data, f, indent=2)

print(f"File-level link decision analysis completed. Results saved to {output_json}")

# Print summary statistics
total_yes = 0
total_no = 0
for proposal_id, file_data in llm_outputs.items():
    for file_path, decision in file_data.items():
        if decision == "Yes":
            total_yes += 1
        elif decision == "No":
            total_no += 1

print(f"Summary: {total_yes} files marked as 'Yes', {total_no} files marked as 'No'")
