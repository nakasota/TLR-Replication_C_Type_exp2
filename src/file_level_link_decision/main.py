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

# Import the file analysis function and prompt generator
sys.path.append(str(Path(__file__).parent / 'prompt'))
from file_level_analyzer import analyze_file_with_skeleton
from file_level_prompt import generate_file_level_link_decision_prompt, generate_file_level_link_decision_diff_prompt

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

# Granularity results (optional): when set, only process documents with "file" granularity
granularity_results = {}
granularity_results_env = os.environ.get('GRANULARITY_RESULTS')
if granularity_results_env:
    try:
        granularity_results = json.loads(granularity_results_env)
    except json.JSONDecodeError:
        print("Error: Invalid JSON in GRANULARITY_RESULTS environment variable.", file=sys.stderr)
        sys.exit(1)

# Selected directory_and_file_level_localization output (optional: default = latest, under src/)
dir_file_output_root = Path(__file__).resolve().parent.parent / 'directory_and_file_level_localization' / 'output'
selected_directory_file_output = os.environ.get('SELECTED_DIRECTORY_FILE_OUTPUT')
if not selected_directory_file_output:
    if not dir_file_output_root.exists() or not any(dir_file_output_root.iterdir()):
        resolved = dir_file_output_root.resolve()
        print("Error: No directory_and_file_level_localization output found. Run that step first.", file=sys.stderr)
        print(f"  Looked at: {resolved}", file=sys.stderr)
        print("  Run this script from: src/file_level_link_decision", file=sys.stderr)
        sys.exit(1)
    # Use latest output directory (by name, e.g. 20260202_133715)
    subdirs = sorted([d.name for d in dir_file_output_root.iterdir() if d.is_dir()], reverse=True)
    selected_directory_file_output = subdirs[0]
    print(f'Using latest directory/file output: {selected_directory_file_output}')

# Diff mode: DOCS_DIFF_SET set → read from data/docs_diff/{DOCS_DIFF_SET}/
docs_diff_set = os.environ.get('DOCS_DIFF_SET', '').strip()
if docs_diff_set:
    documents_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'docs_diff' / docs_diff_set
    diff_mode = True
else:
    docs_set = os.environ.get('DOCS_SET', 'sample_doc').strip()
    documents_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'docs' / docs_set
    diff_mode = False
if not documents_dir.exists():
    print(f"Documents directory not found: {documents_dir}", file=sys.stderr)
    sys.exit(1)

# Load directory_and_file_localization results
dir_file_output_dir = dir_file_output_root / selected_directory_file_output
dir_file_llm_outputs = dir_file_output_dir / 'llm_outputs.json'

if not dir_file_llm_outputs.exists():
    print(f'Directory/file localization output not found: {dir_file_llm_outputs}', file=sys.stderr)
    sys.exit(1)

with open(dir_file_llm_outputs, 'r') as f:
    dir_file_results = json.load(f)

# Documents to process: if GRANULARITY_RESULTS set, only "file" granularity; else all with found_files
if granularity_results:
    file_granularity_documents = {doc: "file" for doc in dir_file_results
                                  if granularity_results.get(doc) == "file"}
else:
    file_granularity_documents = {doc: "file" for doc in dir_file_results
                                  if isinstance(dir_file_results.get(doc), dict)
                                  and dir_file_results[doc].get("found_files")}

print(f'Loaded directory/file localization results: {len(dir_file_results)} documents')
print(f'Documents to process (file-level link decision): {len(file_granularity_documents)}')

if not file_granularity_documents:
    print("No documents to process (no 'file' granularity or no found_files in directory/file results). Exiting.")
    # Create empty output for consistency
    output_root = Path(__file__).parent / 'output'
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = output_root / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(output_dir / 'llm_outputs.json', 'w') as f:
        json.dump({}, f, indent=2)
    
    print(f'Empty output saved to: {output_dir}/llm_outputs.json')
    sys.exit(0)

print(f'Processing {len(file_granularity_documents)} file-granularity documents:')
for document in file_granularity_documents.keys():
    print(f'  - {document}')

# Optional: print one full prompt (including skeleton view) for verification
if len(sys.argv) > 1 and sys.argv[1] == '--show-prompt':
    doc_name = next(iter(file_granularity_documents))
    found = dir_file_results[doc_name].get('found_files', [])
    if not found:
        print('No found_files for first document.', file=sys.stderr)
        sys.exit(1)
    file_path = found[0]
    doc_path = documents_dir / doc_name
    file_analysis = analyze_file_with_skeleton(file_path)
    if not file_analysis:
        print(f'Failed to get skeleton for {file_path}', file=sys.stderr)
        sys.exit(1)
    skeleton_view = file_analysis.get('skeleton_view', '')
    if diff_mode:
        with open(doc_path / 'base.md', 'r') as f:
            base_text = f.read()
        with open(doc_path / 'changed.md', 'r') as f:
            changed_text = f.read()
        prompt = generate_file_level_link_decision_diff_prompt(base_text, changed_text, file_path, skeleton_view)
    else:
        with open(doc_path, 'r') as f:
            document_text = f.read()
        prompt = generate_file_level_link_decision_prompt(document_text, file_path, skeleton_view)
    print('=== Generated prompt (first document, first file) ===')
    print(prompt)
    print('=== End of prompt ===')
    sys.exit(0)

# Create output directory with timestamp
output_root = Path(__file__).parent / 'output'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = output_root / timestamp
output_dir.mkdir(parents=True, exist_ok=True)

