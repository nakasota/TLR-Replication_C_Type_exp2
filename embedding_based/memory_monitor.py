#!/usr/bin/env python3
"""
Memory monitoring script for embedding-based evaluation.
This script helps monitor memory usage during evaluation.
"""

import psutil
import gc
import sys
import os

def get_memory_info():
    """Get current memory usage information."""
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    
    # Get system memory info
    virtual_memory = psutil.virtual_memory()
    
    return {
        'process_rss_mb': memory_info.rss / (1024 * 1024),  # Resident memory in MB
        'process_vms_mb': memory_info.vms / (1024 * 1024),  # Virtual memory in MB
        'system_total_mb': virtual_memory.total / (1024 * 1024),
        'system_available_mb': virtual_memory.available / (1024 * 1024),
        'system_used_percent': virtual_memory.percent
    }

def print_memory_usage(prefix=""):
    """Print current memory usage."""
    info = get_memory_info()
    print(f"{prefix}Memory Usage:")
    print(f"  Process RSS: {info['process_rss_mb']:.1f} MB")
    print(f"  Process VMS: {info['process_vms_mb']:.1f} MB")
    print(f"  System: {info['system_used_percent']:.1f}% used ({info['system_available_mb']:.1f} MB available)")
    
def force_cleanup():
    """Force garbage collection and print memory usage."""
    print("🧹 Forcing memory cleanup...")
    gc.collect()
    print_memory_usage("  After cleanup - ")

if __name__ == "__main__":
    print("=== Memory Monitor ===")
    print_memory_usage("Initial - ")
    
    # Check if we're in a Docker container
    if os.path.exists('/.dockerenv'):
        print("📦 Running in Docker container")
        
        # Check Docker memory limits
        try:
            with open('/sys/fs/cgroup/memory/memory.limit_in_bytes', 'r') as f:
                limit_bytes = int(f.read().strip())
                if limit_bytes < 9223372036854775807:  # Not unlimited
                    limit_mb = limit_bytes / (1024 * 1024)
                    print(f"   Docker memory limit: {limit_mb:.1f} MB")
                else:
                    print("   Docker memory limit: unlimited")
        except:
            print("   Could not read Docker memory limit")
    else:
        print("💻 Running on host system")
    
    # Force cleanup and show result
    force_cleanup()
