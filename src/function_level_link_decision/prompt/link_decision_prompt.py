def generate_link_decision_prompt(proposal_text, file_path, function_name, function_code, function_context):
    """
    Generate prompt for link decision analysis (design document vs C function).
    """
    return f'''You are analyzing whether a specific C function is directly relevant to a given design document.

### Design Document ###
{proposal_text}

### Function Information ###
File: {file_path}
Function Name: {function_name}

### Function Source Code ###
{function_code}

**OBJECTIVE**: Determine if this specific function is **relevant** to the design document.

**IMPORTANT GUIDELINES:**
- Only answer "Yes" if the function is **directly relevant** to the document's main topic
- Otherwise, answer "No"
- Focus on *direct* relevance only: only "Yes" if the function is directly mentioned or clearly implied by the document.

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "Yes" or "No"

Do NOT include any explanations, reasoning, or additional text.'''


def generate_link_decision_diff_prompt(base_spec_text: str, changed_spec_text: str, file_path: str, function_name: str, function_code: str):
    """
    Generate prompt for link decision in diff (change-driven) mode.
    Given base and changed spec sections, determine if this specific function was the one modified.
    """
    return f'''You are analyzing whether a specific C function was **modified** to implement a specification change. Two specification sections are given: the base (before) and the changed (after) version.

### Base Specification (Before Change) ###
{base_spec_text}

### Changed Specification (After Change) ###
{changed_spec_text}

### Function Information ###
File: {file_path}
Function Name: {function_name}

### Function Source Code ###
{function_code}

**OBJECTIVE**: Determine if this specific function was the one **modified** to implement the specification change.

**IMPORTANT GUIDELINES:**
- Answer "Yes" only if this function directly implements the changed specification.
- Otherwise, answer "No"
- Focus on whether the function's behavior matches the changed spec.

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "Yes" or "No"

Do NOT include any explanations, reasoning, or additional text.'''
