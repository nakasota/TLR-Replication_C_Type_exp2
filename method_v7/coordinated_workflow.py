#!/usr/bin/env python3
"""
Coordinated workflow for method_v7 that runs processes based on granularity decisions.

Workflow:
Phase 0: Granularity Decision - determine appropriate granularity for each proposal
Phase 1: Localization
  - Step 1: Directory and file level localization (directory granularity proposals)
  - Step 2: Directory and file level localization (file granularity proposals) 
  - Step 3: Function level localization (function granularity proposals)
Phase 2: Function Level Link Decision - for function granularity proposals only

Granularity mapping:
- "directory" -> directory_and_file_level_localization (directory output)
- "file" -> directory_and_file_level_localization (file output) 
- "function" -> directory_and_file_level_localization (file output) -> function_level_localization -> function_level_link_decision
"""

import os
import sys
import json
import subprocess
import csv
from pathlib import Path
from datetime import datetime

def print_phase_header(phase_num, phase_name, step_num=None, step_name=None):
    """Print a formatted phase/step header."""
    print("=" * 70)
    if step_num is not None:
        print(f"PHASE {phase_num} - {phase_name} | STEP {step_num}: {step_name}")
    else:
        print(f"PHASE {phase_num}: {phase_name}")
    print("=" * 70)

def print_progress(message):
    """Print a progress message with timestamp."""
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"[{timestamp}] {message}")

def get_issue_url_from_original_proposal(proposal_name):
    """Extract Issue URL from the original proposal file."""
    original_proposals_dir = Path(__file__).parent.parent / 'data' / 'preprocess' / 'declined_proposals'
    original_file = original_proposals_dir / proposal_name
    
    if not original_file.exists():
        return "N/A"
    
    try:
        with open(original_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) >= 2:
                line2 = lines[1].strip()
                if line2.startswith("Issue URL: "):
                    return line2.replace("Issue URL: ", "")
    except Exception as e:
        print_progress(f"Warning: Could not extract Issue URL from {proposal_name}: {e}")
    
    return "N/A"

def generate_code_url(granularity, found_files=None, found_directories=None, final_functions=None):
    """Generate appropriate GitHub URL based on granularity and results."""
    base_url = "https://github.com/golang/go"
    
    if granularity == "directory":
        if found_directories and len(found_directories) > 0:
            # Use the first directory
            first_dir = found_directories[0]
            return f"{base_url}/tree/master/{first_dir}"
        
    elif granularity == "file":
        if found_files and len(found_files) > 0:
            # Use the first file
            first_file = found_files[0]
            return f"{base_url}/blob/master/{first_file}"
    
    elif granularity == "function":
        if final_functions and len(final_functions) > 0:
            # Use the file containing the first function with "Yes" decision
            first_func = final_functions[0]
            file_path = first_func.get("file_path", "")
            return f"{base_url}/blob/master/{file_path}"
        elif found_files and len(found_files) > 0:
            # Fallback to first file if no functions with "Yes"
            first_file = found_files[0]
            return f"{base_url}/blob/master/{first_file}"
    
    return f"{base_url}  # Root repository"

def extract_proposal_number(proposal_name):
    """Extract proposal number from filename (e.g., '40239.md' -> '40239')."""
    return proposal_name.replace('.md', '')

