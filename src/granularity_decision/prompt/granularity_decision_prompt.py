def generate_granularity_decision_prompt(doc_text: str) -> str:
    """
    Generate prompt for granularity decision: design document → linking granularity (directory / file / function).
    Definitions are scope-based (what level of code the document describes), not change-based.
    """
    return f'''You are analyzing a design document to determine the most appropriate granularity level for **linking** it to relevant C source code. The document describes some API, module, or feature; choose the level that best matches the document's **scope** (what part of the codebase it refers to), not any hypothetical changes.

### Design Document ###
{doc_text}

**OBJECTIVE**: Choose the granularity at which this document should be linked to the codebase: the level that best corresponds to what the document describes (directory, file(s), or specific function(s)).

**GRANULARITY OPTIONS (scope-based):**
- "directory"
  - The document's scope is directory-level: it describes a subsystem, a directory layout, or a set of files/directories as a whole. Linking should target directory (or multiple directories).
  - Examples: overall project structure; a component spanning several files/directories; directory-level conventions or layout.

- "file"
  - The document's scope is file-level: it describes the contents of one or more specific files (e.g. an API in a header, a module in a .c file), without focusing on individual functions. Linking should target file(s).
  - Examples: API of a header file; behavior of a source file; a small set of related files (e.g. foo.c / foo.h).

- "function"
  - The document's scope is function-level: it describes one or a few specific functions (signatures, behavior, usage). Linking should target those functions.
  - Examples: a single function's contract; a small API surface (e.g. two or three functions); function-level documentation.

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "directory", "file", or "function"

Do NOT include any explanations, reasoning, or additional text.'''
