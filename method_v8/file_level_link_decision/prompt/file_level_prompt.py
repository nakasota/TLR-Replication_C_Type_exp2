def generate_file_level_link_decision_prompt(proposal_text, file_path, skeleton_view):
    """
    Generate prompt for file-level link decision analysis
    Using only proposal_text, file_path, and skeleton_view for focused analysis
    """
    return f'''You are analyzing whether a specific Go file is directly relevant to a given Go proposal.

### Go Proposal ###
{proposal_text}

### File Information ###
File: {file_path}

### File Skeleton View ###
{skeleton_view}

**OBJECTIVE**: Determine if this specific file is **relevant** to implementing or being affected by the Go proposal.

**IMPORTANT GUIDELINES:**
- Only answer "Yes" if the file is **relevant** to the proposal's main topic
- Otherwise, answer "No"
- Consider the file's skeleton view, function signatures, types, and overall structure

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "Yes" or "No"

Do NOT include any explanations, reasoning, or additional text.'''


