# test_setup.py
print("Testing setup...\n")

# Test file locations
import os
print(f"Current directory: {os.getcwd()}")

# Test ELIZA
try:
    from eliza_custom import get_eliza_response
    print("✓ ELIZA loaded successfully")
    test_response = get_eliza_response("Hello")
    print(f"  Response: {test_response}")
except Exception as e:
    print(f"✗ ELIZA error: {e}")

# Test packages
try:
    import transformers
    print(f"✓ Transformers version: {transformers.__version__}")
except:
    print("✗ Transformers not installed")

try:
    import torch
    print(f"✓ PyTorch version: {torch.__version__}")
except:
    print("✗ PyTorch not installed")

print("\nSetup test complete!")