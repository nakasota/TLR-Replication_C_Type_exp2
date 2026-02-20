def generate_file_level_link_decision_prompt(document_text, file_path, skeleton_view):
    """
    Generate prompt for file-level link decision analysis
    Using only proposal_text, file_path, and skeleton_view for focused analysis
    """
    return f'''You are analyzing whether a specific C file is directly relevant to a given C design document.

### C Design Document ###
{document_text}

### File Information ###
File: {file_path}

### File Skeleton View ###
{skeleton_view}

**OBJECTIVE**: Determine if this specific file is **relevant** to the design document.

**IMPORTANT GUIDELINES:**
- Only answer "Yes" if the file is **relevant** to the document's main topic
- Otherwise, answer "No"
- Consider the file's skeleton view, function signatures, types, and overall structure
- Focus on *direct* relevance only: Only include items that are directly mentioned in the document. 

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "Yes" or "No"

Do NOT include any explanations, reasoning, or additional text.'''


def generate_file_level_link_decision_diff_prompt(base_spec_text: str, changed_spec_text: str, file_path: str, skeleton_view: str) -> str:
    """
    Generate prompt for file-level link decision in diff (change-driven) mode.
    Given base and changed spec sections, determine if this specific file is **related to the changed area**.
    """
    return f'''You are analyzing whether a specific C file is **related to the changed area** of a specification change. Two specification sections are given: the base (before) and the changed (after) version.

### Base Specification (Before Change) ###
{base_spec_text}

### Changed Specification (After Change) ###
{changed_spec_text}

### File Information ###
File: {file_path}

### File Skeleton View ###
{skeleton_view}

**OBJECTIVE**: Determine if this file is related to the changed area — i.e., the file that the spec change refers to and that would contain code affected by or implementing the change.

**IMPORTANT GUIDELINES:**
- Answer "Yes" if the specification change explicitly refers to this file (by name, path, or content) or if this file would contain code related to the change.
- Answer "No" only if the spec change clearly refers to a different file or this file is unrelated to the change.
- Focus on whether the file's contents (skeleton, functions, types) are related to the changed area.

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "Yes" or "No"

Do NOT include any explanations, reasoning, or additional text.'''
