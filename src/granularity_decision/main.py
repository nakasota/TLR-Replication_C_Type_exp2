import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path
import json
import time
import random
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_client import get_llm_config, build_chat_payload

# Import the prompt generator
sys.path.append(str(Path(__file__).parent / 'prompt'))
from granularity_decision_prompt import generate_granularity_decision_prompt, generate_granularity_decision_diff_prompt

def make_api_request_with_retry(api_url, headers, payload, max_retries=3, base_delay=2):
    """Execute API request with retries."""
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

# Diff mode: DOCS_DIFF_SET set → read from data/docs_diff/{DOCS_DIFF_SET}/sample_pair_*/
docs_diff_set = os.environ.get('DOCS_DIFF_SET', '').strip()
if docs_diff_set:
    docs_diff_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'docs_diff' / docs_diff_set
    if not docs_diff_dir.exists():
        print(f'Docs diff directory not found: {docs_diff_dir}', file=sys.stderr)
        sys.exit(1)
    pair_dirs = sorted([d for d in docs_diff_dir.iterdir() if d.is_dir() and (d / 'base.md').exists() and (d / 'changed.md').exists()], key=lambda p: p.name)
    doc_files = None
    pair_items = [(p.name, p) for p in pair_dirs]
    print(f"Diff mode: Found {len(pair_items)} pairs in {docs_diff_set}")
else:
    docs_set = os.environ.get('DOCS_SET', 'sample_doc').strip()
    docs_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'docs' / docs_set
    if not docs_dir.exists():
        print(f'Design docs directory not found: {docs_dir}', file=sys.stderr)
        sys.exit(1)
    doc_files = sorted(docs_dir.glob('*.md'), key=lambda p: p.name)
    if not doc_files:
        print('No design document files (.md) found.', file=sys.stderr)
        sys.exit(1)
    pair_items = None
    print(f"Found {len(doc_files)} design documents")

# Output directory with timestamp
output_root = Path(__file__).parent / 'output'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = output_root / timestamp
output_dir.mkdir(parents=True, exist_ok=True)
output_json = output_dir / 'granularity_decisions.json'

granularity_decisions = {}

# Batch/start: from env, or stdin (coordinated_workflow), or default "all"
batch_size = os.environ.get('BATCH_SIZE', '').strip()
start_from = os.environ.get('START_FROM', '').strip()
if not batch_size or not start_from:
    try:
        if not sys.stdin.isatty():
            batch_size = (batch_size or sys.stdin.readline().strip()) or "all"
            start_from = (start_from or sys.stdin.readline().strip()) or "0"
        else:
            batch_size = batch_size or "all"
            start_from = start_from or "0"
    except (EOFError, KeyboardInterrupt):
        batch_size = "all"
        start_from = "0"

items_to_process = pair_items if pair_items else [(f.name, f) for f in doc_files]
total_items = len(items_to_process)

try:
    start_from_int = int(start_from)
    if start_from_int < 0 or start_from_int >= total_items:
        start_from_int = 0
except ValueError:
    start_from_int = 0

if batch_size.lower() == 'all':
    max_docs = total_items - start_from_int
else:
    try:
        max_docs = min(int(batch_size), total_items - start_from_int)
        if max_docs < 1:
            max_docs = total_items - start_from_int
    except ValueError:
        max_docs = total_items - start_from_int

print(f"Processing {max_docs} item(s) starting from index {start_from_int}...")

processed_count = 0
for i in range(start_from_int, total_items):
    if processed_count >= max_docs:
        break
    doc_id, doc_or_pair = items_to_process[i]
    processed_count += 1

    print(f"[{processed_count}/{max_docs}] {doc_id}")
    sys.stdout.flush()

    try:
        if pair_items:
            with open(doc_or_pair / 'base.md', 'r', encoding='utf-8') as f:
                base_text = f.read()
            with open(doc_or_pair / 'changed.md', 'r', encoding='utf-8') as f:
                changed_text = f.read()
            prompt = generate_granularity_decision_diff_prompt(base_text, changed_text)
        else:
            with open(doc_or_pair, 'r', encoding='utf-8') as f:
                doc_text = f.read()
            prompt = generate_granularity_decision_prompt(doc_text)
        
        # Log prompt if LOG_PROMPTS is enabled
        if os.environ.get('LOG_PROMPTS', '0') == '1':
            print(f"\n{'='*70}")
            print(f"[PROMPT LOG] Item: {doc_id}")
            print(f"{'='*70}")
            print(prompt)
            print(f"{'='*70}\n")
            sys.stdout.flush()
        
        payload = build_chat_payload(
            [{"role": "user", "content": prompt}],
            temperature=0.0,
            model_for_payload=model_for_payload,
        )
        success, response_data, error_msg = make_api_request_with_retry(API_URL, headers, payload, max_retries=3, base_delay=2)

        if success:
            try:
                content = response_data['choices'][0]['message']['content'].strip()
                valid_options = ["directory", "file", "function"]
                decision = content.lower() if content.lower() in valid_options else "file"
                granularity_decisions[doc_id] = decision
                print(f"  → {decision}")
            except Exception as parse_error:
                print(f"[ERROR] Parse failed for {doc_id}: {parse_error}")
                granularity_decisions[doc_id] = "file"
                print(f"  → file (fallback)")
        else:
            print(f"[ERROR] API failed for {doc_id}: {error_msg}")
            granularity_decisions[doc_id] = "file"
            print(f"  → file (fallback)")
    except Exception as e:
        print(f"[ERROR] Failed for {doc_id}: {e}")
        granularity_decisions[doc_id] = "file"
        print(f"  → file (fallback)")
    sys.stdout.flush()
    time.sleep(1)

    if processed_count % 5 == 0 or processed_count == max_docs:
        d = sum(1 for v in granularity_decisions.values() if v == "directory")
        f = sum(1 for v in granularity_decisions.values() if v == "file")
        fn = sum(1 for v in granularity_decisions.values() if v == "function")
        print(f"[SUMMARY] Directory: {d}, File: {f}, Function: {fn}")
        sys.stdout.flush()

# Save results
with open(output_json, 'w') as f:
    json.dump(granularity_decisions, f, indent=2)

print(f"Granularity decision completed. Results saved to {output_json}")

directory_count = sum(1 for v in granularity_decisions.values() if v == "directory")
file_count = sum(1 for v in granularity_decisions.values() if v == "file")
function_count = sum(1 for v in granularity_decisions.values() if v == "function")
print(f"Summary: Directory={directory_count}, File={file_count}, Function={function_count}, Total={len(granularity_decisions)}")