def run_granularity_decision(batch_size):
    """Run the granularity decision process and return the results."""
    print_phase_header(0, "GRANULARITY DECISION")
    print_progress(f"Starting granularity decision with batch size: {batch_size}")
    
    granularity_dir = Path(__file__).parent / 'granularity_decision'
    print_progress(f"Working directory: {granularity_dir}")
    
    # Run granularity decision with specified batch size
    batch_input = f"{batch_size}\n" if batch_size != "all" else "all\n"
    print_progress("Executing granularity decision main.py...")
    
    result = subprocess.run([
        sys.executable, 'main.py'
    ], cwd=granularity_dir, capture_output=True, text=True, input=batch_input)
    
    if result.returncode != 0:
        print_progress(f"ERROR: Granularity decision failed with return code {result.returncode}")
        print(f"STDERR: {result.stderr}")
        print(f"STDOUT: {result.stdout}")
        sys.exit(1)
    
    print_progress("Granularity decision completed successfully")
    print(result.stdout)
    
    # Find the most recent output
    output_dir = granularity_dir / 'output'
    print_progress(f"Looking for output in: {output_dir}")
    
    try:
        latest_output = max(output_dir.glob('*/granularity_decisions.json'), key=lambda p: p.stat().st_mtime)
        print_progress(f"Found granularity results: {latest_output}")
    except ValueError:
        print_progress("ERROR: No granularity_decisions.json found")
        sys.exit(1)
    
    with open(latest_output, 'r') as f:
        granularity_results = json.load(f)
    
    print_progress(f"Loaded {len(granularity_results)} granularity decisions")
    return granularity_results, latest_output.parent

def run_directory_and_file_level_localization(granularity_results, repository_structure="repository_structure_2000"):
    """Run directory and file level localization with granularity awareness."""
    print_phase_header(1, "LOCALIZATION", 1, "DIRECTORY AND FILE LEVEL LOCALIZATION")
    
    # Count proposals by granularity
    directory_count = sum(1 for g in granularity_results.values() if g == "directory")
    file_count = sum(1 for g in granularity_results.values() if g == "file")
    function_count = sum(1 for g in granularity_results.values() if g == "function")
    
    print_progress("Proposal breakdown:")
    print(f"  Directory granularity: {directory_count} proposals")
    print(f"  File granularity: {file_count} proposals")
    print(f"  Function granularity: {function_count} proposals")
    print(f"  Total: {len(granularity_results)} proposals")
    
    # Create a modified version of directory_and_file_level_localization that uses granularity info
    directory_file_dir = Path(__file__).parent / 'directory_and_file_level_localization'
    print_progress(f"Working directory: {directory_file_dir}")
    
    # Pass granularity results and repository structure as environment variables
    env = os.environ.copy()
    env['GRANULARITY_RESULTS'] = json.dumps(granularity_results)
    env['REPOSITORY_STRUCTURE'] = repository_structure
    print_progress(f"Setting environment variables: GRANULARITY_RESULTS, REPOSITORY_STRUCTURE={repository_structure}")
    
    print_progress("Executing directory_and_file_level_localization main.py...")
    result = subprocess.run([
        sys.executable, 'main.py'
    ], cwd=directory_file_dir, capture_output=True, text=True, env=env)
    
    if result.returncode != 0:
        print_progress(f"ERROR: Directory and file level localization failed with return code {result.returncode}")
        print(f"STDERR: {result.stderr}")
        print(f"STDOUT: {result.stdout}")
        sys.exit(1)
    
    print_progress("Directory and file level localization completed successfully")
    print(result.stdout)
    
    # Find the most recent output
    output_dir = directory_file_dir / 'output'
    print_progress(f"Looking for output in: {output_dir}")
    
    try:
        latest_output = max(output_dir.glob('*/llm_outputs.json'), key=lambda p: p.stat().st_mtime)
        print_progress(f"Found directory/file results: {latest_output}")
    except ValueError:
        print_progress("ERROR: No llm_outputs.json found")
        sys.exit(1)
    
    return latest_output.parent

