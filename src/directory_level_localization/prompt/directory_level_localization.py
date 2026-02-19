#!/usr/bin/env python3
"""
Generate an LLM prompt for directory level localization using separate repository structure files and a JSON output format, including design documents.
"""

from pathlib import Path
import sys
import os

if __name__ == "__main__":
    # Script mode: accept document file and structure file as arguments
    if len(sys.argv) > 2:
        document_file = Path(sys.argv[1])
        structure_file = Path(sys.argv[2])
    elif len(sys.argv) > 1:
        document_file = Path(sys.argv[1])
        structure_file = Path(__file__).parent / "repository_structure_1000/simplified_repo_structure_separate1.txt"
    else:
        document_file = Path(__file__).parent / "../../../data/docs/sample_doc/overview.md"
        structure_file = Path(__file__).parent / "repository_structure_1000/simplified_repo_structure_separate1.txt"

    with open(structure_file, "r") as f:
        repo_structure = f.read()
    with open(document_file, "r") as df:
        document_content = df.read()
    document_section = f"# Document: {document_file.name}\n" + document_content

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

    try:
        print(prompt)
    except BrokenPipeError:
        try:
            sys.stdout.flush()
            os._exit(0)
        except Exception:
            pass


def generate_directory_level_localization_diff_prompt(base_spec_text: str, changed_spec_text: str, repo_structure: str) -> str:
    """
    Generate prompt for directory level localization in diff (change-driven) mode.
    Given base and changed spec sections, identify which directories are **related to the changed area**.
    """
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
    "src/modules/",
    "include/"
  ]
}

Example of correct output when directories are not found:
{
  "found_directories": []
}
""".strip()
    return f'''
You are analyzing a specification change to identify which C source directories are **related to the changed area**. Two specification sections are given: the base (before) and the changed (after) version.

### Base Specification (Before Change) ###
{base_spec_text}

### Changed Specification (After Change) ###
{changed_spec_text}

### C Repository Directory Structure ###
```
{repo_structure}
```

**CRITICAL INSTRUCTION:** 
You can ONLY select directories that are explicitly shown in the repository structure above. 
Select directory(ies) that are **related to the changed area** — i.e., directories that would contain code affected by or implementing the specification change.

**Step-by-step process:**
1. Compare the base and changed specifications to understand what changed.
2. Scan the repository structure above for directory paths related to the changed area.
3. Include only those directories you actually see listed.
4. If none match, return an empty list (`[]`).

Please output your answer in the following format:
{output_format}
'''
