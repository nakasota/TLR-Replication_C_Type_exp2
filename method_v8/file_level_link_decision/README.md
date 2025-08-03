# Method v8: Enhanced Processing Flow with File-Level Link Decision

Method v8 introduces an improved processing flow that includes a new file-level link decision step between directory/file level and function level processing.

## New Processing Flow

The processing flow has been enhanced as follows:

1. **directory_and_file_localization** (existing) → 
2. **file_level_link_decision** (NEW) → 
3. **function_level_localization** (existing) → 
4. **function_level_link_decision** (existing, previously called link_decision)

## Components

### 1. directory_and_file_localization/
**Input**: Proposal files  
**Output**: List of potentially relevant files based on directory and file names  
**Purpose**: Initial filtering of files from the entire repository

### 2. file_level_link_decision/ (NEW)
**Input**: Files identified by directory_and_file_localization  
**Output**: Filtered list of files with skeleton-based relevance analysis  
**Purpose**: Analyze file content using skeleton view to determine relevance to the proposal

**Key Features**:
- Uses skeleton view instead of full file content for efficiency
- Extracts function signatures, type definitions, and interfaces
- Makes relevance decisions at the file level before detailed function analysis

**Files**:
- `main.py`: Main processing script
- `evaluate.py`: Evaluation against ground truth
- `prompt/file_level_analyzer.py`: Skeleton extraction and file analysis
- `prompt/file_level_prompt.py`: Prompt generation for LLM analysis

### 3. function_level_localization/
**Input**: Relevant files from file_level_link_decision  
**Output**: List of relevant functions within the relevant files  
**Purpose**: Identify specific functions that are relevant to the proposal

**Changes from v6**:
- Now takes input from file_level_link_decision instead of directory_and_file_localization
- Updated to handle the new input format with file relevance information

### 4. function_level_link_decision/ (renamed from link_decision)
**Input**: Functions identified by function_level_localization  
**Output**: Final relevance decisions for each function (Yes/No)  
**Purpose**: Make final link decisions for individual functions

**Changes from v6**:
- Updated to work with the new processing flow
- Now called "function_level_link_decision" conceptually

## Improvements

### 1. Better Precision
- File-level skeleton analysis filters out irrelevant files before expensive function-level processing
- Reduces false positives by analyzing file structure before detailed content analysis

### 2. Efficiency
- Skeleton view processing is faster than full file content analysis
- Early filtering reduces the number of functions that need individual analysis

### 3. Enhanced Context
- Skeleton view provides better structural understanding of files
- Type definitions and interfaces give better context for relevance decisions

## Usage

### Running the Complete Pipeline

1. **Step 1: Directory and File Localization**
   ```bash
   cd directory_and_file_localization
   python main.py
   ```

2. **Step 2: File Level Link Decision (NEW)**
   ```bash
   cd file_level_link_decision
   python main.py
   # Select the directory_and_file_localization output when prompted
   ```

3. **Step 3: Function Level Localization**
   ```bash
   cd function_level_localization
   python main.py
   # Select the file_level_link_decision output when prompted
   ```

4. **Step 4: Function Level Link Decision**
   ```bash
   cd function_level_link_decision
   python main.py
   # Select the function_level_localization output when prompted
   ```

### Evaluation

Each component includes evaluation scripts:

```bash
# Evaluate file-level link decisions
cd file_level_link_decision
python evaluate.py

# Evaluate function-level localization results
cd function_level_localization
python evaluate.py

# Evaluate final link decisions
cd function_level_link_decision
python evaluate.py
```

## Expected Improvements

1. **Higher Precision**: File-level skeleton analysis should reduce false positives
2. **Better Recall**: Structured analysis of file contents should improve function identification
3. **Efficiency**: Early filtering reduces computational overhead
4. **Interpretability**: Skeleton view provides clearer reasoning for decisions

## Data Flow

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
Final Results
```

## Configuration

- **API Settings**: Configure DeepSeek API key in `.env` file
- **Batch Sizes**: Adjustable in each component's main.py
- **Tree-sitter**: Requires Go language grammar for skeleton extraction

## Dependencies

- tree-sitter (for skeleton extraction)
- requests (for API calls)
- python-dotenv (for environment variables)
- Standard Python libraries (json, pathlib, etc.)
