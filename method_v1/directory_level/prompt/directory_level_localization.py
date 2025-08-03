#!/usr/bin/env python3
"""
Generate an LLM prompt for directory-level localization using the full repository structure and a Pydantic output format, including proposals.
"""

from pathlib import Path
import sys
import os

# Path to the full repository structure file
structure_file = Path(__file__).parent / "simplified_repo_structure_limited.txt"

# Accept proposal file as a command-line argument
if len(sys.argv) > 1:
    proposal_file = Path(sys.argv[1])
else:
    # Default for manual testing
    proposal_file = Path(__file__).parent / "../../../data/preprocess/accepted_proposals/evaluable_proposals/19367.md"

# Read the repository structure
with open(structure_file, "r") as f:
    repo_structure = f.read()

# Read the full content of the selected proposal
with open(proposal_file, "r") as pf:
    proposal_content = pf.read()
proposals_section = f"# Proposal: {proposal_file.name}\n" + proposal_content

# Define the output format instructions (Pydantic-style, JSON only)
directory_output_format = """
Return a JSON object with the following format.
The response MUST:
- Be a valid JSON block.
- Contain a key `found_directories` with a list of directory paths.
- Each directory path must be a string like "src/crypto/dsa" or "src/net/http".
- Output ONLY the raw JSON object. Do NOT include any markdown formatting (no ```json or ```).
- Do NOT add any explanations or additional text.

Example of correct output:
{
  "found_directories": [
    "src/crypto/dsa",
    "src/net/http",
    "src/cmd/go"
  ]
}
""".strip()

# Compose the prompt
prompt = f'''
You are analyzing a Go proposal and repository to identify which directories are **most relevant** to the given proposal.

### Proposal Content ###
{proposals_section}

### Go Repository Directory Structure ###
```
{repo_structure}
```

**CRITICAL OBJECTIVE**: Identify the **most relevant directories** that are closely related to the proposal topic and discussion.

**MANDATORY SELECTION RULES - DEEPEST LEAF DIRECTORIES ONLY:**
⚠️  **NEVER SELECT PARENT DIRECTORIES** - Always choose the deepest, most specific directory available
⚠️  **SELECT ONLY THE MOST RELEVANT DIRECTORIES** - Select only the most essential directories
⚠️  **LEAF PACKAGES ONLY** - Select directories that contain actual .go files, not parent directories

Please output your answer in the following format:
{directory_output_format}

Instructions:
- Only include directories that are directly related to the accepted proposals.
- Do not include files, only directories.
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
