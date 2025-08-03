# Content-Validated Ground Truth Creation Process

This document describes the comprehensive workflow for creating high-quality ground truth data with content validation for Go language proposal research.

## Overview

The content-validated ground truth creation process consists of two main stages:
1. **Function Analysis with State Filtering** (`batch_find_relative_func_with_state.py`)
2. **Ground Truth Creation with Content Validation** (`create_ground_truth_final_with_state.py`)

## Prerequisites

### Required Input Data
- **Proposal Files**: `../data/preprocess/accepted_proposals/*.md`
- **Repository Structure**: `../data/ground_truth/go_repo_structure.json`
- **GitHub API Access**: For fetching current repository content

### Required Dependencies
- `find_relative_func.py`: Core CL analysis functionality
- `content_validator.py`: Content validation logic
- `repo_loader.py`: Repository file content retrieval
- `tqdm`: Progress display (optional)

## Stage 1: Function Analysis with State Filtering

### Purpose
Extract and analyze functions from MERGED Change Lists (CLs) with detailed change information.

### Process Flow

#### 1.1 Proposal File Processing
```python
# Process all proposal markdown files
md_files = sorted(proposals_dir.glob("*.md"))
# Example: 19367.md, 28308.md, 46121.md, ...
```

#### 1.2 CL State Filtering
- **Input**: All CLs from proposal files
- **Filter**: Only `MERGED` status CLs are retained
- **Rationale**: Only merged changes represent actual implementations

```python
if cl_status == 'MERGED':
    filtered_cl_analyses.append(enhanced_cl_analysis)
```

#### 1.3 AST-based Function Detection
- Parse Go source code using AST analysis
- Extract function information:
  - Function name
  - Start/end line numbers
  - File path

#### 1.4 Change Content Analysis
For each detected function:
- Extract lines changed within the function scope
- Identify added lines from the CL
- Store detailed change information

```python
func_changes = [
    line for line in changed_lines
    if func_start <= line.get('new_line', 0) <= func_end
]

added_lines = [
    line.get('content', '') 
    for line in func_changes 
    if line.get('type') == 'added'
]
```

### Output
**File**: `accepted_proposals_func_analysis_merged_validated.json`

**Structure**:
```json
{
  "results": [
    {
      "proposal_id": "19367",
      "proposal_file": "../data/preprocess/accepted_proposals/19367.md",
      "cl_analyses": [
        {
          "cl_number": "201839",
          "status": "MERGED",
          "files": [
            {
              "file_path": "src/runtime/checkptr.go",
              "ast_analysis": {
                "detected_functions": [
                  {
                    "function_name": "checkptrAlignment",
                    "start_line": 15,
                    "end_line": 26,
                    "function_changes": {
                      "changes_in_function": 3,
                      "added_lines": ["func checkptrAlignment(p unsafe.Pointer, elem *_type) {", "..."]
                    }
                  }
                ]
              }
            }
          ]
        }
      ]
    }
  ],
  "statistics": {
    "merged_cls_count": 750,
    "content_analysis_stats": {...}
  }
}
```

## Stage 2: Ground Truth Creation with Content Validation

### Purpose
Create high-quality ground truth by validating that CL changes actually exist in the current repository.

### Process Flow

#### 2.1 Repository Structure Matching
- Load current Go repository structure
- Check if files and functions exist in the current repository
- Only process functions that exist in both CL and current repository

```python
if file_path in repo_files:
    repo_funcs = repo_file_functions.get(file_path, set())
    if func_name and func_name in repo_funcs:
        # Proceed with validation
```

#### 2.2 Content Validation Process

##### 2.2.1 Content Retrieval
- Fetch current file content from GitHub repository
- Extract the specific function content
- Handle vendor files and special cases

##### 2.2.2 Change Validation
- Compare CL added lines with current function content
- Use similarity matching for line comparison
- Calculate content match score

```python
content_validation = content_validator.validate_function_content(
    func_name=func_name,
    file_path=file_path,
    cl_added_lines=cl_added_lines,
    func_start_line=func.get('start_line', 1),
    func_end_line=func.get('end_line', 1)
)
```

