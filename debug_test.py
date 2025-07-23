#!/usr/bin/env python3
"""
Debug test to check imports
"""

import sys
import os

print(f"Current working directory: {os.getcwd()}")
print(f"Python executable: {sys.executable}")
print(f"Python path: {sys.path}")

try:
    from utils.validators import UserValidator
    print("✅ Import successful!")
    
    # Test basic functionality
    result = UserValidator.validate_email("test@example.com")
    print(f"✅ Email validation works: {result}")
    
    result = UserValidator.validate_password("password123")
    print(f"✅ Password validation works: {result}")
    
    result = UserValidator.validate_name("John Doe")
    print(f"✅ Name validation works: {result}")
    
    print("🎉 All basic tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
