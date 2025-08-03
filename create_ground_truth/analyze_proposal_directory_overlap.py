#!/usr/bin/env python3
"""
Analyze overlap between cleaned_evaluable_proposals_for_embedding and
cleaned_evaluable_proposals_content_validated directories.

This script compares the two directories and provides detailed analysis
of which proposal files exist in each directory and the differences.
"""

import os
import json
from pathlib import Path
from typing import Set, List, Dict, Any

def get_proposal_files(directory: str) -> Set[str]:
    """Get set of proposal filenames (.md files) from a directory."""
    proposal_files = set()
    for file_path in Path(directory).glob("*.md"):
        proposal_files.add(file_path.name)
    return proposal_files

def load_ground_truth_data(filepath: str) -> Dict[str, Any]:
    """Load ground truth JSON data."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: Ground truth file not found: {filepath}")
        return {}

def extract_proposal_ids_from_ground_truth(ground_truth_data: Dict[str, Any]) -> Set[str]:
    """Extract proposal IDs from ground truth data."""
    proposal_ids = set()
    for proposal_id, proposal_data in ground_truth_data.items():
        proposal_ids.add(proposal_id)
    return proposal_ids

def main():
    # Directories to compare
    embedding_dir = "data/preprocess/accepted_proposals/cleaned_evaluable_proposals_for_embedding"
    content_validated_dir = "data/preprocess/accepted_proposals/cleaned_evaluable_proposals_content_validated"
    
    # Ground truth files
    ground_truth_content_validated = "data/ground_truth/accepted_proposals_ground_truth_content_validated.json"
    
    print("=== Proposal Directory Overlap Analysis ===\n")
    
    # Get proposal files from each directory
    embedding_files = get_proposal_files(embedding_dir)
    content_validated_files = get_proposal_files(content_validated_dir)
    
    # Remove COPY_SUMMARY.md as it's not a proposal
    content_validated_files.discard("COPY_SUMMARY.md")
    
    print(f"Files in cleaned_evaluable_proposals_for_embedding: {len(embedding_files)}")
    print(f"Files in cleaned_evaluable_proposals_content_validated: {len(content_validated_files)}")
    
    # Calculate overlaps
    common_files = embedding_files & content_validated_files
    only_in_embedding = embedding_files - content_validated_files
    only_in_content_validated = content_validated_files - embedding_files
    
    print(f"Common files: {len(common_files)}")
    print(f"Only in embedding: {len(only_in_embedding)}")
    print(f"Only in content_validated: {len(only_in_content_validated)}")
    
    # Load ground truth data to understand the relationship
    gt_content_validated = load_ground_truth_data(ground_truth_content_validated)
    gt_proposal_ids = extract_proposal_ids_from_ground_truth(gt_content_validated)
    
    print(f"\nProposals in content_validated ground truth: {len(gt_proposal_ids)}")
    
    # Check which proposals in ground truth have corresponding files
    gt_with_files = set()
    gt_without_files = set()
    
    for proposal_id in gt_proposal_ids:
        filename = f"{proposal_id}.md"
        if filename in content_validated_files:
            gt_with_files.add(proposal_id)
        else:
            gt_without_files.add(proposal_id)
    
    print(f"Ground truth proposals with files: {len(gt_with_files)}")
    print(f"Ground truth proposals without files: {len(gt_without_files)}")
    
    if gt_without_files:
        print(f"Missing files: {sorted(list(gt_without_files))}")
    
    print("\n=== Detailed Analysis ===")
    
    print(f"\n1. Files only in embedding directory ({len(only_in_embedding)}):")
    if only_in_embedding:
        # Extract proposal IDs
        only_in_embedding_ids = [f.replace('.md', '') for f in only_in_embedding]
        only_in_embedding_ids.sort()
        
        print("   Proposal IDs:", ", ".join(only_in_embedding_ids))
        
        # Check why these are not in content_validated ground truth
        missing_from_gt = []
        for proposal_id in only_in_embedding_ids:
            if proposal_id not in gt_proposal_ids:
                missing_from_gt.append(proposal_id)
        
        if missing_from_gt:
            print(f"   Not in content_validated ground truth ({len(missing_from_gt)}): {missing_from_gt}")
        
        print(f"   These {len(only_in_embedding)} proposals exist in the embedding directory")
        print("   but were excluded from content_validated directory due to content validation.")
    
    print(f"\n2. Files only in content_validated directory ({len(only_in_content_validated)}):")
    if only_in_content_validated:
        only_in_cv_ids = [f.replace('.md', '') for f in only_in_content_validated]
        print("   Proposal IDs:", ", ".join(only_in_cv_ids))
    
    print(f"\n3. Common files ({len(common_files)}):")
    print("   These proposals passed content validation and exist in both directories.")
    
    # Summary statistics
    print("\n=== Summary ===")
    print(f"• Total unique proposals across both directories: {len(embedding_files | content_validated_files)}")
    print(f"• Overlap rate: {len(common_files) / len(embedding_files | content_validated_files) * 100:.1f}%")
    print(f"• Content validation exclusion rate: {len(only_in_embedding) / len(embedding_files) * 100:.1f}%")
    
    # Validation check
    content_validated_from_files = set(f.replace('.md', '') for f in content_validated_files)
    if gt_proposal_ids == content_validated_from_files:
        print("✓ Content validated ground truth matches directory contents")
    else:
        print("✗ Mismatch between ground truth and directory contents")
        print(f"  Ground truth only: {gt_proposal_ids - content_validated_from_files}")
        print(f"  Directory only: {content_validated_from_files - gt_proposal_ids}")

if __name__ == "__main__":
    main()
