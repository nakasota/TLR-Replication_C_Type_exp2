# Graph Creation Scripts

This directory contains scripts for creating visualizations of Go proposal data.

## Files

### `make_treemap_chart.py`
Creates a treemap visualization showing the distribution of Go proposals by directory.

**Features:**
- True treemap layout using squarify algorithm
- Directory boundaries marked with black borders
- Accepted proposals shown in red, declined proposals in blue
- Numbers displayed within each section
- Realistic data with varying acceptance rates across directories

**Usage:**
```bash
python make_treemap_chart.py
```

**Output:** `treemap_chart.png`

### `make_sunburst_chart.py`
Creates a sunburst chart visualization showing the hierarchical distribution of Go proposals.

**Features:**
- Inner and outer rings showing category hierarchy
- Color-coded categories with spacing for clear separation
- Accepted/declined breakdown within each category
- Category-specific color schemes

**Usage:**
```bash
python make_sunburst_chart.py
```

**Output:** `sunburst_chart.png`

## Dependencies

Both scripts require:
- matplotlib
- numpy
- squarify (for treemap)

Install with:
```bash
pip install matplotlib numpy squarify
```

## Data Structure

Both scripts use similar data structures representing Go proposal statistics:
- Directory/category names as keys
- `accepted` and `declined` counts as values
- Realistic distributions showing varying acceptance rates

## Generated Charts

The generated PNG files are saved in the same directory and provide high-resolution (300 DPI) visualizations suitable for presentations and reports.
