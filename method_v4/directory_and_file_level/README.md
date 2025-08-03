# Method V3: Combined Directory and File Level Localization

## Overview

Method V3 combines directory and file level localization into a single unified approach. Unlike method_v2 which processes directory and file levels separately, this method processes multiple repository structure files independently and aggregates their results.

## Key Features

1. **Combined Approach**: Directly identifies relevant files instead of first finding directories then files
2. **Multiple Structure Files**: Uses separate repository structure files (`simplified_repo_structure_separate*.txt`) for comprehensive coverage
3. **Aggregated Results**: Combines results from all structure files to get the union of all found files
4. **File-level Evaluation**: Evaluates performance based on files rather than directories

## Architecture

### Files Structure
```
method_v3/
├── directory_and_file_level/
│   ├── main.py                     # Main execution script
│   ├── evaluate.py                 # Evaluation script
│   ├── output/                     # Generated results
│   └── prompt/
│       ├── directory_and_file_level_localization.py  # Prompt generator
│       └── repository_structure_1000/
│           ├── simplified_repo_structure_separate1.txt
│           ├── simplified_repo_structure_separate2.txt
│           ├── simplified_repo_structure_separate3.txt
│           ├── simplified_repo_structure_separate4.txt
│           └── simplified_repo_structure_separate5.txt
└── function_level/                 # Separate function-level localization
```

## How It Works

### 1. Prompt Generation (`directory_and_file_level_localization.py`)
- Takes proposal file and structure file as arguments
- Generates prompts that ask LLM to identify relevant files directly
- Supports processing different structure files independently
- Outputs structured JSON with `found_files` list

### 2. Main Processing (`main.py`)
- Processes all proposals against all structure files
- For each proposal:
  - Iterates through all 5 separate structure files
  - Generates prompts using each structure file
  - Calls LLM API for each structure file
  - Aggregates all found files into a single unified set
- Saves results in JSON format with aggregated file lists

### 3. Evaluation (`evaluate.py`)
- Loads LLM outputs and ground truth data
- Computes precision, recall, and F1 scores at file level
- Generates comprehensive evaluation reports
- Creates markdown summaries with detailed breakdowns

## Usage

### Running the Main Process
```bash
cd method_v3/directory_and_file_level
python main.py
```

### Running Evaluation
```bash
cd method_v3/directory_and_file_level
python evaluate.py
```

### Testing Prompt Generation
```bash
cd method_v3/directory_and_file_level/prompt
python directory_and_file_level_localization.py \
    ../../../data/preprocess/accepted_proposals/evaluable_proposals/19367.md \
    repository_structure_1000/simplified_repo_structure_separate1.txt
```

## Improvements Over Method V2

1. **Unified Process**: Eliminates the two-step directory → file approach
2. **Better Coverage**: Uses multiple structure files to ensure comprehensive analysis
3. **Aggregated Results**: Combines insights from different structure perspectives
4. **Direct File Targeting**: More efficient by directly identifying relevant files
5. **Simplified Evaluation**: Single evaluation process for file-level results

## Output Format

### LLM Outputs (`llm_outputs.json`)
```json
{
  "proposal_name.md": {
    "found_files": [
      "src/runtime/unsafe.go",
      "src/unsafe/unsafe.go",
      "src/reflect/value.go"
    ]
  }
}
```

### Evaluation Results
- `evaluation_results.json`: Detailed per-proposal metrics
- `evaluation_summary.md`: Human-readable summary with visualizations
- `summary.json`: Macro-level performance metrics 