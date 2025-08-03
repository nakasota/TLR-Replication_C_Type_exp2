# Method v8: Enhanced Processing Flow with File-Level Link Decision

## Overview

Method v8 introduces an improved 4-stage processing flow with a new file-level link decision component:

1. **directory_and_file_localization** → Initial file identification
2. **file_level_link_decision** (NEW) → Skeleton-based file relevance analysis  
3. **function_level_localization** → Function identification within relevant files
4. **function_level_link_decision** → Final function relevance decisions

## Key Improvements

- **Skeleton View Analysis**: Uses Go code skeleton (function signatures, types, interfaces) instead of full file content
- **Enhanced Precision**: File-level filtering reduces false positives before expensive function analysis
- **Better Efficiency**: Early filtering reduces computational overhead
- **Improved Context**: Structural analysis provides better relevance decisions

## Processing Flow

```
Proposals
    ↓
directory_and_file_localization (finds potential files)
    ↓ found_files: [file_paths]
file_level_link_decision (skeleton analysis)
    ↓ relevant_files: [{file_path, reasoning, confidence}]
function_level_localization (identifies functions)
    ↓ {proposal: {file: [functions]}}
function_level_link_decision (final Yes/No)
    ↓ {proposal: {file: {function: Yes/No}}}
```

## Usage

Run the pipeline in order:
1. `cd directory_and_file_localization && python main.py`
2. `cd file_level_link_decision && python main.py` (select directory_and_file_localization output)
3. `cd function_level_localization && python main.py` (select file_level_link_decision output)
4. `cd function_level_link_decision && python main.py` (select function_level_localization output)

## Previous Results (Method v6 baseline)

### separete 6 files (2000 lines)
20250712_080410 -> 20250712_104332 -> 20250716_160634

| Level           | Number of Processed Proposals | Number of Proposals with at least one correct link (precision > 0) | Macro Precision | Macro Recall | Macro F1 |
| --------------- | ----------------------------- | ------------------------------------------------------------------ | --------------- | ------------ | -------- |
| Directory-Level | 231                           | 220 (95.2%)                                                                |  0.762          | 0.703        | 0.681    |
| File-Level      | 231                           |  211 (91.3%)                                                             | 0.510           | 0.525        | 0.465    |
| Function-Level  | 231                           |  199 (86.1%)                                                           | 0.269           | 0.410        | 0.284    |
| Phase 2  | 231                           | 184 (80.0%%)                                                                | 0.534           | 0.328        | 0.354    |

20250706_045628

| Level           | Number of Processed Proposals | Number of Proposals with at least one correct link (precision > 0) | Macro Precision | Macro Recall | Macro F1 |
| --------------- | ----------------------------- | ------------------------------------------------------------------ | --------------- | ------------ | -------- |
| Directory-Level | 231                           | 219 (94.8%)                                                               | 0.748           | 0.703        | 0.673    |
| File-Level      | 231                           | 207 (89.6%)                                                               | 0.493           | 0.513        | 0.452    |
| Function-Level | 231 | 196 (84.8%) | 0.262 | 0.396 | 0.272 |



### separete 12 files
20250712_080432 -> 20250712_163023 -> 20250716_160625

| Level           | Number of Processed Proposals | Number of Proposals with at least one correct link (precision > 0) | Macro Precision | Macro Recall | Macro F1 |
| --------------- | ----------------------------- | ------------------------------------------------------------------ | --------------- | ------------ | -------- |
| Localization(Directory) | 231                           | 221 (95.7%)                                                                | 0.713           | 0.714        | 0.657    |
| Localization(File)      | 231                           | 209 (90.5%)                                                                | 0.480           | 0.537        | 0.448    |
| Localization(Function)  | 231                           | 196 (84.8%)                                                                | 0.248           | 0.412        | 0.264    |
| Link Decision  | 231                           | 184 (80.0%%)                                                                | 0.506           | 0.329        | 0.346    |


20250706_115037

| Level           | Number of Processed Proposals | Number of Proposals with at least one correct link (precision > 0) | Macro Precision | Macro Recall | Macro F1 |
| --------------- | ----------------------------- | ------------------------------------------------------------------ | --------------- | ------------ | -------- |
| Directory-Level | 231                           |  221 (95.7%)                                                              |  0.707          | 0.720        | 0.656    |
| File-Level      | 231                           | 209 (90.5%)                                                               | 0.471           | 0.536        | 0.445    |
| Function-Level | 231 | 198 (85.7%) | 0.250 | 0.407 | 0.263 |
