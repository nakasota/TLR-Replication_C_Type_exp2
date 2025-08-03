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

API_KEY = os.getenv('DEEPSEEK_API_KEY')
if not API_KEY:
    print("Error: DEEPSEEK_API_KEY not found in .env file.", file=sys.stderr)
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

# Directory containing accepted proposals
proposals_dir = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'declined_proposals' / 'cleaned_declined_proposals'

# Repository structure files directory (configurable via environment variable)
repository_structure = os.environ.get('REPOSITORY_STRUCTURE', 'repository_structure_2000')
structure_files_dir = Path(__file__).parent / 'prompt' / repository_structure
print(f"Using repository structure: {repository_structure}")

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

# Filter proposal files based on granularity results if provided
if granularity_results:
    print(f"Filtering proposals based on granularity results: {list(granularity_results.keys())}")
    proposal_files = [pf for pf in proposal_files if pf.name in granularity_results]
    print(f"Filtered from {len(list(proposals_dir.glob('*.md')))} to {len(proposal_files)} proposals")

total = len(proposal_files)

# Get all separate structure files
structure_files = sorted(structure_files_dir.glob('simplified_repo_structure_separate*.txt'))
if not structure_files:
    print(f"Error: No structure files found in {repository_structure}/", file=sys.stderr)
    sys.exit(1)

print(f"Found {len(structure_files)} structure files to process")
for sf in structure_files:
    print(f"  - {sf.name}")

print(f"Total proposal files found: {total}")
print("Starting proposal processing loop...")

for idx, proposal_file in enumerate(proposal_files, 1):
    print(f"Processing {idx}/{total}: {proposal_file.name}")
    # Skip empty or marker-only files
    with open(proposal_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines or (len(lines) == 1 and lines[0].lower() in ['accepted', 'likely accept']):
        print(f"Skipping {proposal_file.name}: file is empty or only contains marker.")
        continue
    
    print(f"  Processing proposal with granularity results from environment variable...")
    
    # Aggregate found files from all structure files
    all_found_files = set()
    
    # Process each structure file separately
    for structure_file in structure_files:
        print(f"  Processing with {structure_file.name}...")
        
        # Generate prompt using directory_and_file_level_localization.py
        prompt_script = Path(__file__).parent / 'prompt' / 'directory_and_file_level_localization.py'
        print(f"    Generating prompt using: {prompt_script}")
        # Pass both proposal_file and structure_file as arguments
        result = subprocess.run([
            sys.executable, str(prompt_script), str(proposal_file.resolve()), str(structure_file.resolve())
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"    Prompt generation failed for {structure_file.name}: {result.stderr}")
            continue
        
        prompt = result.stdout
        print(f"    Generated prompt length: {len(prompt)} characters")
        payload = {
            "model": "deepseek-chat",
            "temperature": 0.0,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        print(f"    Making API request to: {API_URL}")
        print(f"    Payload model: {payload['model']}, temperature: {payload['temperature']}")
        
        # Use retry logic for API calls
        success, response_data, error_msg = make_api_request_with_retry(API_URL, headers, payload, max_retries=3, base_delay=2)
        print(f"    LLM API status for {structure_file.name}: {'Success' if success else 'Failed'}")
        if not success and error_msg:
            print(f"    Error details: {error_msg}")
        
        if success:
            try:
                content = response_data['choices'][0]['message']['content']
                print(f"    LLM API raw output (first 200 chars):\n{content[:200]}\n---")
                
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
                
            except Exception as e:
                print(f"    [ERROR] Failed to parse LLM output for {structure_file.name}: {e}")
                print(f"    [ERROR] Raw output was:\n{content}")
        else:
            print(f"    [ERROR] LLM API call failed for {structure_file.name}: {error_msg}")
    
    # Determine output format based on granularity
    proposal_granularity = granularity_results.get(proposal_file.name, "file")  # Default to "file"
    print(f"  Detected granularity for {proposal_file.name}: {proposal_granularity}")
    print(f"  Total files found across all structure files: {len(all_found_files)}")
    
    if proposal_granularity == "directory":
        # For directory granularity, group files by directory
        directories = set()
        for file_path in all_found_files:
            directory = str(Path(file_path).parent)
            if directory != '.':
                directories.add(directory)
            else:
                directories.add('.')  # Root directory
        
        llm_outputs[proposal_file.name] = {
            "granularity": "directory",
            "found_directories": list(directories),
            "found_files": list(all_found_files)  # Keep for reference
        }
        print(f"  Directory granularity - Found {len(directories)} directories, {len(all_found_files)} files")
    
    elif proposal_granularity == "file":
        # For file granularity, keep individual files
        llm_outputs[proposal_file.name] = {
            "granularity": "file", 
            "found_files": list(all_found_files)
        }
        print(f"  File granularity - Found {len(all_found_files)} files")
    
    elif proposal_granularity == "function":
        # For function granularity, keep files for later function-level processing
        llm_outputs[proposal_file.name] = {
            "granularity": "function",
            "found_files": list(all_found_files)
        }
        print(f"  Function granularity - Found {len(all_found_files)} files (for function-level processing)")
    
    else:
        # Fallback to file granularity
        llm_outputs[proposal_file.name] = {
            "granularity": "file",
            "found_files": list(all_found_files)
        }
        print(f"  Unknown granularity '{proposal_granularity}' - defaulting to file level")

# Save aggregated results
with open(output_json, 'w') as f:
    json.dump(llm_outputs, f, indent=2)

print(f"\nResults saved to: {output_json}")
print(f"Total proposals processed: {len(llm_outputs)}")
