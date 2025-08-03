#!/bin/bash
# Test script for embedding-based evaluation with memory management

echo "=== Testing Embedding-Based Evaluation with Memory Management ==="

# First, test with just 3 proposals
echo "🔬 Testing with 3 proposals..."
python embedding_based_localization_full.py --max-proposals 3

echo ""
echo "✅ If the above worked, you can try with more proposals:"
echo "   python embedding_based_localization_full.py --max-proposals 10"
echo "   python embedding_based_localization_full.py --max-proposals 20"
echo "   python embedding_based_localization_full.py --all  # All proposals"

echo ""
echo "📊 Memory usage tips:"
echo "   - Use --max-proposals to limit memory usage"
echo "   - Monitor memory with: docker stats [container_name]"
echo "   - The script now does garbage collection every 5 proposals"
