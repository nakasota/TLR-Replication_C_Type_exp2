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
