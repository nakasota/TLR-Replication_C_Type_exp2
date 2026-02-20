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


def generate_granularity_decision_diff_prompt(base_spec_text: str, changed_spec_text: str) -> str:
    """
    Generate prompt for granularity decision in diff (change-driven) mode.
    Given base and changed spec sections, determine the granularity level that is
    **related to the changed area** (directory / file / function).
    C language specific: .c = implementation, .h = declarations/structs.
    """
    return f'''You are analyzing a specification change to determine the most appropriate granularity level for linking C source code that is **related to the changed area**.

### Base Specification (Before Change) ###
{base_spec_text}

### Changed Specification (After Change) ###
{changed_spec_text}

**OBJECTIVE**: Determine the granularity level that best corresponds to what is **related to the changed area**. When multiple levels apply, prefer the most specific (function > file > directory).

- "directory"
  - Choose when the changed area relates to directory-level scope: creating/removing/renaming/moving .c or .h files, or changing the directory/module structure.
  - Examples: adding new .c or .h files; adding a new module; splitting code into new files; moving/renaming modules.

- "file"
  - Choose when the changed area relates to file-level scope: .h files (declarations, struct definitions, macros) or adding new functions/variables/types.
  - Examples: adding function declarations in a header; changing struct member definitions; adding new functions in a .c file; changing function signatures.

- "function"
  - Choose when the changed area relates to function-level scope: changes inside the body of existing function(s) in .c files.
  - Examples: editing assignment statements; changing control flow; changing return values or local logic; modifying default values or constants inside a function body.

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "directory", "file", or "function"

Do NOT include any explanations, reasoning, or additional text.'''
