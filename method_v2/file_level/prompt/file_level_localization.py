#!/usr/bin/env python3
"""
Generate an LLM prompt for file-level localization using the full repository structure and a Pydantic output format, including proposals and directory-level localization results.
"""

from pathlib import Path
import sys
import os
import json

# Path to the full repository structure file (for file-level, use the full structure)
structure_file = Path(__file__).parent / "../../directory_level/prompt/simplified_repo_structure_full.txt"

def load_directory_level_localization(directory_level_json_path):
    with open(directory_level_json_path, "r") as f:
        return json.load(f)

# Accept proposal file and directory-level localization file as command-line arguments
if len(sys.argv) > 2:
    proposal_file = Path(sys.argv[1])
    directory_level_json = Path(sys.argv[2])
else:
    # Default for manual testing
    proposal_file = Path(__file__).parent / "../../../data/preprocess/accepted_proposals/evaluable_proposals/19367.md"
    directory_level_json = Path(__file__).parent / "../../../method_v1/directory_level/output/latest/llm_outputs.json"

# Read the repository structure
with open(structure_file, "r") as f:
    repo_structure = f.read()

# Read the full content of the selected proposal
with open(proposal_file, "r") as pf:
    proposal_content = pf.read()
proposals_section = f"# Proposal: {proposal_file.name}\n" + proposal_content

# Read the directory-level localization results
# Only include directories found by directory-level localization

directory_level_results = load_directory_level_localization(directory_level_json)

# Extract relevant directories from directory_level_results
if isinstance(directory_level_results, dict):
    # If the file is a dict of proposal_id -> result, pick the current proposal
    proposal_id = proposal_file.stem
    found_dirs = set()
    if proposal_id in directory_level_results:
        v = directory_level_results[proposal_id]
        if isinstance(v, str):
            try:
                v = json.loads(v)
            except Exception:
                v = {}
        found_dirs = set(v.get('found_directories', []))
    else:
        found_dirs = set()
else:
    found_dirs = set(directory_level_results.get('found_directories', []))

# Filter the repo structure to only include the directories found by directory-level localization
localized_structure_lines = []
for line in repo_structure.splitlines():
    for d in found_dirs:
        if line.strip().startswith(d + "/") or line.strip() == d:
            localized_structure_lines.append(line)
            break
localized_repo_structure = '\n'.join(localized_structure_lines)

# Define the output format instructions (Pydantic-style, JSON only)
file_output_format = """
Return a JSON object with the following format.
The response MUST:
- Be a valid JSON block.
- Contain a key `found_files` with a list of file paths.
- Each file path must be a string like "src/crypto/dsa/dsa.go" or "src/net/http/server.go".
- Output ONLY the raw JSON object. Do NOT include any markdown formatting (no ```json or ```).
- Do NOT add any explanations or additional text.

Example of correct output:
{
  "found_files": [
    "src/crypto/dsa/dsa.go",
    "src/net/http/server.go"
  ]
}
""".strip()

# Compose the prompt
prompt = f'''
You are analyzing a Go proposal and repository to identify which files are **most relevant** to the given proposal.

### Proposal Content ###
{proposals_section}

### Localized Go Repository Directory Structure ###
```
{localized_repo_structure}
```

### Directory-Level Localization Results ###
{json.dumps(list(found_dirs), indent=2)}

**CRITICAL OBJECTIVE**: Identify the **most relevant files** that are closely related to the proposal topic and discussion.

**MANDATORY OUTPUT FORMAT:**
{file_output_format}

**MANDATORY SELECTION RULES:**
- Select only the most essential files, not directories.
- Only include files that are directly related to the accepted proposals.
- The output must strictly follow the format.
- If you are unsure, make your best guess based on the structure.
'''

# Save the prompt to a file (optional)
with open(Path(__file__).parent / "llm_prompt.txt", "w") as f:
    f.write(prompt)

# Print the prompt (for immediate use)
try:
    print(prompt)
except BrokenPipeError:
    try:
        sys.stdout.flush()
        os._exit(0)
    except Exception:
        pass
