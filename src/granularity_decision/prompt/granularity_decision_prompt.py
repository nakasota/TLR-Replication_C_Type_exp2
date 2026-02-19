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
    Given base and changed spec sections, determine the granularity level at which
    the code change occurred (directory / file / function).
    """
    return f'''You are analyzing a specification change to determine the most appropriate granularity level for linking the source code that would be modified to implement this change.

### Base Specification (Before Change) ###
{base_spec_text}

### Changed Specification (After Change) ###
{changed_spec_text}

**OBJECTIVE**: Determine the most appropriate granularity level for linking source code that would be relevant to implementing (not merely being affected by) this specification change.

- "directory"
  - Definition: Choose ONLY when the spec change explicitly mandates creating/removing/renaming/moving files or modules, or otherwise changing the directory/module structure.
  - Examples: adding new source files or headers; adding a new module; splitting code into new files; moving/renaming modules or files; adding platform-specific new files (when explicitly required).

- "file"
  - Definition: Choose when ALL required edits are confined to EXISTING files only (even if the edits span multiple files or modules), and the spec change does NOT explicitly require new/removed/moved files or modules.
  - Examples: adding functions/variables/types in existing files; exposing new APIs in an existing module; changing interfaces and updating callers in existing files; adding declarations in existing files.

- "function"
  - Definition: Choose only when the change is limited to modifying the internal logic of EXISTING functions or their documentation, with no new top-level declarations and no other changes required outside the functions.
  - Examples: editing statements; changing control flow; tweaking parameters/returns of existing functions without touching other parts; deprecating functions by adding deprecation comments; modifying inline documentation within function bodies.

**OUTPUT FORMAT:**
Respond with EXACTLY one word: "directory", "file", or "function"

Do NOT include any explanations, reasoning, or additional text.'''
