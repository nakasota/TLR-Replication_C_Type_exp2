def generate_granularity_decision_prompt(proposal_text):
    """
    Generate prompt for granularity decision analysis
    Determines the appropriate granularity level for linking source code to Go proposals
    """
    return f'''You are analyzing a Go proposal to determine the most appropriate granularity level for linking relevant source code.

### Go Proposal ###
{proposal_text}

**OBJECTIVE**: Determine the most appropriate granularity level for linking source code that would be relevant to implementing or being affected by this Go proposal.

**GRANULARITY OPTIONS:**
- "directory": Choose this if the proposal affects entire packages, modules, or architectural components that span multiple files
- "file": Choose this if the proposal affects specific files or small groups of related files, but not entire directories
- "function": Choose this if the proposal affects specific functions, methods, or very localized code changes

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "directory", "file", or "function"

Do NOT include any explanations, reasoning, or additional text.'''
