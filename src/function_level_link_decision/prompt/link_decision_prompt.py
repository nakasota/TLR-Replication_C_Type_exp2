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
    Given base and changed spec sections, determine if this function is **related to the changed area**.
    """
    return f'''You are analyzing whether a specific C function is **related to the changed area** of a specification change. Two specification sections are given: the base (before) and the changed (after) version.

### Base Specification (Before Change) ###
{base_spec_text}

### Changed Specification (After Change) ###
{changed_spec_text}

### Function Information ###
File: {file_path}
Function Name: {function_name}

### Function Source Code ###
{function_code}

**OBJECTIVE**: Determine if this function is related to the changed area — i.e., the function that the spec change explicitly refers to (by name or behavior) and that would need to be modified to implement the change.

**IMPORTANT GUIDELINES:**
- Answer "Yes" if the specification change explicitly refers to this function (by name or behavior), and this function would need to be modified to implement the change.
- Do NOT check whether the current implementation already matches the changed specification. Answer based solely on whether the spec change refers to this function.
- Answer "No" only if the spec change clearly refers to a different function or this function is unrelated to the change.

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "Yes" or "No"

Do NOT include any explanations, reasoning, or additional text.'''
