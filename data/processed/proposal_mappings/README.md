# Proposal-to-Code Mappings Pipeline

This directory contains the complete pipeline for creating proposal-to-code mappings, from raw extraction to validated reference data.

## Directory Structure

```
proposal_mappings/
├── raw/                              # Raw mappings from CL extraction (7,767 mappings)
│   ├── proposal_file_mappings.csv
│   ├── proposal_file_mappings.json
│   └── detailed_proposal_file_mappings.json
├── validated/                        # CL-validated high-confidence mappings (6 mappings)
│   ├── cl_validation_summary.json
│   ├── cl_high_confidence_mappings.json
│   ├── cl_validated_mappings.csv
│   └── cl_validated_dataset.json
├── intermediate_validation_results.json  # Step 2: CL diff validation (intermediate)
└── README.md                        # This file
```

## Data Pipeline

1. **Raw Extraction** (`raw/`):
   - **Source**: Accepted proposal files
   - **Process**: Text mining for CL links + Gerrit API calls
   - **Output**: 7,767 unvalidated proposal-to-file mappings
   - **Purpose**: Complete extraction results for research/debugging

2. **CL Diff Validation** (`intermediate_validation_results.json`):
   - **Source**: Raw mappings  
   - **Process**: Compare each CL's diffs with current source code
   - **Output**: Detailed validation results with confidence scores for each file
   - **Purpose**: Intermediate processing step with full validation details

3. **High-Confidence Filtering** (`validated/`):
   - **Source**: Intermediate validation results
   - **Filter**: Keep only ≥80% confidence mappings
   - **Output**: 6 high-confidence mappings from 2 proposals
   - **Purpose**: Gold standard reference dataset for evaluation

## Usage

- **For evaluation**: Use `validated/cl_high_confidence_mappings.json`
- **For research/debugging**: Use `raw/` files to understand extraction process
- **For validation analysis**: See intermediate results in `intermediate_validation_results.json`

## Key Files

### Raw Mappings
- `proposal_file_mappings.json`: All 7,767 extracted mappings
- `detailed_proposal_file_mappings.json`: Extended metadata for each mapping

### Validated Mappings  
- `cl_high_confidence_mappings.json`: **Primary evaluation reference** (6 mappings)
- `cl_validated_dataset.json`: Complete validation results with confidence scores 