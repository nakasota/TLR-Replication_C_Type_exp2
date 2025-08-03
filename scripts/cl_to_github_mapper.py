import os
import re
import json
from pathlib import Path
from typing import Optional, Dict, List
import requests
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN not found in .env file")

class CLToGitHubMapper:
    def __init__(self, github_client=None):
        self.base_dir = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.cache_file = self.base_dir / "data" / "processed" / "cl_to_github_mapping.json"
        self.cache = self._load_cache()
        self.github_client = github_client
        
        # GitHub API headers
        self.headers = {
            'Authorization': f'token {GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        # Gerrit API headers
        self.gerrit_headers = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        }

    def _load_cache(self) -> Dict:
        """Load the CL to GitHub commit mapping cache."""
        if self.cache_file.exists():
            with open(self.cache_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_cache(self):
        """Save the CL to GitHub commit mapping cache."""
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f, indent=2)

    def get_commit_from_cl(self, cl_identifier: str) -> Optional[str]:
        """Get the GitHub commit hash for a given CL number or Change-Id."""
        # Check if it's a Change-Id
        if cl_identifier.startswith('change-id:'):
            change_id = cl_identifier.split(':')[1]
            return self._get_commit_from_change_id(change_id)
        
        # Extract CL number if it's a URL
        cl_number = re.search(r'\d+', cl_identifier).group(0)
        
        # Check cache first
        if cl_number in self.cache:
            logger.info(f"Found CL {cl_number} in cache: {self.cache[cl_number]}")
            return self.cache[cl_number]

        try:
            # Try different Gerrit API endpoints with DETAILED_ACCOUNTS and ALL_REVISIONS options
            gerrit_endpoints = [
                f"https://go-review.googlesource.com/changes/{cl_number}/detail?o=CURRENT_REVISION&o=ALL_REVISIONS&o=DETAILED_ACCOUNTS",
                f"https://go-review.googlesource.com/changes/go~{cl_number}/detail?o=CURRENT_REVISION&o=ALL_REVISIONS&o=DETAILED_ACCOUNTS",
                f"https://go-review.googlesource.com/changes/golang%2Fgo~{cl_number}/detail?o=CURRENT_REVISION&o=ALL_REVISIONS&o=DETAILED_ACCOUNTS"
            ]
            
            change_details = None
            used_endpoint = None
            
            for endpoint in gerrit_endpoints:
                response = requests.get(endpoint, headers=self.gerrit_headers)
                if response.status_code == 200:
                    # Remove the ")]}'" prefix that Gerrit adds
                    text = response.text
                    if text.startswith(")]}'"):
                        text = text[4:]
                    try:
                        change_details = json.loads(text)
                        used_endpoint = endpoint
                        logger.info(f"Successfully fetched CL {cl_number} from {endpoint}")
                        # Debug: Print the structure of change_details
                        logger.info(f"Change details keys: {list(change_details.keys())}")
                        logger.info(f"Status: {change_details.get('status')}")
                        if 'revisions' in change_details:
                            logger.info(f"Number of revisions: {len(change_details['revisions'])}")
                            logger.info(f"Revision keys: {list(change_details['revisions'].keys())}")
                        break
                    except json.JSONDecodeError:
                        logger.error(f"Failed to parse JSON from {endpoint}")
                        logger.error(f"Response text: {text[:200]}...")  # First 200 chars
                        continue
            
            if not change_details:
                logger.error(f"Failed to fetch CL {cl_number} from all endpoints")
                return None

            # Get all available revisions
            revisions = change_details.get('revisions', {})
            if not revisions:
                logger.error(f"No revisions found for CL {cl_number} (status: {change_details.get('status')})")
                if change_details.get('status') == 'ABANDONED':
                    logger.info(f"CL {cl_number} was abandoned, skipping")
                    return None
                return None

            # Try current revision first, then others if that fails
            revision_hashes = [change_details.get('current_revision')] + [
                rev for rev in revisions.keys() if rev != change_details.get('current_revision')
            ]
            revision_hashes = [rev for rev in revision_hashes if rev]  # Remove None values

            for revision_hash in revision_hashes:
                revision_details = revisions[revision_hash]
                commit_message = revision_details.get('commit', {}).get('message', '')
                
                if not commit_message:
                    continue

                # Get the Change-Id
                change_id_match = re.search(r'Change-Id: (I[a-f0-9]+)', commit_message)
                change_id = change_id_match.group(1) if change_id_match else None

                # Try different search strategies
                search_url = "https://api.github.com/search/commits"
                search_strategies = [
                    # Strategy 1: Search by commit hash
                    {'q': f'repo:golang/go hash:{revision_hash}'},
                    # Strategy 2: Search by Change-Id
                    *([] if not change_id else [{'q': f'repo:golang/go {change_id}'}]),
                    # Strategy 3: Search by commit message title
                    {'q': f'repo:golang/go "{commit_message.split(chr(10))[0]}"'},
                    # Strategy 4: Search by CL number in commit message
                    {'q': f'repo:golang/go "CL {cl_number}"'},
                    # Strategy 5: Search by commit message with fuzzy matching
                    {'q': f'repo:golang/go "{" ".join(commit_message.split()[:5])}"'}
                ]

                for strategy_index, params in enumerate(search_strategies, 1):
                    params.update({
                        'sort': 'created',
                        'order': 'desc'
                    })

                    response = requests.get(search_url, headers=self.headers, params=params)
                    
                    if response.status_code == 403:
                        logger.error("GitHub API rate limit exceeded")
                        return None
                    elif response.status_code != 200:
                        continue

                    try:
                        search_results = response.json()
                    except json.JSONDecodeError:
                        continue

                    if search_results.get('total_count', 0) > 0:
                        commit_sha = search_results['items'][0]['sha']
                        logger.info(f"Found commit {commit_sha} for CL {cl_number} using strategy {strategy_index}")
                        
                        # Verify the commit
                        if self._verify_commit(commit_sha, cl_number, change_id):
                            # Cache the result
                            self.cache[cl_number] = commit_sha
                            self._save_cache()
                            return commit_sha

            logger.warning(f"No GitHub commit found for CL {cl_number} after trying all strategies")
            return None

        except Exception as e:
            logger.error(f"Error mapping CL {cl_number} to GitHub commit: {e}")
            return None

    def _verify_commit(self, commit_sha: str, cl_number: str, change_id: Optional[str]) -> bool:
        """Verify that a GitHub commit corresponds to a Gerrit CL."""
        try:
            if not self.github_client:
                return True  # Skip verification if no GitHub client is available
            
            repo = self.github_client.get_repo("golang/go")
            commit = repo.get_commit(commit_sha)
            commit_message = commit.commit.message
            
            # Check for CL number in commit message
            if f"CL {cl_number}" in commit_message:
                return True
            
            # Check for Change-Id if available
            if change_id and change_id in commit_message:
                return True
            
            return False
        except Exception as e:
            logger.error(f"Error verifying commit {commit_sha}: {e}")
            return False

    def _get_commit_from_change_id(self, change_id: str) -> Optional[str]:
        """Get the GitHub commit hash for a given Gerrit Change-Id."""
        try:
            search_url = "https://api.github.com/search/commits"
            params = {
                'q': f'repo:golang/go {change_id}',
                'sort': 'created',
                'order': 'desc'
            }

            response = requests.get(search_url, headers=self.headers, params=params)
            
            if response.status_code == 200:
                results = response.json()
                if results.get('total_count', 0) > 0:
                    return results['items'][0]['sha']
            
            return None
        except Exception as e:
            logger.error(f"Error looking up Change-Id {change_id}: {e}")
            return None

    def get_modified_functions(self, commit_sha: str) -> List[str]:
        """Get the list of modified Go functions from a GitHub commit."""
        try:
            # Get the commit details
            url = f"https://api.github.com/repos/golang/go/commits/{commit_sha}"
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                logger.error(f"Failed to fetch commit details for {commit_sha}")
                return []

            commit_data = response.json()
            
            # Get the files changed in this commit
            modified_functions = []
            for file in commit_data['files']:
                if not file['filename'].endswith('.go'):
                    continue
                
                # Get the patch and extract function names
                patch = file.get('patch', '')
                if patch:
                    # Look for function declarations in the patch
                    func_matches = re.finditer(r'[+-]func\s+(\w+)', patch)
                    for match in func_matches:
                        func_name = match.group(1)
                        modified_functions.append(func_name)

            return list(set(modified_functions))  # Remove duplicates

        except Exception as e:
            logger.error(f"Error getting modified functions for commit {commit_sha}: {e}")
            return []

def main():
    # Example usage
    mapper = CLToGitHubMapper()
    cl_number = "12345"  # Example CL number
    
    commit_sha = mapper.get_commit_from_cl(cl_number)
    if commit_sha:
        print(f"Found GitHub commit: {commit_sha}")
        modified_functions = mapper.get_modified_functions(commit_sha)
        print(f"Modified functions: {modified_functions}")
    else:
        print(f"Could not find GitHub commit for CL {cl_number}")

if __name__ == "__main__":
    main() 