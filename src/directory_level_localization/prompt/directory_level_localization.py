#!/usr/bin/env python3
"""
Generate an LLM prompt for directory level localization using separate repository structure files and a JSON output format, including design documents.
"""

from pathlib import Path
import sys
import os

# Accept document file and structure file as command-line arguments
if len(sys.argv) > 2:
    document_file = Path(sys.argv[1])
    structure_file = Path(sys.argv[2])
elif len(sys.argv) > 1:
    document_file = Path(sys.argv[1])
    # Default structure file for testing
    structure_file = Path(__file__).parent / "repository_structure_1000/simplified_repo_structure_separate1.txt"
else:
    # Default for manual testing
    document_file = Path(__file__).parent / "../../../data/docs/sample_doc/overview.md"
    structure_file = Path(__file__).parent / "repository_structure_1000/simplified_repo_structure_separate1.txt"

# Read the repository structure
with open(structure_file, "r") as f:
    repo_structure = f.read()

# Read the full content of the selected document
with open(document_file, "r") as df:
    document_content = df.read()
document_section = f"# Document: {document_file.name}\n" + document_content

# Define the output format instructions (Pydantic-style, JSON only)
output_format = """
Return a JSON object with the following format.
The response MUST:
- Be a valid JSON block.
- Contain a key `found_directories` with a list of directory paths.
- Output ONLY the raw JSON object. Do NOT include any markdown formatting (no ```json or ```).
- Do NOT add any explanations or additional text.
- If you are unsure which directories apply, return an empty list.

Example of correct output when directories are found:
{
  "found_directories": [
    "include/",
    "src/"
  ]
}

Example of correct output when directories are not found:
{
  "found_directories": []
}
""".strip()

# Compose the prompt
prompt = f'''
You are analyzing a C design document and repository to identify which directories are **most relevant** to the given document.

### Document Content ###
{document_section}

### C Repository Directory Structure ###
```
{repo_structure}
```

**CRITICAL INSTRUCTION:** 
You can ONLY select directories that are explicitly shown in the repository structure above. 
If the document discusses topics not covered by the directories in this structure, return an empty list.
Focus on *direct* relevance only: Only include items that are directly mentioned in the document. 

**Step-by-step process:**
1. Read the document title and content.  
2. Scan the repository structure above for matching directory paths.  
3. Include only those directories you actually see listed.  
4. If none match, return an empty list (`[]`).

Please output your answer in the following format:
{output_format}
'''

# Print the prompt (for immediate use)
try:
    print(prompt)
except BrokenPipeError:
    try:
        sys.stdout.flush()
        os._exit(0)
    except Exception:
        pass
