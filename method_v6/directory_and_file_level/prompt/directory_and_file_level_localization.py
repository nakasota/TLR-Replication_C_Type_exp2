#!/usr/bin/env python3
"""
Generate an LLM prompt for directory and file level localization using separate repository structure files and a Pydantic output format, including proposals.
"""

from pathlib import Path
import sys
import os

# Accept proposal file and structure file as command-line arguments
if len(sys.argv) > 2:
    proposal_file = Path(sys.argv[1])
    structure_file = Path(sys.argv[2])
elif len(sys.argv) > 1:
    proposal_file = Path(sys.argv[1])
    # Default structure file for testing
    structure_file = Path(__file__).parent / "repository_structure_1000/simplified_repo_structure_separate1.txt"
else:
    # Default for manual testing
    proposal_file = Path(__file__).parent / "../../../data/preprocess/accepted_proposals/evaluable_proposals/19367.md"
    structure_file = Path(__file__).parent / "repository_structure_1000/simplified_repo_structure_separate1.txt"

# Read the repository structure
with open(structure_file, "r") as f:
    repo_structure = f.read()

# Read the full content of the selected proposal
with open(proposal_file, "r") as pf:
    proposal_content = pf.read()
proposals_section = f"# Proposal: {proposal_file.name}\n" + proposal_content

# Define the output format instructions (Pydantic-style, JSON only)
output_format = """
Return a JSON object with the following format.
The response MUST:
- Be a valid JSON block.
- Contain a key `found_files` with a list of file paths.
- Output ONLY the raw JSON object. Do NOT include any markdown formatting (no ```json or ```).
- Do NOT add any explanations or additional text.
- If you are unsure which files apply, return an empty list.

Example of correct output when files are found:
{
  "found_files": [
    "src/crypto/dsa/dsa.go",
    "src/net/http/server.go"
  ]
}

Example of correct output when files are not found:
{
  "found_files": []
}
""".strip()

# Compose the prompt
prompt = f'''
You are analyzing a Go proposal and repository to identify which files are **most relevant** to the given proposal.

### Proposal Content ###
{proposals_section}

### Go Repository Directory Structure ###
```
{repo_structure}
```

**CRITICAL INSTRUCTION:** 
You can ONLY select files that are explicitly shown in the repository structure above. 
If the proposal discusses topics not covered by the files in this structure, return an empty list.

**Step-by-step process:**
1. Read the proposal title and content.  
2. Scan the repository structure above for matching file paths.  
3. Include only those files you actually see listed.  
4. If none match, return an empty list (`[]`).

Please output your answer in the following format:
{output_format}
'''

# Save the prompt to a file (optional, with structure file suffix)
structure_suffix = structure_file.stem.split('_')[-1]  # e.g., "separate1"
prompt_file = Path(__file__).parent / f"llm_prompt_{structure_suffix}.txt"
with open(prompt_file, "w") as f:
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
