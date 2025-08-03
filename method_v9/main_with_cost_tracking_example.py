#!/usr/bin/env python3
"""
Example: Modified main.py with cost tracking
This shows how to integrate cost tracking into method_v9 main.py scripts

Copy the relevant parts into the actual main.py files:
- method_v9/directory_and_file_level/main.py
- method_v9/directory_and_file_level/main_1000.py  
- method_v9/function_level/main.py
"""

import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path
import json
import subprocess
from datetime import datetime
import time
import random

# Import cost tracking utilities
sys.path.append(str(Path(__file__).parent))
from cost_tracking_utils import create_cost_tracker, track_openai_request, track_openai_response

# Initialize cost tracker at the beginning of main()
def main():
    # Create cost tracker with output directory
    output_root = Path(__file__).parent / 'output'
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = output_root / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize cost tracker
    cost_tracker = create_cost_tracker(save_dir=output_dir)
    
    # ... existing setup code ...
    
    # Load environment variables from .env
    load_dotenv(dotenv_path=Path(__file__).parent.parent.parent / '.env')
    
    API_KEY = os.getenv('OPENAI_API_KEY')
    if not API_KEY:
        print("Error: OPENAI_API_KEY not found in .env file.", file=sys.stderr)
        sys.exit(1)
    
    API_URL = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # ... existing proposal loading code ...
    
    proposals_dir = Path(__file__).parent.parent.parent / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals'
    proposal_files = list(proposals_dir.glob('*.md'))
    total = len(proposal_files)
    
    print(f"📊 Processing {total} proposals with cost tracking enabled")
    
    llm_outputs = {}
    
    for idx, proposal_file in enumerate(proposal_files, 1):
        print(f"Processing {idx}/{total}: {proposal_file.name}")
        
        # ... existing file processing code ...
        
        # Process each structure file separately
        for structure_file in structure_files:
            print(f"  Processing with {structure_file.name}...")
            
            # Generate prompt using directory_and_file_level_localization.py
            prompt_script = Path(__file__).parent / 'prompt' / 'directory_and_file_level_localization.py'
            result = subprocess.run([
                sys.executable, str(prompt_script), str(proposal_file.resolve()), str(structure_file.resolve())
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"    Prompt generation failed for {structure_file.name}: {result.stderr}")
                continue
            
            prompt = result.stdout
            
            # ★ COST TRACKING: Track the request
            call_info = track_openai_request(
                cost_tracker, 
                prompt, 
                proposal_name=f"{proposal_file.name}_{structure_file.name}"
            )
            
            payload = {
                "model": "gpt-4o",
                "temperature": 0.0,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
            
            # Make API request
            success, response_data, error_msg = make_api_request_with_retry(API_URL, headers, payload, max_retries=3, base_delay=2)
            print(f"    LLM API status for {structure_file.name}: {'Success' if success else 'Failed'}")
            
            if success:
                try:
                    content = response_data['choices'][0]['message']['content']
                    
                    # ★ COST TRACKING: Track the response
                    track_openai_response(
                        cost_tracker,
                        call_info,
                        response_data,
                        raw_response=content
                    )
                    
                    print(f"    LLM API raw output (first 200 chars):\n{content[:200]}\n---")
                    
                    # ... existing response processing code ...
                    
                except Exception as e:
                    print(f"    [ERROR] Failed to parse LLM output for {structure_file.name}: {e}")
            else:
                print(f"    [ERROR] LLM API call failed for {structure_file.name}: {error_msg}")
        
        # ... existing aggregation code ...
    
    # Save results
    output_json = output_dir / 'llm_outputs.json'
    with open(output_json, 'w') as f:
        json.dump(llm_outputs, f, indent=2)
    
    print(f"\nResults saved to: {output_json}")
    print(f"Total proposals processed: {len(llm_outputs)}")
    
    # ★ COST TRACKING: Print summary and save report
    cost_tracker.print_summary()
    cost_report_file = cost_tracker.save_cost_report("directory_file_level_cost")
    
    print(f"\n🎉 Execution completed!")
    print(f"📄 Main results: {output_json}")
    print(f"💰 Cost report: {cost_report_file}")

def make_api_request_with_retry(api_url, headers, payload, max_retries=3, base_delay=2):
    """
    APIリクエストをリトライ機能付きで実行
    """
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                return True, response.json(), None
            elif response.status_code == 429:  # Rate limit
                print(f"    [RETRY] Rate limit hit, attempt {attempt + 1}/{max_retries + 1}")
                if attempt < max_retries:
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    time.sleep(delay)
                    continue
            else:
                print(f"    [ERROR] API returned status {response.status_code}, attempt {attempt + 1}/{max_retries + 1}")
                if attempt < max_retries:
                    delay = base_delay * (2 ** attempt)
                    time.sleep(delay)
                    continue
                    
        except requests.exceptions.SSLError as e:
            print(f"    [RETRY] SSL error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                time.sleep(delay)
                continue
                
        except requests.exceptions.ConnectionError as e:
            print(f"    [RETRY] Connection error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                time.sleep(delay)
                continue
                
        except requests.exceptions.Timeout as e:
            print(f"    [RETRY] Timeout on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
                continue
                
        except Exception as e:
            print(f"    [RETRY] Unexpected error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
                continue
    
    return False, None, f"Failed after {max_retries + 1} attempts"

if __name__ == '__main__':
    main()

"""
INTEGRATION INSTRUCTIONS:

1. Copy cost_tracking_utils.py to method_v9/ directory

2. Add these imports to the top of main.py files:
   ```python
   sys.path.append(str(Path(__file__).parent))
   from cost_tracking_utils import create_cost_tracker, track_openai_request, track_openai_response
   ```

3. Initialize cost tracker in main():
   ```python
   cost_tracker = create_cost_tracker(save_dir=output_dir)
   ```

4. Before each API call:
   ```python
   call_info = track_openai_request(cost_tracker, prompt, proposal_name=proposal_file.name)
   ```

5. After each successful API response:
   ```python
   track_openai_response(cost_tracker, call_info, response_data, raw_response=content)
   ```

6. At the end of execution:
   ```python
   cost_tracker.print_summary()
   cost_tracker.save_cost_report("script_name_cost")
   ```

This will provide:
- Real-time cost tracking during execution
- Accurate token counting with tiktoken
- Detailed cost reports saved to JSON
- Per-call and total cost summaries
- Input/output token breakdown
"""
