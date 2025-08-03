#!/usr/bin/env python3
"""
Cost Tracking Utilities for Method v9
Provides functions to track token usage and costs in main.py scripts
"""

import json
import time
from datetime import datetime
from pathlib import Path

# Import tiktoken for accurate token counting
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
    print("✅ tiktoken available for accurate token counting")
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print("⚠️  tiktoken not available, using estimation")

# GPT-4o pricing (per 1M tokens)
GPT4O_INPUT_PRICE = 2.50
GPT4O_CACHED_INPUT_PRICE = 1.25
GPT4O_OUTPUT_PRICE = 10.00

class GPT4oCostTracker:
    """Track GPT-4o API costs and token usage"""
    
    def __init__(self, save_dir=None):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_api_calls = 0
        self.start_time = time.time()
        self.api_call_details = []
        self.save_dir = Path(save_dir) if save_dir else Path.cwd()
        
        # Initialize tiktoken encoder
        self.tokenizer = None
        if TIKTOKEN_AVAILABLE:
            try:
                self.tokenizer = tiktoken.encoding_for_model("gpt-4")
            except:
                try:
                    self.tokenizer = tiktoken.get_encoding("cl100k_base")
                except:
                    self.tokenizer = None
        
        print(f"🔧 Cost tracker initialized. Save directory: {self.save_dir}")
    
    def count_tokens(self, text: str) -> int:
        """Count tokens accurately using tiktoken"""
        if self.tokenizer:
            try:
                return len(self.tokenizer.encode(text))
            except Exception as e:
                print(f"Warning: tiktoken encoding failed: {e}")
        
        # Fallback: 4 chars per token
        return len(text) // 4
    
    def track_api_request(self, prompt: str, proposal_name: str = None):
        """Track an API request before sending"""
        input_tokens = self.count_tokens(prompt)
        
        call_info = {
            'call_number': self.total_api_calls + 1,
            'proposal_name': proposal_name,
            'input_tokens': input_tokens,
            'prompt_preview': prompt[:200] + "..." if len(prompt) > 200 else prompt,
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"[COST] 📤 API Call #{call_info['call_number']}")
        if proposal_name:
            print(f"[COST]    Proposal: {proposal_name}")
        print(f"[COST]    Input tokens: {input_tokens:,}")
        
        return call_info
    
    def track_api_response(self, call_info: dict, response_data: dict, raw_response: str = None):
        """Track an API response after receiving"""
        # Count output tokens
        if raw_response:
            output_tokens = self.count_tokens(raw_response)
        else:
            # Try to extract from response_data
            content = ""
            if 'choices' in response_data and response_data['choices']:
                content = response_data['choices'][0].get('message', {}).get('content', '')
            output_tokens = self.count_tokens(content)
        
        # Get actual usage from OpenAI response if available
        actual_input_tokens = call_info['input_tokens']
        actual_output_tokens = output_tokens
        
        if 'usage' in response_data:
            usage = response_data['usage']
            actual_input_tokens = usage.get('prompt_tokens', call_info['input_tokens'])
            actual_output_tokens = usage.get('completion_tokens', output_tokens)
            total_tokens = usage.get('total_tokens', actual_input_tokens + actual_output_tokens)
            
            print(f"[COST] 📥 Response received")
            print(f"[COST]    Actual input tokens: {actual_input_tokens:,}")
            print(f"[COST]    Actual output tokens: {actual_output_tokens:,}")
            print(f"[COST]    Total tokens: {total_tokens:,}")
        else:
            print(f"[COST] 📥 Response received")
            print(f"[COST]    Estimated output tokens: {output_tokens:,}")
        
        # Update totals
        self.total_input_tokens += actual_input_tokens
        self.total_output_tokens += actual_output_tokens
        self.total_api_calls += 1
        
        # Calculate costs
        input_cost = (actual_input_tokens / 1_000_000) * GPT4O_INPUT_PRICE
        output_cost = (actual_output_tokens / 1_000_000) * GPT4O_OUTPUT_PRICE
        call_cost = input_cost + output_cost
        
        # Complete call info
        call_info.update({
            'estimated_output_tokens': output_tokens,
            'actual_input_tokens': actual_input_tokens,
            'actual_output_tokens': actual_output_tokens,
            'input_cost_usd': input_cost,
            'output_cost_usd': output_cost,
            'call_cost_usd': call_cost,
            'response_preview': (raw_response or content)[:200] + "..." if len(raw_response or content) > 200 else (raw_response or content)
        })
        
        if 'usage' in response_data:
            call_info['openai_usage'] = response_data['usage']
        
        self.api_call_details.append(call_info)
        
        # Show running totals
        total_cost = (self.total_input_tokens / 1_000_000 * GPT4O_INPUT_PRICE + 
                     self.total_output_tokens / 1_000_000 * GPT4O_OUTPUT_PRICE)
        
        print(f"[COST] 💰 Call cost: ${call_cost:.6f}")
        print(f"[COST] 📊 Running totals: {self.total_input_tokens:,} input + {self.total_output_tokens:,} output = ${total_cost:.6f}")
        print()
        
        return call_info
    
    def get_cost_summary(self):
        """Get comprehensive cost summary"""
        elapsed_time = time.time() - self.start_time
        
        input_cost = (self.total_input_tokens / 1_000_000) * GPT4O_INPUT_PRICE
        output_cost = (self.total_output_tokens / 1_000_000) * GPT4O_OUTPUT_PRICE
        total_cost = input_cost + output_cost
        
        summary = {
            'execution_info': {
                'start_time': datetime.fromtimestamp(self.start_time).isoformat(),
                'end_time': datetime.now().isoformat(),
                'elapsed_seconds': elapsed_time,
                'tiktoken_available': TIKTOKEN_AVAILABLE
            },
            'token_usage': {
                'total_api_calls': self.total_api_calls,
                'total_input_tokens': self.total_input_tokens,
                'total_output_tokens': self.total_output_tokens,
                'total_tokens': self.total_input_tokens + self.total_output_tokens,
                'avg_input_per_call': self.total_input_tokens / max(1, self.total_api_calls),
                'avg_output_per_call': self.total_output_tokens / max(1, self.total_api_calls)
            },
            'costs_usd': {
                'input_cost': input_cost,
                'output_cost': output_cost,
                'total_cost': total_cost,
                'cost_per_call': total_cost / max(1, self.total_api_calls)
            },
            'pricing_info': {
                'gpt4o_input_per_1m': GPT4O_INPUT_PRICE,
                'gpt4o_cached_input_per_1m': GPT4O_CACHED_INPUT_PRICE,
                'gpt4o_output_per_1m': GPT4O_OUTPUT_PRICE
            },
            'api_call_details': self.api_call_details
        }
        
        return summary
    
    def save_cost_report(self, filename_prefix="cost_report"):
        """Save detailed cost report to JSON file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{filename_prefix}_{timestamp}.json"
        filepath = self.save_dir / filename
        
        summary = self.get_cost_summary()
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Cost report saved to: {filepath}")
        return filepath
    
    def print_summary(self):
        """Print cost summary to console"""
        summary = self.get_cost_summary()
        
        print("\n" + "=" * 60)
        print("💰 GPT-4o COST SUMMARY")
        print("=" * 60)
        
        tokens = summary['token_usage']
        costs = summary['costs_usd']
        exec_info = summary['execution_info']
        
        print(f"⏱️  Execution time: {exec_info['elapsed_seconds']:.1f} seconds")
        print(f"🔧 Tiktoken available: {'Yes' if exec_info['tiktoken_available'] else 'No'}")
        print(f"📞 Total API calls: {tokens['total_api_calls']:,}")
        print(f"📥 Total input tokens: {tokens['total_input_tokens']:,}")
        print(f"📤 Total output tokens: {tokens['total_output_tokens']:,}")
        print(f"🎯 Total tokens: {tokens['total_tokens']:,}")
        print(f"📊 Average input per call: {tokens['avg_input_per_call']:.0f}")
        print(f"📊 Average output per call: {tokens['avg_output_per_call']:.0f}")
        print()
        print(f"💵 Input cost: ${costs['input_cost']:.6f}")
        print(f"💵 Output cost: ${costs['output_cost']:.6f}")
        print(f"💰 Total cost: ${costs['total_cost']:.6f}")
        print(f"💲 Cost per API call: ${costs['cost_per_call']:.6f}")
        print("=" * 60)

# Helper function to create tracker instances
def create_cost_tracker(save_dir=None):
    """Create a new cost tracker instance"""
    return GPT4oCostTracker(save_dir)

# Example usage functions
def track_openai_request(tracker, prompt, proposal_name=None):
    """Helper to track an OpenAI request"""
    return tracker.track_api_request(prompt, proposal_name)

def track_openai_response(tracker, call_info, response_data, raw_response=None):
    """Helper to track an OpenAI response"""
    return tracker.track_api_response(call_info, response_data, raw_response)
