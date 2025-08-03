import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path
import json
import time
import random
from datetime import datetime

# Import the prompt generator
sys.path.append(str(Path(__file__).parent / 'prompt'))
from granularity_decision_prompt import generate_granularity_decision_prompt

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
proposals_dir = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'declined_proposals' / 'cleaned_declined_proposals'

if not proposals_dir.exists():
    print(f'Proposals directory not found: {proposals_dir}', file=sys.stderr)
    sys.exit(1)

# Get all proposal files
proposal_files = list(proposals_dir.glob('*.md'))
if not proposal_files:
    print('No proposal files found.', file=sys.stderr)
    sys.exit(1)

print(f"Found {len(proposal_files)} proposal files")

# Output directory with timestamp
output_root = Path(__file__).parent / 'output'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = output_root / timestamp
output_dir.mkdir(parents=True, exist_ok=True)
output_json = output_dir / 'granularity_decisions.json'

API_URL = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

granularity_decisions = {}

# Allow user to set a batch size limit for testing
batch_size = input(f"Enter batch size (1-{len(proposal_files)}, or 'all' for all proposals): ").strip()
if batch_size.lower() == 'all':
    max_proposals = len(proposal_files)
else:
    try:
        max_proposals = int(batch_size)
        if max_proposals < 1 or max_proposals > len(proposal_files):
            raise ValueError
    except ValueError:
        print("Invalid batch size. Using default of 10 proposals.")
        max_proposals = 10

print(f"Processing up to {max_proposals} proposals...")

# Process each proposal
processed_count = 0
for proposal_file in proposal_files:
    if processed_count >= max_proposals:
        break
        
    proposal_id = proposal_file.name
    processed_count += 1
    
    print(f"[Progress] {processed_count}/{max_proposals}: {proposal_id}")
    
    try:
        # Load proposal text
        with open(proposal_file, 'r', encoding='utf-8') as f:
            proposal_text = f.read()
        
        # Generate prompt
        prompt = generate_granularity_decision_prompt(proposal_text)
        
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
                
                # Validate response is one of the valid granularity options
                valid_options = ["directory", "file", "function"]
                if content.lower() in valid_options:
                    decision = content.lower()  # Normalize to lowercase
                else:
                    print(f"[WARNING] Invalid LLM response '{content}', defaulting to 'file'")
                    decision = "file"  # Default fallback
                
                granularity_decisions[proposal_id] = decision
                
            except Exception as parse_error:
                print(f"[ERROR] Failed to parse LLM output for {proposal_id}: {parse_error}")
                granularity_decisions[proposal_id] = "file"  # Default fallback
        else:
            print(f"[ERROR] LLM API call failed for {proposal_id}: {error_msg}")
            granularity_decisions[proposal_id] = "file"  # Default fallback
            
    except Exception as e:
        print(f"[ERROR] Proposal analysis failed for {proposal_id}: {e}")
        granularity_decisions[proposal_id] = "file"  # Default fallback
    
    # Add a small delay between requests to be respectful to the API
    time.sleep(1)

# Save results
with open(output_json, 'w') as f:
    json.dump(granularity_decisions, f, indent=2)

print(f"Granularity decision analysis completed. Results saved to {output_json}")

# Print summary statistics
directory_count = sum(1 for decision in granularity_decisions.values() if decision == "directory")
file_count = sum(1 for decision in granularity_decisions.values() if decision == "file")
function_count = sum(1 for decision in granularity_decisions.values() if decision == "function")

print(f"Summary:")
print(f"  Directory granularity: {directory_count} proposals")
print(f"  File granularity: {file_count} proposals")
print(f"  Function granularity: {function_count} proposals")
print(f"  Total processed: {len(granularity_decisions)} proposals")
