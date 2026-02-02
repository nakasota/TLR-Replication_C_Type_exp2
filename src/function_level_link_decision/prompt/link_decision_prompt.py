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