# Process each file-granularity document
results = {}
total_documents = len(file_granularity_documents)
successful_documents = 0
failed_documents = []

for idx, (document_file, granularity) in enumerate(file_granularity_documents.items(), 1):
    print(f"\n[{idx}/{total_documents}] Processing document: {document_file}")
    sys.stdout.flush()
    
    # Skip if document not in directory/file results
    if document_file not in dir_file_results:
        print(f"[SKIP] Document {document_file} not found in directory/file results")
        sys.stdout.flush()
        failed_documents.append((document_file, "not_found_in_dir_file_results"))
        continue
    
    # Get the found files from directory_and_file_level_localization
    document_data = dir_file_results[document_file]
    found_files = document_data.get('found_files', [])
    
    if not found_files:
        print(f"[SKIP] No files found for document {document_file}")
        sys.stdout.flush()
        results[document_file] = {}
        continue
    
    print(f"[INFO] Found {len(found_files)} files to analyze")
    sys.stdout.flush()
    
    # Load document content
    document_path = documents_dir / document_file
    if not document_path.exists():
        print(f"[ERROR] Document file not found: {document_path}")
        sys.stdout.flush()
        failed_documents.append((document_file, "document_file_not_found"))
        continue
    
    if diff_mode:
        with open(document_path / 'base.md', 'r', encoding='utf-8') as f:
            base_text = f.read()
        with open(document_path / 'changed.md', 'r', encoding='utf-8') as f:
            changed_text = f.read()
    else:
        with open(document_path, 'r', encoding='utf-8') as f:
            document_text = f.read()
    
    # Process each file
    document_results = {}
    
    for file_idx, file_path in enumerate(found_files, 1):
        print(f"  [{file_idx}/{len(found_files)}] Analyzing file: {file_path}")
        sys.stdout.flush()
        
        # Get file skeleton and context
        file_analysis = analyze_file_with_skeleton(file_path)
        if not file_analysis:
            print(f"    [ERROR] Failed to analyze file skeleton for {file_path}")
            sys.stdout.flush()
            document_results[file_path] = {"decision": "Error", "error": "skeleton_analysis_failed"}
            continue
        
        skeleton_view = file_analysis.get('skeleton_view', '')
        if not skeleton_view:
            print(f"    [ERROR] Empty skeleton view for {file_path}")
            document_results[file_path] = {"decision": "Error", "error": "empty_skeleton"}
            continue
        
        # Generate prompt for file-level link decision
        if diff_mode:
            prompt = generate_file_level_link_decision_diff_prompt(base_text, changed_text, file_path, skeleton_view)
        else:
            prompt = generate_file_level_link_decision_prompt(document_text, file_path, skeleton_view)
        
        # Log prompt if LOG_PROMPTS is enabled
        if os.environ.get('LOG_PROMPTS', '0') == '1':
            print(f"\n{'='*70}")
            print(f"[PROMPT LOG] Document: {document_file}, File: {file_path}")
            print(f"{'='*70}")
            print(prompt)
            print(f"{'='*70}\n")
            sys.stdout.flush()
        
        # API request payload
        payload = build_chat_payload(
            [{"role": "user", "content": prompt}],
            temperature=0.0,
            model_for_payload=model_for_payload,
            max_tokens=50,
        )
        
        # Make API request with retry
        success, response, error = make_api_request_with_retry(API_URL, headers, payload)
        
        if not success:
            print(f"    [ERROR] API request failed for {file_path}: {error}")
            document_results[file_path] = {"decision": "Error", "error": str(error)}
            continue
        
        try:
            decision = response['choices'][0]['message']['content'].strip()
            # Normalize decision to Yes/No
            if decision.lower() in ['yes', 'y']:
                decision = "Yes"
            elif decision.lower() in ['no', 'n']:
                decision = "No"
            else:
                print(f"    [WARNING] Unexpected decision format: '{decision}', treating as 'No'")
                decision = "No"
            
            document_results[file_path] = {"decision": decision}
            print(f"    [RESULT] Decision: {decision}")
            sys.stdout.flush()
            
        except Exception as e:
            print(f"    [ERROR] Failed to parse API response for {file_path}: {e}")
            sys.stdout.flush()
            document_results[file_path] = {"decision": "Error", "error": str(e)}
        
        # Add small delay between requests
        time.sleep(0.1)
    
    results[document_file] = document_results
    successful_documents += 1
    print(f"[SUCCESS] Completed document {document_file}")
    sys.stdout.flush()

# Save results
output_file = output_dir / 'llm_outputs.json'
with open(output_file, 'w') as f:
    json.dump(results, f, indent=2)

# Generate summary
summary = {
    "timestamp": timestamp,
    "total_documents": total_documents,
    "successful_documents": successful_documents,
    "failed_documents": len(failed_documents),
    "failed_details": failed_documents,
    "granularity_filter": "file",
    "input_source": f"directory_and_file_level_localization/{selected_directory_file_output}"
}

summary_file = output_dir / 'processing_summary.json'
with open(summary_file, 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\n{'='*50}")
print("FILE-LEVEL LINK DECISION COMPLETED")
print(f"{'='*50}")
print(f"Total documents processed: {successful_documents}/{total_documents}")
print(f"Failed documents: {len(failed_documents)}")
print(f"Results saved to: {output_file}")
print(f"Summary saved to: {summary_file}")
print("For function-level pipeline next: run function_level_localization, then function_level_link_decision.")

if failed_documents:
    print("\nFailed documents:")
    for document, reason in failed_documents:
        print(f"  - {document}: {reason}")
