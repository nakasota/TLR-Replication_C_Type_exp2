# Ground Truth Creation Process

This document summarizes the process and results of creating a high-quality ground truth dataset for evaluating the ability of LLMs to understand proposal changes in the Go language.

## 🎯 Purpose

- Extract function-level changes from accepted Go proposals
- Create a reliable ground truth containing only functions that exist in the current Go repository
- Establish a consistent function extraction method using tree-sitter

## 📋 Processing Flow

### 1. Initial Data Preparation
```
Accepted proposal files (337)
↓
Function analysis (find_relative_func.py + batch_find_relative_func.py)
↓
accepted_proposals_func_analysis.json (271 proposals with detected functions)
```

### 2. Current Repository Structure Analysis
```
data/repos/go/ (current Go repository)
↓
tree-sitter analysis (create_go_repo_structure.py)
↓
go_repo_structure.json (10,605 files, 85,800 functions)
```

### 3. Ground Truth Creation
```
accepted_proposals_func_analysis.json + go_repo_structure.json
↓
Cross-check with current repository (create_ground_truth_final.py)
↓
accepted_proposals_ground_truth.json (231 final ground truth proposals)
```

## 📊 Processing Statistics

### Input Data
| Stage      | File                        | Proposals | Notes                                 |
|------------|-----------------------------|-----------|---------------------------------------|
| Initial    | Accepted proposals          | 337       | All original accepted proposals       |
| After analysis | func_analysis.json       | 271       | Proposals with detected functions (80.4%) |
| Final      | ground_truth.json           | 231       | Proposals with functions in current repo (68.5%) |

### Function Detection Results
| Item              | Count    | Details                        |
|-------------------|----------|-------------------------------|
| Analyzed files    | 10,605   | .go files in Go repository    |
| Detected functions| 85,800   | Total functions detected      |
| Avg. functions/file| 8.09    | Functions per file            |

### Ground Truth Quality
| Item              | Value    | Description                   |
|-------------------|----------|-------------------------------|
| Final proposals   | 231      | Proposals matching current repo |
| Total files       | 2,131    | Files in ground truth         |
| Total functions   | 6,875    | Functions in ground truth     |
| Avg. files/proposal| 9.23    | Files per proposal            |
| Avg. functions/proposal| 29.76| Functions per proposal        |

## 🔧 Types of Functions Detected

### ✅ Detected Functions (Named)
1. **Regular function declarations**
   ```go
   func main() { ... }
   func calculate(x int) int { ... }
   ```
2. **Method declarations**
   ```go
   func (s *state) expr(n *Node) *ssa.Value { ... }
   func (t *Type) String() string { ... }
   ```
3. **Interface methods**
   ```go
   type Writer interface {
       Write([]byte) (int, error)  // ← detected
   }
   ```
4. **Function literals assigned to variables**
   ```go
   var handler = func(w http.ResponseWriter, r *http.Request) { ... }
   is_zero := func(x int) bool { return x == 0 }
   ```

### ❌ Not Detected (Anonymous)
1. **Immediately-invoked anonymous functions**
   ```go
   func() { fmt.Println("anonymous") }()
   ```
2. **Anonymous functions passed directly**
   ```go
   http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) { ... })
   ```

## 📁 File List

### Main Scripts
| File name                      | Purpose                        | Notes                |
|--------------------------------|--------------------------------|----------------------|
| `find_relative_func.py`        | Function analysis for one proposal | Uses tree-sitter  |
| `batch_find_relative_func.py`  | Batch processing for all proposals | 337 proposals     |
| `create_go_repo_structure.py`  | Repository structure analysis   | Analyzes current Go repo |
| `create_ground_truth_final.py` | Final ground truth creation     | Cross-check & validation |
| `compare_current_implementation.py` | Analysis/comparison tool   | For debugging         |

### Analysis/Validation Tools
| File name                | Purpose                        |
|-------------------------|--------------------------------|
| `analyze_func_analysis.py` | Statistics for function analysis |

### Data Files
| File name                        | Content                        | Size      |
|-----------------------------------|--------------------------------|-----------|
| `accepted_proposals_func_analysis.json` | Function analysis results | ~50MB     |
| `go_repo_structure.json`          | Repository structure           | ~153MB    |
| `accepted_proposals_ground_truth.json` | Final ground truth        | ~few MB   |

## 🎯 Ground Truth Format

```json
[
  {
    "proposal_id": "19367",
    "proposal_file": "../data/preprocess/accepted_proposals/19367.md",
    "files": [
      "src/runtime/checkptr.go",
      "src/runtime/select.go"
    ],
    "detected_functions": [
      {
        "function_name": "checkptrAlignment",
        "file_path": "src/runtime/checkptr.go",
        "start_line": 15,
        "end_line": 26
      },
      {
        "function_name": "selectgo", 
        "file_path": "src/runtime/select.go",
        "start_line": 115,
        "end_line": 491
      }
    ]
  }
]
```

## 📈 Quality Metrics

### Data Quality
- **File path match rate**: 77.3% (7,699/9,949)
- **Function name match rate**: 69.1% (6,875/9,949)
- **Unique file count**: 1,279
- **Proposal size distribution**: 1-194 files, 1-545 functions

### Most Frequent Elements
- **File**: `src/reflect/all_test.go` (15 changes)
- **Function**: `init` (80 times), `main` (52), `String` (37)

## 🔄 Processing Time
- **Function analysis**: ~10 min (337 proposals)
- **Repository analysis**: ~5 min (10,605 files)
- **Ground truth creation**: ~30 sec

## 🎉 Achievements

1. **High accuracy**: Reliable dataset containing only functions present in the current repository
2. **Consistency**: Unified function detection using tree-sitter
3. **Completeness**: Proper detection of complex function types (interface methods, function literals, etc.)
4. **Practicality**: Clean format directly usable for LLM evaluation

## 📝 Usage

```bash
# 1. Function analysis
python batch_find_relative_func.py

# 2. Repository structure creation
python create_go_repo_structure.py

# 3. Ground truth creation
python create_ground_truth_final.py
```

## 📚 Technical Details

- **tree-sitter**: Accurate AST analysis with Go parser
- **Validation**: Bidirectional matching of file paths and function names
- **Error handling**: Invalid files/functions are automatically excluded
- **Memory efficiency**: Stepwise processing of large JSON files

---

**Created**: December 2024  
**Last updated**: 231 high-quality ground truth proposals completed