import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path
import json
import subprocess
from datetime import datetime
import ijson

# Load environment variables from .env
load_dotenv(dotenv_path=Path(__file__).parent.parent.parent / '.env')

API_KEY = os.getenv('DEEPSEEK_API_KEY')
if not API_KEY:
    print("Error: DEEPSEEK_API_KEY not found in .env file.", file=sys.stderr)
    sys.exit(1)

# Directory containing accepted proposals
proposals_dir = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals'

# Prompt user to select file-level output directory
file_level_output_root = Path(__file__).parent.parent / 'directory_and_file_level' / 'output'
if not file_level_output_root.exists() or not any(d.is_dir() for d in file_level_output_root.iterdir()):
    print('No file-level output found.', file=sys.stderr)
    sys.exit(1)
file_level_output_dirs = sorted([d for d in file_level_output_root.iterdir() if d.is_dir()], reverse=True)
print('Available file-level output directories:')
for i, d in enumerate(file_level_output_dirs):
    print(f"[{i}] {d.name}")
selected_idx = input(f"Select file-level output index [0-{len(file_level_output_dirs)-1}]: ")
try:
    selected_idx = int(selected_idx)
    if not (0 <= selected_idx < len(file_level_output_dirs)):
        raise ValueError
except Exception:
    print('Invalid selection.', file=sys.stderr)
    sys.exit(1)
file_level_output_dir = file_level_output_dirs[selected_idx]
file_level_llm_outputs = file_level_output_dir / 'llm_outputs.json'

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
# Only process proposals that exist in the selected file-level output
with open(file_level_llm_outputs, 'r') as f:
    file_level_results = json.load(f)
proposal_files = [p for p in proposal_files if p.name in file_level_results]
total = len(proposal_files)

if total == 0:
    print('No proposals to process for the selected file-level output.')
    sys.exit(0)

# Load repo structure mapping (nested dict)
repo_structure_path = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'go_repo_structure.json'
with open(repo_structure_path, 'r') as f:
    repo_structure = json.load(f)

for idx, proposal_file in enumerate(proposal_files, 1):
    print(f"[Progress] {idx}/{total}: {proposal_file.name}")
    proposal_id = proposal_file.name
    v = file_level_results.get(proposal_id)
    if not v or "found_files" not in v or not v["found_files"]:
        print(f"[SKIP] No found_files for {proposal_id}")
        continue
    found_files = v["found_files"]
    for file_path in found_files:
        if not file_path.endswith('.go'):
            print(f"[SKIP] {file_path} is not a Go source file")
            continue
        directory = os.path.dirname(file_path)
        # Check if file exists in the actual Go repository
        go_repo_path = Path(__file__).parent.parent.parent / 'data' / 'repos' / 'go'
        abs_file_path = go_repo_path / file_path
        if not abs_file_path.exists():
            print(f"[SKIP] {file_path} not found in Go repository")
            continue
        prompt_script = Path(__file__).parent / 'prompt' / 'function_level_localization.py'
        result = subprocess.run([
            sys.executable, str(prompt_script), str(proposal_file.resolve()), directory, abs_file_path
        ], capture_output=True, text=True)
        if result.returncode != 0 or not result.stdout.strip():
            print(f"[SKIP] Prompt generation failed for {proposal_id} in {file_path}")
            continue
        prompt = result.stdout
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
        except Exception as e:
            print(f"[ERROR] LLM API call failed for {proposal_id} in {file_path}: {e}")
            continue
        if response.status_code == 200:
            data = response.json()
            try:
                content = data['choices'][0]['message']['content']
                print(f"[LLM RAW OUTPUT] {proposal_id} | {file_path} | {content[:200]}")
                if content.startswith('```json'):
                    content = content[len('```json'):].strip()
                if content.startswith('```'):
                    content = content[len('```'):].strip()
                if content.endswith('```'):
                    content = content[:-3].strip()
                parsed = json.loads(content)
                functions = parsed.get('relevant_functions', [])
                if proposal_id not in llm_outputs:
                    llm_outputs[proposal_id] = {}
                llm_outputs[proposal_id][file_path] = functions
            except Exception:
                print(f"[ERROR] Failed to parse LLM output for {proposal_id} in {file_path}.")
        else:
            print(f"[ERROR] LLM API returned error: {response.status_code} for {proposal_id} in {file_path}.")

with open(output_json, 'w') as f:
    output_data = {"selected_file_level_output": file_level_output_dir.name}
    output_data.update(llm_outputs)
    json.dump(output_data, f, indent=2)
