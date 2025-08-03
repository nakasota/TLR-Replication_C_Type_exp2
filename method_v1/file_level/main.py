import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path
import json
import subprocess
from datetime import datetime

# Load environment variables from .env
load_dotenv(dotenv_path=Path(__file__).parent.parent.parent / '.env')

API_KEY = os.getenv('DEEPSEEK_API_KEY')
if not API_KEY:
    print("Error: DEEPSEEK_API_KEY not found in .env file.", file=sys.stderr)
    sys.exit(1)

# Directory containing accepted proposals
proposals_dir = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals'

# Directory-level LLM output (should be generated before running this script)
directory_level_output_root = Path(__file__).parent.parent.parent / 'method_v1' / 'directory_level' / 'output'
# Prompt user to select directory-level output if multiple exist
if not directory_level_output_root.exists() or not any(d.is_dir() for d in directory_level_output_root.iterdir()):
    print('No directory-level output found.', file=sys.stderr)
    sys.exit(1)
directory_level_output_dirs = sorted([d for d in directory_level_output_root.iterdir() if d.is_dir()], reverse=True)

print('Available directory-level output directories:')
for i, d in enumerate(directory_level_output_dirs):
    print(f"[{i}] {d.name}")
selected_idx = input(f"Select directory-level output index [0-{len(directory_level_output_dirs)-1}]: ")
try:
    selected_idx = int(selected_idx)
    if not (0 <= selected_idx < len(directory_level_output_dirs)):
        raise ValueError
except Exception:
    print('Invalid selection.', file=sys.stderr)
    sys.exit(1)
directory_level_output_dir = directory_level_output_dirs[selected_idx]
directory_level_llm_outputs = directory_level_output_dir / 'llm_outputs.json'

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
# Only process proposals that exist in the selected directory-level output
with open(directory_level_llm_outputs, 'r') as f:
    dir_level_results = json.load(f)
proposal_files = [p for p in proposal_files if p.name in dir_level_results]
total = len(proposal_files)

if total == 0:
    print('No proposals to process for the selected directory-level output.')
    sys.exit(0)

for idx, proposal_file in enumerate(proposal_files, 1):
    print(f"Processing {idx}/{total}: {proposal_file.name}")
    # Skip empty or marker-only files
    with open(proposal_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines or (len(lines) == 1 and lines[0].lower() in ['accepted', 'likely accept']):
        print(f"Skipping {proposal_file.name}: file is empty or only contains marker.")
        continue
    # Load directory-level localization result for this proposal
    proposal_id = proposal_file.name  # Use full filename with .md
    found_dirs = set()
    if proposal_id in dir_level_results:
        v = dir_level_results[proposal_id]
        # Robustly parse v to handle string, code block, or dict
        if isinstance(v, str):
            v = v.strip()
            if v.startswith('```json'):
                v = v[len('```json'):].strip()
            if v.startswith('```'):
                v = v[len('```'):].strip()
            if v.endswith('```'):
                v = v[:-3].strip()
            try:
                v = json.loads(v)
            except Exception:
                v = {}
        found_dirs = set(v.get('found_directories', []))
    else:
        found_dirs = set()
    proposal_found_files = set()
    for d in found_dirs:
        # Generate prompt using file_level_localization.py for each directory
        prompt_script = Path(__file__).parent / 'prompt' / 'file_level_localization.py'
        result = subprocess.run([
            sys.executable, str(prompt_script), str(proposal_file.resolve()), str(directory_level_llm_outputs.resolve()), d
        ], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Prompt generation failed for {proposal_file.name} in directory {d}: {result.stderr}")
            continue
        prompt = result.stdout
        # Remove prompt preview from terminal output for privacy/cleanliness
        # print(f"Prompt for {proposal_file.name} in {d} (first 500 chars):\n{prompt[:500]}\n---")
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        print(f"[INFO] LLM API status for {proposal_file.name} in {d}: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            try:
                content = data['choices'][0]['message']['content']
                print(f"[INFO] LLM API raw output (first 200 chars):\n{content[:200]}\n---")
                # Try to parse the LLM output to extract found_files
                if content.startswith('```json'):
                    content = content[len('```json'):].strip()
                if content.startswith('```'):
                    content = content[len('```'):].strip()
                if content.endswith('```'):
                    content = content[:-3].strip()
                parsed = json.loads(content)
                files = parsed.get('found_files', [])
                proposal_found_files.update(files)
                print(f"[INFO] Parsed found_files: {files}")
            except Exception as e:
                print(f"[ERROR] Failed to parse LLM output: {e}\n[ERROR] Raw output was:\n{content}")
        else:
            print(f"[ERROR] LLM API returned error: {response.status_code} - {response.text}")
    llm_outputs[proposal_file.name] = {"found_files": list(proposal_found_files)}

with open(output_json, 'w') as f:
    # Add selected directory-level output as a top-level key
    output_data = {"selected_directory_level_output": directory_level_output_dir.name}
    output_data.update(llm_outputs)
    json.dump(output_data, f, indent=2)
