# File Level Link Decision (C / design document)

## Overview

This module implements file-level link decision for the C repository and design documents pipeline. It takes the files identified by `directory_and_file_level_localization` and decides whether each file is relevant to the given design document (Yes/No).

## Purpose

1. Takes the files identified by `directory_and_file_level_localization`
2. Builds a skeleton view for each C file (includes, macros, types, function signatures) from `c_repo_structure.json`
3. Calls the LLM to get a Yes/No decision per file

## Processing Flow

```
Input: Files from directory_and_file_level_localization (design doc → found_files)
   ↓
Extract skeleton view for each file (tree-sitter or regex)
   ↓
Generate file-level link decision prompt
   ↓
Call LLM API to get Yes/No decision for each file
   ↓
Output: llm_outputs.json with decisions per document and file
```

## Input/Output

### Input
- **Directory/File results**: `src/directory_and_file_level_localization/output/<timestamp>/llm_outputs.json` (or set `SELECTED_DIRECTORY_FILE_OUTPUT` to pick one)
- **Design documents**: `data/docs/`
- **Repo structure**: `data/preprocess/c_repo_structure.json`

### Output
- **llm_outputs.json**: File-level decisions per document
  ```json
  {
    "overview.md": {
      "src/math_utils.c": {"decision": "Yes"},
      "src/other.c": {"decision": "No"}
    }
  }
  ```
- **processing_summary.json**: Statistics and metadata

## Key Features

### 1. Standalone run
- Run from `src/file_level_link_decision`; no environment variables required.
- Uses the latest `directory_and_file_level_localization` output if `SELECTED_DIRECTORY_FILE_OUTPUT` is not set.
- Processes all documents that have `found_files` (no granularity filter unless `GRANULARITY_RESULTS` is set).

### 2. Skeleton-based analysis
- Extracts C code skeleton from `c_repo_structure.json` content (tree-sitter or regex fallback).
- Includes includes, macros, types, and function signatures.

## Testing (skeleton view)

The primary test is that **skeleton view generation** works for C files. Run:

```bash
cd src/file_level_link_decision
python test_skeleton_view.py
```

Requires the project venv (or `pip install tree-sitter`). Tests verify:

- `_extract_includes` / `_extract_macros` extract expected lines from C source
- `_extract_file_skeleton` returns a non-empty skeleton (tree-sitter or regex fallback)
- `analyze_file_with_skeleton(file_path)` returns a dict with non-empty `skeleton_view` when the path exists in the repo structure (mocked or real)

Optional: run against real `data/preprocess/c_repo_structure.json` (from `src/file_level_link_decision`):

```bash
python -c "from test_skeleton_view import test_with_real_repo_structure; test_with_real_repo_structure()"
```

Show generated skeleton views:

```bash
python test_skeleton_view.py --show-skeleton
```

## Files

### main.py
- Loads directory/file localization results (latest or `SELECTED_DIRECTORY_FILE_OUTPUT`).
- Optionally filters by `GRANULARITY_RESULTS` ("file" only) when set.
- For each document and each found file, builds skeleton, calls LLM, and writes decisions.

### prompt/file_level_analyzer.py
- Loads `c_repo_structure.json`.
- Extracts skeleton view from file content (tree-sitter or regex fallback).

### prompt/file_level_prompt.py
- Builds the LLM prompt (design document + file path + skeleton view, Yes/No).

## Usage

### Standalone (no env vars)
```bash
cd src/file_level_link_decision
python main.py
```

### With environment variables (e.g. coordinated workflow)
- `GRANULARITY_RESULTS`: optional; JSON of document → granularity; when set, only "file" granularity documents are processed.
- `SELECTED_DIRECTORY_FILE_OUTPUT`: optional; directory name under `directory_and_file_level_localization/output/` (default: latest).

## Error Handling

- Missing or empty `directory_and_file_level_localization` output → clear error and path shown; run from `src/file_level_link_decision`.
- Missing files in `c_repo_structure.json`, empty skeleton, API errors → logged; per-file errors recorded in output.

## Output Structure

### Success
```json
{
  "overview.md": {
    "src/math_utils.c": {"decision": "Yes"},
    "src/other.c": {"decision": "No"}
  }
}
```

### Error for a file
```json
{
  "overview.md": {
    "path/to/file.c": {"decision": "Error", "error": "skeleton_analysis_failed"}
  }
}
```
