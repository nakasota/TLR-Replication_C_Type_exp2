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

# Repository structure files directory
structure_files_dir = Path(__file__).parent / 'prompt' / 'repository_structure_1000'

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

# Get all separate structure files
structure_files = sorted(structure_files_dir.glob('simplified_repo_structure_separate*.txt'))
if not structure_files:
    print("Error: No structure files found in repository_structure_1000/", file=sys.stderr)
    sys.exit(1)

print(f"Found {len(structure_files)} structure files to process")
for sf in structure_files:
    print(f"  - {sf.name}")

for idx, proposal_file in enumerate(proposal_files, 1):
    print(f"Processing {idx}/{total}: {proposal_file.name}")
    # Skip empty or marker-only files
    with open(proposal_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines or (len(lines) == 1 and lines[0].lower() in ['accepted', 'likely accept']):
        print(f"Skipping {proposal_file.name}: file is empty or only contains marker.")
        continue
    
    # Aggregate found files from all structure files
    all_found_files = set()
    
    # Process each structure file separately
    for structure_file in structure_files:
        print(f"  Processing with {structure_file.name}...")
        
        # Generate prompt using directory_and_file_level_localization.py
        prompt_script = Path(__file__).parent / 'prompt' / 'directory_and_file_level_localization.py'
        # Pass both proposal_file and structure_file as arguments
        result = subprocess.run([
            sys.executable, str(prompt_script), str(proposal_file.resolve()), str(structure_file.resolve())
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"    Prompt generation failed for {structure_file.name}: {result.stderr}")
            continue
        
        prompt = result.stdout
        payload = {
            "model": "deepseek-chat",
            "temperature": 0.0,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        
        response = requests.post(API_URL, headers=headers, json=payload)
        print(f"    LLM API status for {structure_file.name}: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            try:
                content = data['choices'][0]['message']['content']
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
            print(f"    [ERROR] LLM API returned error for {structure_file.name}: {response.status_code} - {response.text}")
    
    # Store aggregated results for this proposal
    llm_outputs[proposal_file.name] = {"found_files": list(all_found_files)}
    print(f"  Total unique files found for {proposal_file.name}: {len(all_found_files)}")

# Save aggregated results
with open(output_json, 'w') as f:
    json.dump(llm_outputs, f, indent=2)

print(f"\nResults saved to: {output_json}")
print(f"Total proposals processed: {len(llm_outputs)}")
