def generate_link_decision_prompt(proposal_text, file_path, function_name, function_code, function_context):
    """
    Generate prompt for link decision analysis
    Using only function_code for more focused analysis
    """
    return f'''You are analyzing whether a specific Go function is directly relevant to a given Go proposal.

### Go Proposal ###
{proposal_text}

### Function Infomation ###
File: {file_path}
Function Name: {function_name}

### Function Source Code ###
{function_code}

**OBJECTIVE**: Determine if this specific function is **relevant** to implementing or being affected by the Go proposal.

**IMPORTANT GUIDELINES:**
- Only answer "Yes" if the function is **directly relevant** to the proposal's main topic
- Answer "No" for utility functions, helpers, or functions that are only tangentially related
- Answer "No" for test functions unless the proposal specifically discusses testing changes
- Answer "No" for functions in completely unrelated domains or packages

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "Yes" or "No"

Do NOT include any explanations, reasoning, or additional text.'''