def run_function_level_localization(granularity_results, directory_file_output_dir):
    """Run function level localization only for function granularity proposals."""
    print_phase_header(1, "LOCALIZATION", 3, "FUNCTION LEVEL LOCALIZATION")
    
    # Count function granularity proposals
    function_proposals = [proposal for proposal, granularity in granularity_results.items() 
                         if granularity == "function"]
    
    if not function_proposals:
        print_progress("No proposals require function-level processing. Skipping function_level_localization.")
        return None
    
    print_progress(f"Processing {len(function_proposals)} function-granularity proposals")
    print_progress(f"Function proposals: {function_proposals}")
    
    function_dir = Path(__file__).parent / 'function_level_localization'
    print_progress(f"Working directory: {function_dir}")
    
    # Pass both granularity results and selected directory_file output
    env = os.environ.copy()
    env['GRANULARITY_RESULTS'] = json.dumps(granularity_results)
    env['SELECTED_DIRECTORY_FILE_OUTPUT'] = str(directory_file_output_dir.name)
    print_progress(f"Setting environment variables: GRANULARITY_RESULTS, SELECTED_DIRECTORY_FILE_OUTPUT={directory_file_output_dir.name}")
    
    print_progress("Executing function_level_localization main.py...")
    result = subprocess.run([
        sys.executable, 'main.py'
    ], cwd=function_dir, capture_output=True, text=True, env=env)
    
    if result.returncode != 0:
        print_progress(f"ERROR: Function level localization failed with return code {result.returncode}")
        print(f"STDERR: {result.stderr}")
        print(f"STDOUT: {result.stdout}")
        sys.exit(1)
    
    print_progress("Function level localization completed successfully")
    print(result.stdout)
    
    # Find the most recent output
    output_dir = function_dir / 'output'
    print_progress(f"Looking for output in: {output_dir}")
    
    try:
        latest_output = max(output_dir.glob('*/llm_outputs.json'), key=lambda p: p.stat().st_mtime)
        print_progress(f"Found function level localization results: {latest_output}")
    except ValueError:
        print_progress("ERROR: No function level localization llm_outputs.json found")
        sys.exit(1)
    
    return latest_output.parent

def run_function_level_link_decision(granularity_results, function_output_dir):
    """Run function level link decision only for function granularity proposals."""
    print_phase_header(2, "FUNCTION LEVEL LINK DECISION")
    
    # Count function granularity proposals
    function_proposals = [proposal for proposal, granularity in granularity_results.items() 
                         if granularity == "function"]
    
    if not function_proposals:
        print_progress("No proposals require link decision processing. Skipping function_level_link_decision.")
        return None
    
    if function_output_dir is None:
        print_progress("No function level output available. Skipping function_level_link_decision.")
        return None
    
    print_progress(f"Processing {len(function_proposals)} function-granularity proposals")
    print_progress(f"Function proposals: {function_proposals}")
    
    link_decision_dir = Path(__file__).parent / 'function_level_link_decision'
    print_progress(f"Working directory: {link_decision_dir}")
    
    # Pass both granularity results and selected function output
    env = os.environ.copy()
    env['GRANULARITY_RESULTS'] = json.dumps(granularity_results)
    env['SELECTED_FUNCTION_OUTPUT'] = str(function_output_dir.name)
    print_progress(f"Setting environment variables: GRANULARITY_RESULTS, SELECTED_FUNCTION_OUTPUT={function_output_dir.name}")
    
    print_progress("Executing function_level_link_decision main.py...")
    result = subprocess.run([
        sys.executable, 'main.py'
    ], cwd=link_decision_dir, capture_output=True, text=True, env=env)
    
    if result.returncode != 0:
        print_progress(f"ERROR: Function level link decision failed with return code {result.returncode}")
        print(f"STDERR: {result.stderr}")
        print(f"STDOUT: {result.stdout}")
        sys.exit(1)
    
    print_progress("Function level link decision completed successfully")
    print(result.stdout)
    
    # Find the most recent output
    output_dir = link_decision_dir / 'output'
    print_progress(f"Looking for output in: {output_dir}")
    
    try:
        latest_output = max(output_dir.glob('*/llm_outputs.json'), key=lambda p: p.stat().st_mtime)
        print_progress(f"Found function level link decision results: {latest_output}")
    except ValueError:
        print_progress("ERROR: No function level link decision llm_outputs.json found")
        sys.exit(1)
    
    return latest_output.parent

