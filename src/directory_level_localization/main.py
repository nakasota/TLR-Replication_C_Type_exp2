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
sys.path.append(str(Path(__file__).parent / 'prompt'))
from directory_level_localization import generate_directory_level_localization_diff_prompt

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
                sys.stdout.flush()
                if attempt < max_retries:
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    time.sleep(delay)
                    continue
            else:
                print(f"    [ERROR] API returned status {response.status_code}, attempt {attempt + 1}/{max_retries + 1}")
                sys.stdout.flush()
                if attempt < max_retries:
                    delay = base_delay * (2 ** attempt)
                    time.sleep(delay)
                    continue
                    
        except requests.exceptions.SSLError as e:
            print(f"    [RETRY] SSL error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            sys.stdout.flush()
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                time.sleep(delay)
                continue
                
        except requests.exceptions.ConnectionError as e:
            print(f"    [RETRY] Connection error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            sys.stdout.flush()
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                time.sleep(delay)
                continue
                
        except requests.exceptions.Timeout as e:
            print(f"    [RETRY] Timeout on attempt {attempt + 1}/{max_retries + 1}: {e}")
            sys.stdout.flush()
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
                continue
                
        except Exception as e:
            print(f"    [RETRY] Unexpected error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            sys.stdout.flush()
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
    raise ValueError(str(e)) from e

# Load granularity results from environment variable
granularity_results_env = os.environ.get('GRANULARITY_RESULTS', '{}')
try:
    granularity_results = json.loads(granularity_results_env)
    print(f"Loaded granularity results: {len(granularity_results)} documents")
    sys.stdout.flush()
except json.JSONDecodeError:
    print("Warning: Could not parse GRANULARITY_RESULTS environment variable. Processing all documents.")
    sys.stdout.flush()
    granularity_results = {}

# Diff mode: DOCS_DIFF_SET set → read from data/docs_diff/{DOCS_DIFF_SET}/
docs_diff_set = os.environ.get('DOCS_DIFF_SET', '').strip()
if docs_diff_set:
    documents_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'docs_diff' / docs_diff_set
    diff_mode = True
else:
    docs_set = os.environ.get('DOCS_SET', 'sample_doc').strip()
    documents_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'docs' / docs_set
    diff_mode = False

# C repository root: C_REPO_ROOT or data/repos/{REPO_SET} (default REPO_SET=sample_repo)
repo_set = os.environ.get('REPO_SET', 'sample_repo').strip()
repo_root = Path(os.environ.get('C_REPO_ROOT', f'data/repos/{repo_set}'))
if not repo_root.is_absolute():
    repo_root = (Path(__file__).parent.parent.parent / repo_root).resolve()

# Repository structure: repository_structure_{type}_{repo_set} (type: full, 500, 1000, 2000)
_structure_type = os.environ.get('REPOSITORY_STRUCTURE_TYPE', '2000').strip().lower()
if _structure_type not in ('full', '500', '1000', '2000'):
    _structure_type = '2000'
repo_structure = os.environ.get('REPOSITORY_STRUCTURE', f'repository_structure_{_structure_type}_{repo_set}')
print(f"Using repository structure: {repo_structure}")
sys.stdout.flush()

# Repository structure files directory
repo_structure_dir = Path(__file__).parent / 'prompt' / repo_structure

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

structure_files = sorted(repo_structure_dir.glob('simplified_repo_structure_separate*.txt'))
if force_rebuild or not structure_files:
    create_simplified_script = Path(__file__).parent / 'create_simplified_repo_structure.py'
    print(f"Generating simplified repository structure: {repo_structure}")
    result = subprocess.run([
        sys.executable, str(create_simplified_script), '--output', repo_structure
    ], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)

# Build directory index for validation
with open(repo_structure_json, 'r') as f:
    repo_structure_data = json.load(f)

repo_directories = set()
for file_path in repo_structure_data.keys():
    parts = Path(file_path).parts
    for i in range(1, len(parts)):
        repo_directories.add("/".join(parts[:i]) + "/")

# Output directory with timestamp
output_root = Path(__file__).parent / 'output'
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_dir = output_root / timestamp
output_dir.mkdir(parents=True, exist_ok=True)
output_json = output_dir / 'llm_outputs.json'

print(f"Output will be saved to: {output_json}")
sys.stdout.flush()

# Process proposals
llm_outputs = {}

if diff_mode:
    document_files = sorted([d for d in documents_dir.iterdir() if d.is_dir() and (d / 'base.md').exists()], key=lambda p: p.name)
else:
    document_files = sorted(documents_dir.glob('*.md'))

# Filter for directory granularity documents only if results provided
if granularity_results:
    directory_documents = [
        name for name, granularity in granularity_results.items()
        if granularity == "directory"
    ]
    if directory_documents:
        if diff_mode:
            document_files = [documents_dir / name for name in directory_documents if (documents_dir / name).is_dir() and (documents_dir / name / 'base.md').exists()]
        else:
            document_files = [documents_dir / name for name in directory_documents if (documents_dir / name).exists()]
        print(f"Processing {len(document_files)} directory granularity documents: {[df.name for df in document_files]}")
        sys.stdout.flush()

total = len(document_files)

# Get all separate structure files
structure_files = sorted(repo_structure_dir.glob('simplified_repo_structure_separate*.txt'))
if not structure_files:
    print(f"Error: No structure files found in {repo_structure}/", file=sys.stderr)
    sys.stderr.flush()
    sys.exit(1)

print(f"Found {len(structure_files)} structure files to process")
sys.stdout.flush()
for sf in structure_files:
    print(f"  - {sf.name}")
sys.stdout.flush()

for idx, document_file in enumerate(document_files, 1):
    print(f"Processing {idx}/{total}: {document_file.name}")
    sys.stdout.flush()
    if not diff_mode:
        with open(document_file, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines:
            print(f"Skipping {document_file.name}: file is empty.")
            sys.stdout.flush()
            continue
    
    # Aggregate found files from all structure files
    all_found_files = set()
    all_found_directories = set()
    
    # Process each structure file separately
    for structure_file in structure_files:
        print(f"  Processing with {structure_file.name}...")
        sys.stdout.flush()
        
        if diff_mode:
            with open(document_file / 'base.md', 'r', encoding='utf-8') as f:
                base_text = f.read()
            with open(document_file / 'changed.md', 'r', encoding='utf-8') as f:
                changed_text = f.read()
            with open(structure_file, 'r', encoding='utf-8') as f:
                chunk = f.read()
            prompt = generate_directory_level_localization_diff_prompt(base_text, changed_text, chunk)
        else:
            # Generate prompt using directory_level_localization.py
            prompt_script = Path(__file__).parent / 'prompt' / 'directory_level_localization.py'
            result = subprocess.run([
                sys.executable, str(prompt_script), str(document_file.resolve()), str(structure_file.resolve())
            ], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"    Prompt generation failed for {structure_file.name}: {result.stderr}")
                sys.stdout.flush()
                continue
            prompt = result.stdout
        
        # Log prompt if LOG_PROMPTS is enabled
        if os.environ.get('LOG_PROMPTS', '0') == '1':
            print(f"\n{'='*70}")
            print(f"[PROMPT LOG] Document: {document_file.name}, Structure: {structure_file.name}")
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
        print(f"    LLM API status for {structure_file.name}: {'Success' if success else 'Failed'}")
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
                
                # Try to parse the LLM output to extract found_files and found_directories
                parsed = json.loads(content)
                
                # Extract files
                files = parsed.get('found_files', [])
                all_found_files.update(files)
                print(f"    Parsed found_files: {files}")
                sys.stdout.flush()
                
                # Extract directories and validate against repo structure
                directories = parsed.get('found_directories', [])
                normalized_dirs = []
                for directory in directories:
                    normalized = directory if directory.endswith("/") else directory + "/"
                    if normalized in repo_directories:
                        normalized_dirs.append(normalized)
                all_found_directories.update(normalized_dirs)
                print(f"    Parsed found_directories: {normalized_dirs}")
                sys.stdout.flush()
                
            except Exception as e:
                print(f"    [ERROR] Failed to parse LLM output for {structure_file.name}: {e}")
                print(f"    [ERROR] Raw output was:\n{content}")
                sys.stdout.flush()
        else:
            print(f"    [ERROR] LLM API call failed for {structure_file.name}: {error_msg}")
            sys.stdout.flush()
    
    # Store aggregated results for this document
    llm_outputs[document_file.name] = {
        "found_files": list(all_found_files),
        "found_directories": list(all_found_directories)
    }
    print(f"  Total unique files found for {document_file.name}: {len(all_found_files)}")
    print(f"  Total unique directories found for {document_file.name}: {len(all_found_directories)}")
    sys.stdout.flush()

# Save aggregated results
with open(output_json, 'w') as f:
    json.dump(llm_outputs, f, indent=2)

print(f"\nResults saved to: {output_json}")
print(f"Total proposals processed: {len(llm_outputs)}")
sys.stdout.flush()
