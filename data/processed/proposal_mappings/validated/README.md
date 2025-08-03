# CL-Validated Ground Truth Data for Accepted Proposals

This directory contains **high-quality ground truth data** for evaluating proposal-to-code mapping methods. All data is derived from **accepted Go proposals** and validated using **CL (Change List) diff analysis** from Gerrit.

## 🎯 **MAIN EVALUATION FILES (USE THESE!)**

### **File-Level Ground Truth**
- **`accepted_proposals_FILE_LEVEL_GROUND_TRUTH.json`** ⭐
  - **Purpose**: Primary ground truth for file-level evaluation
  - **Format**: `[[proposal_id, file_path], ...]`
  - **Coverage**: 3,280 high-confidence file mappings
  - **Example**: `[51430, "src/internal/coverage/cformat/format.go"]`

### **Function-Level Ground Truth**  
- **`accepted_proposals_FUNCTION_LEVEL_GROUND_TRUTH.json`** ⭐
  - **Purpose**: Primary ground truth for function-level evaluation
  - **Format**: `[[proposal_id, file_path, function_name], ...]`
  - **Coverage**: 13,247 high-confidence function mappings
  - **Example**: `[45428, "src/crypto/tls/handshake_test.go", "checkOpenSSLVersion"]`

## 📊 **DETAILED VALIDATION DATA (FOR RESEARCH)**

### **Complete Validation Results**
- **`accepted_proposals_file_level_detailed_validation.json`**
  - Complete file-level validation with confidence scores for all proposals
  - Includes high, medium, and low confidence mappings
  - Size: ~9MB with full validation metadata

- **`accepted_proposals_function_level_detailed_validation.json`**
  - Complete function-level validation with confidence scores
  - Includes all function-level CL analysis results
  - Size: ~37MB with comprehensive validation data

### **Supporting Files**
- **`accepted_proposals_file_level_mappings.csv`**
  - CSV format of file-level mappings for easy analysis
  - Includes confidence scores and validation metadata

- **`accepted_proposals_validation_summary.json`**
  - Summary statistics of the validation process
  - Overview of confidence distribution and coverage

## 🔬 **INTERMEDIATE PROCESSING FILES (ADVANCED USERS)**

- **`accepted_proposals_function_level_intermediate.json`**
  - Intermediate function-level processing results
  - Used during validation pipeline development

- **`accepted_proposals_function_level_from_repo.json`**
  - Function mappings derived from repository structure analysis
  - Alternative function-level dataset (lower quality than CL-validated)

## 🎓 **VALIDATION METHODOLOGY**

All ground truth data uses **identical validation methodology**:

1. **Raw Extraction**: Mine proposal text for CL (Change List) references
2. **Gerrit API**: Fetch actual implementation diffs from Go's code review system
3. **Diff Analysis**: Compare CL changes against current Go source code
4. **Confidence Scoring**: Calculate validation confidence per mapping
5. **High-Confidence Filtering**: Keep only ≥80% confidence mappings

## 📈 **QUALITY METRICS**

| Level | Ground Truth Mappings | Validation Method | Quality |
|-------|----------------------|------------------|---------|
| **File** | 3,280 | CL diff validation | ⭐⭐⭐⭐⭐ |
| **Function** | 13,247 | CL diff validation | ⭐⭐⭐⭐⭐ |

## 🚀 **USAGE IN EVALUATION**

```python
# File-level evaluation
import json
with open('accepted_proposals_FILE_LEVEL_GROUND_TRUTH.json', 'r') as f:
    file_ground_truth = json.load(f)
# Format: [[proposal_id, file_path], ...]

# Function-level evaluation  
with open('accepted_proposals_FUNCTION_LEVEL_GROUND_TRUTH.json', 'r') as f:
    function_ground_truth = json.load(f)
# Format: [[proposal_id, file_path, function_name], ...]
```

## ⚠️ **IMPORTANT NOTES**

- **Only covers ACCEPTED proposals** - declined proposals don't have implementation CLs
- **High confidence only** - these are the most reliable mappings (≥80% confidence)
- **Current Go source** - validated against the current state of the Go repository
- **CL-based validation** - derived from actual implementation changes, not speculation

## 📝 **CITATION**

If you use this ground truth data in research, please note the validation methodology:
*"Ground truth derived from accepted Go proposals using CL diff validation against implementation commits in the official Go repository."* 