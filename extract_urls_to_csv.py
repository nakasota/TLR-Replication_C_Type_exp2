#!/usr/bin/env python3
"""
Extract URLs from the second line of markdown files in accepted_proposals and declined_proposals directories
and create CSV files with columns "No." and "Issue URL"
"""

import os
import csv
import re
from pathlib import Path

def extract_url_from_file(file_path):
    """Extract URL from the second line of a markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) >= 2:
                second_line = lines[1].strip()
                # Extract URL from "Issue URL: <URL>" format
                if second_line.startswith("Issue URL: "):
                    url = second_line.replace("Issue URL: ", "").strip()
                    return url
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def process_directory(directory_path, output_csv_path):
    """Process all .md files in a directory and create a CSV file"""
    results = []
    
    # Get all .md files and sort them by number
    md_files = [f for f in os.listdir(directory_path) if f.endswith('.md')]
    md_files.sort(key=lambda x: int(x.split('.')[0]) if x.split('.')[0].isdigit() else float('inf'))
    
    for filename in md_files:
        if filename.endswith('.md'):
            file_path = os.path.join(directory_path, filename)
            # Extract number from filename (without .md extension)
            number = filename.replace('.md', '')
            
            # Extract URL from file
            url = extract_url_from_file(file_path)
            
            if url:
                results.append([number, url])
            else:
                print(f"Warning: Could not extract URL from {filename}")
    
    # Write to CSV
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['No.', 'Issue URL'])  # Header
        writer.writerows(results)
    
    print(f"Created {output_csv_path} with {len(results)} entries")
    return len(results)

def main():
    # Base directory path
    base_path = "data/preprocess"
    
    # Process accepted proposals
    accepted_dir = os.path.join(base_path, "accepted_proposals")
    accepted_csv = os.path.join(base_path, "accepted_proposals_urls.csv")
    
    if os.path.exists(accepted_dir):
        accepted_count = process_directory(accepted_dir, accepted_csv)
        print(f"Processed {accepted_count} accepted proposals")
    else:
        print(f"Directory not found: {accepted_dir}")
    
    # Process declined proposals
    declined_dir = os.path.join(base_path, "declined_proposals")
    declined_csv = os.path.join(base_path, "declined_proposals_urls.csv")
    
    if os.path.exists(declined_dir):
        declined_count = process_directory(declined_dir, declined_csv)
        print(f"Processed {declined_count} declined proposals")
    else:
        print(f"Directory not found: {declined_dir}")

if __name__ == "__main__":
    main()