def create_integrated_results(granularity_results, granularity_output_dir, 
                            directory_file_output_dir, function_output_dir, 
                            link_decision_output_dir, batch_size):
    """Create integrated results combining all phases."""
    print_phase_header("FINAL", "RESULT INTEGRATION")
    print_progress("Creating integrated results from all phases...")
    
    # Create output directory with timestamp
    output_root = Path(__file__).parent / 'output'
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = output_root / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print_progress(f"Created output directory: {output_dir}")
    
    # Initialize integrated results
    integrated_results = {
        "workflow_info": {
            "timestamp": timestamp,
            "batch_size": batch_size,
            "total_proposals": len(granularity_results),
            "granularity_breakdown": {
                "directory": sum(1 for g in granularity_results.values() if g == "directory"),
                "file": sum(1 for g in granularity_results.values() if g == "file"),
                "function": sum(1 for g in granularity_results.values() if g == "function")
            }
        },
        "proposals": {}
    }
    
    # Load directory and file level results
    directory_file_results = {}
    if directory_file_output_dir:
        directory_file_json = directory_file_output_dir / 'llm_outputs.json'
        if directory_file_json.exists():
            with open(directory_file_json, 'r') as f:
                directory_file_results = json.load(f)
            print_progress(f"Loaded directory/file results: {len(directory_file_results)} proposals")
    
    # Load function level results
    function_results = {}
    if function_output_dir:
        function_json = function_output_dir / 'llm_outputs.json'
        if function_json.exists():
            with open(function_json, 'r') as f:
                function_results = json.load(f)
            print_progress(f"Loaded function results: {len(function_results)} proposals")
    
    # Load link decision results
    link_decision_results = {}
    if link_decision_output_dir:
        link_json = link_decision_output_dir / 'llm_outputs.json'
        if link_json.exists():
            with open(link_json, 'r') as f:
                link_decision_results = json.load(f)
            print_progress(f"Loaded link decision results: {len(link_decision_results)} entries")
    
    # Integrate results for each proposal
    for proposal, granularity in granularity_results.items():
        print_progress(f"Integrating results for {proposal} (granularity: {granularity})")
        
        proposal_result = {
            "proposal_file": proposal,
            "granularity": granularity,
            "phase_results": {}
        }
        
        # Phase 0: Granularity Decision
        proposal_result["phase_results"]["granularity_decision"] = {
            "decided_granularity": granularity
        }
        
        # Phase 1: Directory and File Level
        if proposal in directory_file_results:
            df_result = directory_file_results[proposal]
            proposal_result["phase_results"]["directory_file_level"] = df_result
            
            # Extract found files for summary
            if granularity == "directory":
                proposal_result["found_directories"] = df_result.get("found_directories", [])
                proposal_result["found_files"] = df_result.get("found_files", [])
            else:
                proposal_result["found_files"] = df_result.get("found_files", [])
        
        # Phase 1: Function Level (only for function granularity)
        if granularity == "function" and proposal in function_results:
            func_result = function_results[proposal]
            proposal_result["phase_results"]["function_level_localization"] = func_result
            
            # Count total functions across all files
            total_functions = []
            for file_path, functions in func_result.items():
                if file_path != "selected_file_level_output":  # Skip metadata
                    for func in functions:
                        total_functions.append({
                            "file_path": file_path,
                            "function_name": func
                        })
            proposal_result["found_functions"] = total_functions
        
        # Phase 2: Link Decision (only for function granularity)
        if granularity == "function" and proposal in link_decision_results:
            proposal_link_data = link_decision_results[proposal]
            proposal_functions = []
            
            # Process the nested structure: proposal -> file_path -> {function_name: decision}
            for file_path, file_functions in proposal_link_data.items():
                if file_path != "selected_function_level_localization_output":  # Skip metadata
                    for function_name, link_decision in file_functions.items():
                        function_entry = {
                            "file_path": file_path,
                            "function_name": function_name,
                            "link_decision": link_decision
                        }
                        proposal_functions.append(function_entry)
            
            if proposal_functions:
                proposal_result["phase_results"]["link_decision"] = {
                    "total_functions": len(proposal_functions),
                    "functions_with_yes": sum(1 for f in proposal_functions if f["link_decision"] == "Yes"),
                    "functions_with_no": sum(1 for f in proposal_functions if f["link_decision"] == "No"),
                    "detailed_results": proposal_functions
                }
                proposal_result["final_functions"] = [f for f in proposal_functions if f["link_decision"] == "Yes"]
        
        integrated_results["proposals"][proposal] = proposal_result
    
    # Save integrated results
    integrated_json = output_dir / 'integrated_results.json'
    with open(integrated_json, 'w') as f:
        json.dump(integrated_results, f, indent=2)
    
    # Create summary report
    summary_report = output_dir / 'summary_report.txt'
    with open(summary_report, 'w') as f:
        f.write("Method v7 Coordinated Workflow - Summary Report\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Execution Time: {timestamp}\n")
        f.write(f"Batch Size: {batch_size}\n")
        f.write(f"Total Proposals: {len(granularity_results)}\n\n")
        
        f.write("Granularity Breakdown:\n")
        for granularity, count in integrated_results["workflow_info"]["granularity_breakdown"].items():
            f.write(f"  {granularity.capitalize()}: {count} proposals\n")
        f.write("\n")
        
        f.write("Results by Proposal:\n")
        f.write("-" * 30 + "\n")
        for proposal, result in integrated_results["proposals"].items():
            f.write(f"\n{proposal} ({result['granularity']} granularity):\n")
            
            if "found_files" in result:
                f.write(f"  Found Files: {len(result['found_files'])}\n")
                for file_path in result['found_files'][:5]:  # Show first 5
                    f.write(f"    - {file_path}\n")
                if len(result['found_files']) > 5:
                    f.write(f"    ... and {len(result['found_files']) - 5} more\n")
            
            if "found_functions" in result:
                f.write(f"  Found Functions: {len(result['found_functions'])}\n")
            
            if "final_functions" in result:
                f.write(f"  Final Functions (Yes): {len(result['final_functions'])}\n")
                for func in result['final_functions'][:3]:  # Show first 3
                    f.write(f"    - {func['file_path']}:{func['function_name']}\n")
                if len(result['final_functions']) > 3:
                    f.write(f"    ... and {len(result['final_functions']) - 3} more\n")
    
    print_progress(f"Integrated results saved to: {integrated_json}")
    print_progress(f"Summary report saved to: {summary_report}")
    
    # Create CSV report with detailed breakdown
    csv_report = output_dir / f'results_summary_{timestamp}.csv'
    with open(csv_report, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'Proposal No.',
            'Issue URL',
            'Granularity',
            'Directory Level',
            'File Level', 
            'Function Level',
            'Code URL'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Track previous values to avoid repetition
        all_rows = []
        
        # First, collect all rows
        for proposal, result in integrated_results["proposals"].items():
            proposal_number = extract_proposal_number(proposal)
            issue_url = get_issue_url_from_original_proposal(proposal)
            granularity = result["granularity"]
            
            # Generate rows based on granularity level
            if granularity == "directory":
                # For directory granularity, show each directory
                found_directories = result.get('found_directories', [])
                if found_directories:
                    for directory in found_directories:
                        all_rows.append({
                            'Proposal No.': proposal_number,
                            'Issue URL': issue_url,
                            'Granularity': granularity,
                            'Directory Level': directory,
                            'File Level': 'N/A',
                            'Function Level': 'N/A',
                            'Code URL': f"https://github.com/golang/go/tree/master/{directory}"
                        })
                else:
                    # Fallback if no directories found
                    all_rows.append({
                        'Proposal No.': proposal_number,
                        'Issue URL': issue_url,
                        'Granularity': granularity,
                        'Directory Level': 'No directories found',
                        'File Level': 'N/A',
                        'Function Level': 'N/A',
                        'Code URL': 'https://github.com/golang/go'
                    })
            
            elif granularity == "file":
                # For file granularity, show directories and files
                found_files = result.get('found_files', [])
                if found_files:
                    for file_path in found_files:
                        # Extract directory from file path
                        directory = str(Path(file_path).parent) if '/' in file_path else '.'
                        
                        all_rows.append({
                            'Proposal No.': proposal_number,
                            'Issue URL': issue_url,
                            'Granularity': granularity,
                            'Directory Level': directory,
                            'File Level': file_path,
                            'Function Level': 'N/A',
                            'Code URL': f"https://github.com/golang/go/blob/master/{file_path}"
                        })
                else:
                    # Fallback if no files found
                    all_rows.append({
                        'Proposal No.': proposal_number,
                        'Issue URL': issue_url,
                        'Granularity': granularity,
                        'Directory Level': 'No files found',
                        'File Level': 'No files found',
                        'Function Level': 'N/A',
                        'Code URL': 'https://github.com/golang/go'
                    })
            
            elif granularity == "function":
                # For function granularity, show directories, files, and functions
                final_functions = result.get('final_functions', [])
                found_functions = result.get('found_functions', [])
                found_files = result.get('found_files', [])
                
                # Priority 1: Use final_functions (functions with "Yes" decision)
                if final_functions:
                    for func_info in final_functions:
                        file_path = func_info.get('file_path', '')
                        function_name = func_info.get('function_name', '')
                        
                        # Extract directory from file path
                        directory = str(Path(file_path).parent) if '/' in file_path else '.'
                        
                        all_rows.append({
                            'Proposal No.': proposal_number,
                            'Issue URL': issue_url,
                            'Granularity': granularity,
                            'Directory Level': directory,
                            'File Level': file_path,
                            'Function Level': function_name,
                            'Code URL': f"https://github.com/golang/go/blob/master/{file_path}"
                        })
                
                # Priority 2: Use found_functions (all functions found, but none selected)
                elif found_functions:
                    # Group functions by file and show one "not selected" row per file
                    files_with_functions = {}
                    for func_info in found_functions:
                        file_path = func_info.get('file_path', '')
                        if file_path not in files_with_functions:
                            files_with_functions[file_path] = []
                        files_with_functions[file_path].append(func_info.get('function_name', ''))
                    
                    # Create one row per file with "not selected"
                    for file_path in files_with_functions:
                        directory = str(Path(file_path).parent) if '/' in file_path else '.'
                        
                        all_rows.append({
                            'Proposal No.': proposal_number,
                            'Issue URL': issue_url,
                            'Granularity': granularity,
                            'Directory Level': directory,
                            'File Level': file_path,
                            'Function Level': 'not selected',
                            'Code URL': f"https://github.com/golang/go/blob/master/{file_path}"
                        })
                
                # Priority 3: Fallback to file level
                elif found_files:
                    for file_path in found_files:
                        directory = str(Path(file_path).parent) if '/' in file_path else '.'
                        
                        all_rows.append({
                            'Proposal No.': proposal_number,
                            'Issue URL': issue_url,
                            'Granularity': granularity,
                            'Directory Level': directory,
                            'File Level': file_path,
                            'Function Level': 'Function analysis failed',
                            'Code URL': f"https://github.com/golang/go/blob/master/{file_path}"
                        })
                
                # Priority 4: Ultimate fallback (avoid "No results found")
                else:
                    all_rows.append({
                        'Proposal No.': proposal_number,
                        'Issue URL': issue_url,
                        'Granularity': granularity,
                        'Directory Level': 'Analysis incomplete',
                        'File Level': 'Analysis incomplete',
                        'Function Level': 'Analysis incomplete',
                        'Code URL': 'https://github.com/golang/go'
                    })
        
        # Now process rows to remove duplicates (except Code URL)
        fields_to_check = ['Proposal No.', 'Issue URL', 'Granularity', 'Directory Level', 'File Level', 'Function Level']
        previous_values = {}
        
        for i, row in enumerate(all_rows):
            # Check if this is a new proposal (Proposal No. changed)
            is_new_proposal = (i == 0 or row['Proposal No.'] != previous_values.get('Proposal No.', ''))
            
            if is_new_proposal:
                # For new proposals, show all values and reset previous_values
                for field in fields_to_check:
                    previous_values[field] = row[field]
            else:
                # For same proposal, apply duplicate removal logic
                for field in fields_to_check:
                    if field == 'Function Level':
                        # Special handling for Function Level
                        if row[field] == 'not selected':
                            # Always show "not selected" for each file, don't remove duplicates
                            previous_values[field] = row[field]
                        elif row[field] == '' and previous_values.get(field, '') == 'not selected':
                            # If this row has empty Function Level but previous was "not selected",
                            # this is likely a function granularity with no selected functions
                            row[field] = 'not selected'
                            previous_values[field] = row[field]
                        elif row[field] == previous_values.get(field, ''):
                            row[field] = ''
                        else:
                            previous_values[field] = row[field]
                    elif row[field] == previous_values.get(field, ''):
                        row[field] = ''
                    else:
                        previous_values[field] = row[field]
            
            # Write the processed row
            writer.writerow(row)
    
    print_progress(f"CSV report saved to: {csv_report}")
    
    return output_dir

def main():
    """Run the complete coordinated workflow."""
    print("Starting coordinated workflow for method_v7")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Ask user for batch size
    print("\nSelect number of proposals to process:")
    print("  - Enter a number (e.g., 5, 10, 50)")
    print("  - Enter 'all' to process all proposals")
    batch_size = input("Batch size: ").strip()
    
    # Validate input
    if batch_size.lower() != 'all':
        try:
            batch_size_int = int(batch_size)
            if batch_size_int < 1:
                print("Invalid batch size. Using default of 5.")
                batch_size = "5"
            else:
                batch_size = str(batch_size_int)
        except ValueError:
            print("Invalid batch size. Using default of 5.")
            batch_size = "5"
    
    # Ask user for repository structure
    print("\nSelect repository structure to use:")
    print("  1. repository_structure_1000")
    print("  2. repository_structure_2000 (default)")
    structure_choice = input("Choose (1/2) [default: 2]: ").strip()
    
    if structure_choice == "1":
        repository_structure = "repository_structure_1000"
    else:
        repository_structure = "repository_structure_2000"
        if structure_choice and structure_choice != "2":
            print("Invalid choice. Using default repository_structure_2000.")
    
    print(f"Processing {batch_size} proposals with {repository_structure}...\n")
    
    # Phase 0: Granularity Decision
    granularity_results, granularity_output_dir = run_granularity_decision(batch_size)
    
    # Phase 1: Directory and File Level (all proposals)
    directory_file_output_dir = run_directory_and_file_level_localization(granularity_results, repository_structure)
    
    # Phase 1 Step 3: Function Level (function granularity only)
    function_output_dir = run_function_level_localization(granularity_results, directory_file_output_dir)
    
    # Phase 2: Link Decision (function granularity only)
    link_decision_output_dir = run_function_level_link_decision(granularity_results, function_output_dir)
    
    # Create integrated results
    integrated_output_dir = create_integrated_results(
        granularity_results, granularity_output_dir, 
        directory_file_output_dir, function_output_dir, 
        link_decision_output_dir, batch_size
    )
    
    # Summary
    print("=" * 70)
    print("WORKFLOW COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("Output directories:")
    print(f"  Phase 0 (Granularity): {granularity_output_dir}")
    print(f"  Phase 1 (Directory & File): {directory_file_output_dir}")
    if function_output_dir:
        print(f"  Phase 1 (Function): {function_output_dir}")
    if link_decision_output_dir:
        print(f"  Phase 2 (Link Decision): {link_decision_output_dir}")
    print(f"  Integrated Results: {integrated_output_dir}")
    print(f"    - JSON: {integrated_output_dir / 'integrated_results.json'}")
    print(f"    - Summary: {integrated_output_dir / 'summary_report.txt'}")
    csv_files = list(integrated_output_dir.glob('results_summary_*.csv'))
    if csv_files:
        print(f"    - CSV: {csv_files[0]}")
    else:
        print(f"    - CSV: {integrated_output_dir / 'results_summary.csv'}")
    
    # Statistics
    directory_count = sum(1 for g in granularity_results.values() if g == "directory")
    file_count = sum(1 for g in granularity_results.values() if g == "file")
    function_count = sum(1 for g in granularity_results.values() if g == "function")
    
    print(f"\nFinal Statistics:")
    print(f"  Batch size requested: {batch_size}")
    print(f"  Total processed: {len(granularity_results)} proposals")
    print(f"  Directory granularity: {directory_count} proposals")
    print(f"  File granularity: {file_count} proposals")
    print(f"  Function granularity: {function_count} proposals")

if __name__ == "__main__":
    main() 