import json
from collections import defaultdict
from pathlib import Path

# Path to the ground truth JSON file
GT_PATH = Path(__file__).parent.parent / "data" / "preprocess" / "accepted_proposals_ground_truth.json"

def main():
    with open(GT_PATH, "r") as f:
        data = json.load(f)

    results = []
    for entry in data:
        proposal_id = entry.get("proposal_id")
        files = entry.get("files", [])
        functions = entry.get("functions", [])
        # Get unique directories from file paths
        directories = set()
        for file_path in files:
            dir_path = "/".join(file_path.split("/")[:-1])
            if dir_path:
                directories.add(dir_path)
        results.append({
            "proposal_id": proposal_id,
            "num_directories": len(directories),
            "num_files": len(files),
            "num_functions": len(functions)
        })

    # Print results
    for r in results:
        print(f"Proposal {r['proposal_id']}: {r['num_directories']} directories, {r['num_files']} files, {r['num_functions']} functions")

if __name__ == "__main__":
    main()
