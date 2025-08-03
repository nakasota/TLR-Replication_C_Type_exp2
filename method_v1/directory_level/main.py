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
total = len(proposal_files)

proposal_files = proposal_files
total = len(proposal_files)

for idx, proposal_file in enumerate(proposal_files, 1):
    print(f"Processing {idx}/{total}: {proposal_file.name}")
    # Skip empty or marker-only files
    with open(proposal_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines or (len(lines) == 1 and lines[0].lower() in ['accepted', 'likely accept']):
        print(f"Skipping {proposal_file.name}: file is empty or only contains marker.")
        continue
    # Generate prompt using directory_level_localization.py
    prompt_script = Path(__file__).parent / 'prompt' / 'directory_level_localization.py'
    # Pass the proposal_file as a string (absolute path)
    result = subprocess.run([
        sys.executable, str(prompt_script), str(proposal_file.resolve())
    ], capture_output=True, text=True)
    if result.returncode != 0:
        llm_outputs[proposal_file.name] = f"Prompt generation failed: {result.stderr}"
        continue
    prompt = result.stdout
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        llm_outputs[proposal_file.name] = data['choices'][0]['message']['content']
    else:
        llm_outputs[proposal_file.name] = f"Error: {response.status_code} - {response.text}"

with open(output_json, 'w') as f:
    json.dump(llm_outputs, f, indent=2)
