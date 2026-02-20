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

# Import skeleton builder and prompt from prompt module (one file, like directory_*)
sys.path.append(str(Path(__file__).parent / 'prompt'))
from function_level_localization import extract_c_skeleton, generate_function_level_localization_prompt, generate_function_level_localization_diff_prompt

def make_api_request_with_retry(api_url, headers, payload, max_retries=3, base_delay=2):
    """Execute API request with retries."""
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)

            if response.status_code == 200:
                return True, response.json(), None
            elif response.status_code == 429:
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
selected_directory_file_output = None
if 'GRANULARITY_RESULTS' in os.environ:
    try:
        granularity_results = json.loads(os.environ['GRANULARITY_RESULTS'])
        print(f"Loaded granularity results for {len(granularity_results)} documents")
    except Exception as e:
        print(f"Warning: Failed to parse granularity results: {e}")
        granularity_results = {}

if 'SELECTED_DIRECTORY_FILE_OUTPUT' in os.environ:
    selected_directory_file_output = os.environ['SELECTED_DIRECTORY_FILE_OUTPUT']
    print(f"Using coordinated directory_file output: {selected_directory_file_output}")

# Diff mode: DOCS_DIFF_SET set → read from data/docs_diff/{DOCS_DIFF_SET}/
docs_diff_set = os.environ.get('DOCS_DIFF_SET', '').strip()
if docs_diff_set:
    docs_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'docs_diff' / docs_diff_set
    diff_mode = True
else:
    docs_set = os.environ.get('DOCS_SET', 'sample_doc').strip()
    docs_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'docs' / docs_set
    diff_mode = False
if not docs_dir.exists():
    print(f"Docs directory not found: {docs_dir}", file=sys.stderr)
    sys.exit(1)

# File-level output from directory_and_file_level_localization (under src/)
file_level_output_root = Path(__file__).resolve().parent.parent / 'directory_and_file_level_localization' / 'output'
if not file_level_output_root.exists() or not any(d.is_dir() for d in file_level_output_root.iterdir()):
    print('No file-level output found. Run directory_and_file_level_localization first.', file=sys.stderr)
    print(f'  Looked at: {file_level_output_root}', file=sys.stderr)
    sys.exit(1)

if selected_directory_file_output:
    file_level_output_dir = file_level_output_root / selected_directory_file_output
    if not file_level_output_dir.exists():
        print(f'Coordinated directory_file output not found: {selected_directory_file_output}', file=sys.stderr)
        sys.exit(1)
    print(f"Using coordinated directory_file output: {selected_directory_file_output}")
else:
    # Use latest output (by directory name) so C/docs run needs no interaction
    file_level_output_dirs = sorted([d for d in file_level_output_root.iterdir() if d.is_dir()], key=lambda d: d.name, reverse=True)
    file_level_output_dir = file_level_output_dirs[0]
    print(f'Using latest directory/file output: {file_level_output_dir.name}')

file_level_llm_outputs = file_level_output_dir / 'llm_outputs.json'
with open(file_level_llm_outputs, 'r') as f:
    file_level_results = json.load(f)

# Document list: keys from file-level results (design doc names)
if diff_mode:
    proposal_files = [docs_dir / name for name in file_level_results if (docs_dir / name).is_dir() and (docs_dir / name / 'base.md').exists()]
else:
    proposal_files = [docs_dir / name for name in file_level_results if (docs_dir / name).exists()]
proposal_files.sort(key=lambda p: p.name)

# Optional granularity filter
if granularity_results:
    function_docs = [p for p in proposal_files if granularity_results.get(p.name) == "function"]
    if len(function_docs) < len(proposal_files):
        print(f"Granularity filtering: Processing {len(function_docs)} function-granularity docs, skipping {len(proposal_files) - len(function_docs)} others")
    proposal_files = function_docs

total = len(proposal_files)
if total == 0:
    print('No design documents to process for the selected file-level output.')
    sys.exit(0)

# Output directory
output_root = Path(__file__).parent / 'output'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = output_root / timestamp
output_dir.mkdir(parents=True, exist_ok=True)
output_json = output_dir / 'llm_outputs.json'

llm_outputs = {}

for idx, doc_file in enumerate(proposal_files, 1):
    print(f"[Progress] {idx}/{total}: {doc_file.name}")
    sys.stdout.flush()
    doc_id = doc_file.name
    v = file_level_results.get(doc_id)
    if not v or not isinstance(v, dict):
        print(f"[SKIP] No entry for {doc_id}")
        continue
    found = v.get("found_files", [])
    if not found:
        print(f"[SKIP] No found_files for {doc_id}")
        continue

    for file_path in found:
        if not (file_path.endswith('.c') or file_path.endswith('.h')):
            print(f"[SKIP] {file_path} is not a C source/header file")
            continue

        skeleton = extract_c_skeleton(file_path)
        if not skeleton:
            print(f"[SKIP] {file_path} not in repo structure or empty skeleton")
            continue

        directory = os.path.dirname(file_path)

        try:
            if diff_mode:
                with open(doc_file / 'base.md', 'r', encoding='utf-8') as f:
                    base_text = f.read()
                with open(doc_file / 'changed.md', 'r', encoding='utf-8') as f:
                    changed_text = f.read()
                prompt = generate_function_level_localization_diff_prompt(base_text, changed_text, file_path, directory, skeleton)
            else:
                with open(doc_file, 'r', encoding='utf-8') as f:
                    doc_text = f.read()
                prompt = generate_function_level_localization_prompt(doc_text, file_path, directory, skeleton)
        except Exception as e:
            print(f"[SKIP] Failed to read doc {doc_id}: {e}")
            continue
        
        # Log prompt if LOG_PROMPTS is enabled
        if os.environ.get('LOG_PROMPTS', '0') == '1':
            print(f"\n{'='*70}")
            print(f"[PROMPT LOG] Document: {doc_id}, File: {file_path}")
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
                content = response_data['choices'][0]['message']['content']
                if content.startswith('```json'):
                    content = content[len('```json'):].strip()
                if content.startswith('```'):
                    content = content[len('```'):].strip()
                if content.endswith('```'):
                    content = content[:-3].strip()
                parsed = json.loads(content)
                functions = parsed.get('relevant_functions', [])
                if doc_id not in llm_outputs:
                    llm_outputs[doc_id] = {}
                llm_outputs[doc_id][file_path] = functions
            except Exception as parse_error:
                print(f"[ERROR] Failed to parse LLM output for {doc_id} in {file_path}: {parse_error}")
                if doc_id not in llm_outputs:
                    llm_outputs[doc_id] = {}
                llm_outputs[doc_id][file_path] = []
        else:
            print(f"[ERROR] LLM API call failed for {doc_id} in {file_path}: {error_msg}")
            if doc_id not in llm_outputs:
                llm_outputs[doc_id] = {}
            llm_outputs[doc_id][file_path] = []

with open(output_json, 'w') as f:
    output_data = {"selected_file_level_output": file_level_output_dir.name}
    output_data.update(llm_outputs)
    json.dump(output_data, f, indent=2)

print(f"\nCompleted. Output: {output_json}")
print("Run function_level_link_decision next; it will use this output by default (latest).")