##### 2.2.3 Ground Truth Qualification
A function qualifies as ground truth if:
- ✅ CL status is `MERGED`
- ✅ Function name exists in current repository
- ✅ File path exists in current repository  
- ✅ At least one added line from CL exists
- ✅ At least one added line matches current function content

```python
is_qualified_ground_truth = content_validation.get('is_ground_truth', False)
```

#### 2.3 Quality Filtering

##### 2.3.1 Strict Requirements
- **No added lines**: Functions with zero added lines are excluded
- **Content mismatch**: Functions where no added lines match current content are excluded
- **File access errors**: Functions in inaccessible files are excluded

##### 2.3.2 Progress Tracking
- Real-time progress display with tqdm
- Error handling with continuation on individual failures
- Detailed statistics collection

### Output
**File**: `accepted_proposals_ground_truth_content_validated.json`

**Structure**:
```json
{
  "ground_truth": [
    {
      "proposal_id": "19367",
      "proposal_file": "../data/preprocess/accepted_proposals/19367.md",
      "merged_cl_count": 1,
      "files": ["src/runtime/checkptr.go"],
      "detected_functions": [
        {
          "function_name": "checkptrAlignment",
          "file_path": "src/runtime/checkptr.go",
          "start_line": 15,
          "end_line": 26,
          "cl_number": "201839",
          "cl_status": "MERGED",
          "content_validation": {
            "validation_status": "content_matches",
            "content_match_score": 0.6,
            "is_ground_truth": true,
            "added_lines_found": 3,
            "added_lines_total": 5,
            "reason": "3 out of 5 added lines found in current function"
          }
        }
      ]
    }
  ],
  "statistics": {
    "total_proposals": 210,
    "total_functions": 4201,
    "content_validation_stats": {...}
  }
}
```

## Quality Metrics

### Validation Statistics
- **Content Match Score**: Ratio of matched added lines to total added lines
- **Validation Status**: 
  - `content_matches`: Added lines found in current repository
  - `content_differs`: Added lines not found in current repository
  - `file_not_found`: File not accessible in current repository
  - `function_not_found`: Function not found in current file

### Filtering Results
- **Input**: 262 proposals, 750 MERGED CLs
- **After MERGED filtering**: ~210 proposals
- **After content validation**: ~210 proposals with high-quality functions
- **Exclusions**: 
  - Functions with no added lines
  - Functions with no matching content
  - Inaccessible vendor files (if vendor exclusion enabled)

## Usage Instructions

### Step 1: Run Function Analysis
```bash
cd create_ground_truth
python batch_find_relative_func_with_state.py
```

### Step 2: Create Ground Truth
```bash
python create_ground_truth_final_with_state.py
```

### Step 3: Validate Results (Optional)
```bash
python detailed_ground_truth_comparison.py
```

## Benefits of Content Validation

### 1. **High Precision**
- Only includes functions that actually exist in current repository
- Validates that proposed changes were actually implemented

### 2. **Research Reliability**
- Eliminates false positives from proposal analysis
- Ensures ground truth represents real implementations

### 3. **Quality Assurance**
- Content match scores provide confidence levels
- Detailed validation status for debugging and analysis

### 4. **Comprehensive Coverage**
- Handles edge cases (vendor files, missing functions, etc.)
- Robust error handling ensures complete processing

## Troubleshooting

### Common Issues
1. **GitHub API Rate Limits**: Implement retry logic and caching
2. **File Access Errors**: Check repository structure and file paths
3. **Memory Usage**: Process large proposals in batches if needed

### Validation Failures
- **file_not_found**: File may have been moved or deleted
- **function_not_found**: Function may have been renamed or removed
- **content_differs**: Implementation may have evolved since CL

## Configuration Options

### Content Validator Settings
- **Similarity Threshold**: Adjust line matching sensitivity (default: 0.8)
- **Vendor File Handling**: Include/exclude vendor directory files
- **Error Tolerance**: Continue processing on individual failures

### Repository Loader Settings
- **GitHub API vs Raw Content**: Fallback mechanisms for content retrieval
- **Caching**: Enable local caching for repeated file access
- **Timeout Settings**: Configure request timeouts for reliability

This comprehensive workflow ensures the creation of high-quality, validated ground truth data suitable for reliable research on Go language proposals.
