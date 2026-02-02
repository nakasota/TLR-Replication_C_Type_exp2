import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path
import json
import subprocess
from datetime import datetime
import time
import random

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from llm_client import get_llm_config, build_chat_payload

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
                print(f"    [RETRY] Rate limit hit, attempt {attempt + 1}/{max_retries + 1}")
                if attempt < max_retries:
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    time.sleep(delay)
                    continue
            else:
                print(f"    [ERROR] API returned status {response.status_code}, attempt {attempt + 1}/{max_retries + 1}")
                if attempt < max_retries:
                    delay = base_delay * (2 ** attempt)
                    time.sleep(delay)
                    continue
                    
        except requests.exceptions.SSLError as e:
            print(f"    [RETRY] SSL error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                time.sleep(delay)
                continue
                
        except requests.exceptions.ConnectionError as e:
            print(f"    [RETRY] Connection error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                time.sleep(delay)
                continue
                
        except requests.exceptions.Timeout as e:
            print(f"    [RETRY] Timeout on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
                continue
                
        except Exception as e:
            print(f"    [RETRY] Unexpected error on attempt {attempt + 1}/{max_retries + 1}: {e}")
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
if 'GRANULARITY_RESULTS' in os.environ:
    try:
        granularity_results = json.loads(os.environ['GRANULARITY_RESULTS'])
        print(f"Loaded granularity results for {len(granularity_results)} proposals")
    except Exception as e:
        print(f"Warning: Failed to parse granularity results: {e}")
        granularity_results = {}

# Design documents: data/docs/{DOCS_SET} (default sample_doc)
docs_set = os.environ.get('DOCS_SET', 'sample_doc').strip()
documents_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'docs' / docs_set

# C repository root: C_REPO_ROOT or data/repos/{REPO_SET} (default sample_repo)
repo_set = os.environ.get('REPO_SET', 'sample_repo').strip()
repo_root = Path(os.environ.get('C_REPO_ROOT', f'data/repos/{repo_set}'))
if not repo_root.is_absolute():
    repo_root = (Path(__file__).parent.parent.parent / repo_root).resolve()

# Repository structure: repository_structure_{type}_{repo_set} (type: full, 500, 1000, 2000)
_structure_type = os.environ.get('REPOSITORY_STRUCTURE_TYPE', '2000').strip().lower()
if _structure_type not in ('full', '500', '1000', '2000'):
    _structure_type = '2000'
repository_structure = os.environ.get('REPOSITORY_STRUCTURE', f'repository_structure_{_structure_type}_{repo_set}')
structure_files_dir = Path(__file__).parent / 'prompt' / repository_structure
print(f"Using repository structure: {repository_structure}")

# Generate repo structure JSON and simplified structures if needed
repo_structure_json = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / f'repo_structure_{repo_set}.json'
force_rebuild = os.environ.get('FORCE_REBUILD_STRUCTURES', '0') == '1'

if force_rebuild or not repo_structure_json.exists():
    create_repo_script = Path(__file__).parent / 'create_c_repo_structure.py'
    print(f"Generating repo_structure_{repo_set}.json from: {repo_root}")
    result = subprocess.run([
        sys.executable, str(create_repo_script), str(repo_root), '-o', str(repo_structure_json)
    ], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)

if force_rebuild or not structure_files_dir.exists():
    create_simplified_script = Path(__file__).parent / 'create_simplified_repo_structure.py'
    print(f"Generating simplified repository structure: {repository_structure}")
    result = subprocess.run([
        sys.executable, str(create_simplified_script), '--output', repository_structure
    ], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)

# Output directory with timestamp
output_root = Path(__file__).parent / 'output'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = output_root / timestamp
output_dir.mkdir(parents=True, exist_ok=True)
output_json = output_dir / 'llm_outputs.json'

llm_outputs = {}

document_files = sorted(documents_dir.glob('*.md'))

# Filter proposal files based on granularity results if provided
if granularity_results:
    print(f"Filtering documents based on granularity results: {list(granularity_results.keys())}")
    # Filter for file and function granularity documents only
    file_function_documents = [
        df for df in document_files
        if df.name in granularity_results and granularity_results[df.name] in ["file", "function"]
    ]
    document_files = file_function_documents
    print(f"Found {len(document_files)} file/function granularity documents to process")
    print(f"Filtered from {len(list(documents_dir.glob('*.md')))} to {len(document_files)} documents")

total = len(document_files)

# Get all separate structure files
structure_files = sorted(structure_files_dir.glob('simplified_repo_structure_separate*.txt'))
if not structure_files:
    print(f"Error: No structure files found in {repository_structure}/", file=sys.stderr)
    sys.exit(1)

print(f"Found {len(structure_files)} structure files to process")
for sf in structure_files:
    print(f"  - {sf.name}")

print(f"Total document files found: {total}")
print("Starting document processing loop...")

for idx, document_file in enumerate(document_files, 1):
    print(f"Processing {idx}/{total}: {document_file.name}")
    sys.stdout.flush()
    # Skip empty files
    with open(document_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        print(f"Skipping {document_file.name}: file is empty.")
        sys.stdout.flush()
        continue
    
    print("  Processing document with granularity results from environment variable...")
    sys.stdout.flush()
    
    # Aggregate found files from all structure files
    all_found_files = set()
    
    # Process each structure file separately
    for structure_file in structure_files:
        print(f"  Processing with {structure_file.name}...")
        sys.stdout.flush()
        
        # Generate prompt using directory_and_file_level_localization.py
        prompt_script = Path(__file__).parent / 'prompt' / 'directory_and_file_level_localization.py'
        print(f"    Generating prompt using: {prompt_script}")
        sys.stdout.flush()
        # Pass both document_file and structure_file as arguments
        result = subprocess.run([
            sys.executable, str(prompt_script), str(document_file.resolve()), str(structure_file.resolve())
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"    Prompt generation failed for {structure_file.name}: {result.stderr}")
            sys.stdout.flush()
            continue
        
        prompt = result.stdout
        print(f"    Generated prompt length: {len(prompt)} characters")
        sys.stdout.flush()
        payload = build_chat_payload(
            [{"role": "user", "content": prompt}],
            temperature=0.0,
            model_for_payload=model_for_payload,
        )
        print(f"    Making API request to: {API_URL}")
        print(f"    Payload model: {payload.get('model', '(Azure deployment)')}, temperature: {payload['temperature']}")
        sys.stdout.flush()
        
        # Use retry logic for API calls
        success, response_data, error_msg = make_api_request_with_retry(API_URL, headers, payload, max_retries=3, base_delay=2)
        print(f"    LLM API status for {structure_file.name}: {'Success' if success else 'Failed'}")
        if not success and error_msg:
            print(f"    Error details: {error_msg}")
        sys.stdout.flush()
        
        if success:
            try:
                content = response_data['choices'][0]['message']['content']
                print(f"    LLM API raw output (first 200 chars):\n{content[:200]}\n---")
                sys.stdout.flush()
                
                # Try to parse the LLM output to extract found_files
                if content.startswith('```json'):
                    content = content[len('```json'):].strip()
                if content.startswith('```'):
                    content = content[len('```'):].strip()
                if content.endswith('```'):
                    content = content[:-3].strip()
                
                parsed = json.loads(content)
                files = parsed.get('found_files', [])
                all_found_files.update(files)
                print(f"    Parsed found_files: {files}")
                sys.stdout.flush()
                
            except Exception as e:
                print(f"    [ERROR] Failed to parse LLM output for {structure_file.name}: {e}")
                print(f"    [ERROR] Raw output was:\n{content}")
                sys.stdout.flush()
        else:
            print(f"    [ERROR] LLM API call failed for {structure_file.name}: {error_msg}")
            sys.stdout.flush()
    
    # Determine output format based on granularity
    proposal_granularity = granularity_results.get(document_file.name, "file")  # Default to "file"
    print(f"  Detected granularity for {document_file.name}: {proposal_granularity}")
    sys.stdout.flush()
    print(f"  Total files found across all structure files: {len(all_found_files)}")
    sys.stdout.flush()
    
    if proposal_granularity == "directory":
        # For directory granularity, group files by directory
        directories = set()
        for file_path in all_found_files:
            directory = str(Path(file_path).parent)
            if directory != '.':
                directories.add(directory)
            else:
                directories.add('.')  # Root directory
        
        llm_outputs[document_file.name] = {
            "granularity": "directory",
            "found_directories": list(directories),
            "found_files": list(all_found_files)  # Keep for reference
        }
        print(f"  Directory granularity - Found {len(directories)} directories, {len(all_found_files)} files")
        sys.stdout.flush()
    
    elif proposal_granularity == "file":
        # For file granularity, keep individual files
        llm_outputs[document_file.name] = {
            "granularity": "file", 
            "found_files": list(all_found_files)
        }
        print(f"  File granularity - Found {len(all_found_files)} files")
        sys.stdout.flush()
    
    elif proposal_granularity == "function":
        # For function granularity, keep files for later function-level processing
        llm_outputs[document_file.name] = {
            "granularity": "function",
            "found_files": list(all_found_files)
        }
        print(f"  Function granularity - Found {len(all_found_files)} files (for function-level processing)")
        sys.stdout.flush()
    
    else:
        # Fallback to file granularity
        llm_outputs[document_file.name] = {
            "granularity": "file",
            "found_files": list(all_found_files)
        }
        print(f"  Unknown granularity '{proposal_granularity}' - defaulting to file level")
        sys.stdout.flush()

# Save aggregated results
with open(output_json, 'w') as f:
    json.dump(llm_outputs, f, indent=2)

print(f"\nResults saved to: {output_json}")
print(f"Total proposals processed: {len(llm_outputs)}")
