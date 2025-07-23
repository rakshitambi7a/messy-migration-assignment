#!/usr/bin/env python3
"""
Debug script to test JWT authentication step by step
"""

import requests
import json

BASE_URL = "http://localhost:5009"

def debug_jwt_authentication():
    """Debug JWT authentication flow"""
    print("🔍 Debugging JWT Authentication Flow")
    print("=" * 50)
    
    # Step 1: Login to get token
    print("\n1. Testing Login...")
    login_data = {
        "email": "rakshitambi7a@gmail.com",  # Use your actual email
        "password": "yourpassword"  # Use your actual password
    }
    
    try:
        response = requests.post(f"{BASE_URL}/login", json=login_data, timeout=10)
        print(f"   Login Status: {response.status_code}")
        
        if response.status_code == 200:
            login_result = response.json()
            token = login_result.get('token')
            print(f"   ✅ Login successful!")
            print(f"   Token: {token[:50]}...")
            
            # Step 2: Test protected route
            print("\n2. Testing Protected Route (/profile)...")
            
            # Test with Authorization header (correct way)
            headers = {"Authorization": f"Bearer {token}"}
            print(f"   Using header: Authorization: Bearer {token[:20]}...")
            
            response = requests.get(f"{BASE_URL}/profile", headers=headers, timeout=10)
            print(f"   Profile Status: {response.status_code}")
            
            if response.status_code == 200:
                print(f"   ✅ Protected route access successful!")
                profile_data = response.json()
                print(f"   User: {profile_data.get('user', {}).get('name')}")
            else:
                print(f"   ❌ Protected route failed")
                print(f"   Response: {response.text}")
                
                # Try alternative method with query parameter
                print("\n3. Testing with Query Parameter...")
                response = requests.get(f"{BASE_URL}/profile?token={token}", timeout=10)
                print(f"   Profile Status (query): {response.status_code}")
                
                if response.status_code == 200:
                    print(f"   ✅ Query parameter method worked!")
                else:
                    print(f"   ❌ Query parameter method also failed")
                    print(f"   Response: {response.text}")
        else:
            print(f"   ❌ Login failed: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Cannot connect to server. Make sure the app is running.")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def test_token_format():
    """Test different token formats"""
    print("\n🧪 Testing Token Formats")
    print("=" * 30)
    
    # Dummy token for format testing
    dummy_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.dummy.signature"
    
    test_cases = [
        ("Correct format", f"Bearer {dummy_token}"),
        ("Missing Bearer", dummy_token),
        ("Lowercase bearer", f"bearer {dummy_token}"),
        ("Extra spaces", f"Bearer  {dummy_token}"),
        ("Wrong prefix", f"Token {dummy_token}"),
    ]
    
    for description, auth_header in test_cases:
        print(f"\n   {description}: {auth_header[:30]}...")
        headers = {"Authorization": auth_header}
        
        try:
            response = requests.get(f"{BASE_URL}/profile", headers=headers, timeout=5)
            print(f"   Status: {response.status_code}")
            if response.status_code != 200:
                result = response.json()
                print(f"   Error: {result.get('error', 'Unknown error')}")
        except Exception as e:
            print(f"   Exception: {e}")

if __name__ == "__main__":
    # Check if server is running
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running\n")
            debug_jwt_authentication()
            test_token_format()
        else:
            print("❌ Server not responding correctly")
    except requests.exceptions.ConnectionError:
        print("❌ Server not running. Please start with: python app.py")
    except Exception as e:
        print(f"❌ Error checking server: {e}")
