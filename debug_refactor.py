#!/usr/bin/env python3
"""
Debug script to test the refactored architecture
"""
import os
import sys
sys.path.insert(0, '.')

# Set testing environment
os.environ['TESTING'] = '1'

def test_components():
    """Test each component individually"""
    try:
        print("=== Testing Refactored Architecture ===")
        
        # Test 1: Basic imports
        print("\n1. Testing imports...")
        from utils.validators import validate_user_data, validate_email
        print("   ✓ Validators imported")
        
        from core.container import container
        print("   ✓ Container imported")
        
        # Test 2: Container services
        print("\n2. Testing container services...")
        user_service = container.user_service()
        print("   ✓ User service created")
        
        # Test 3: Validation
        print("\n3. Testing validation...")
        test_data = {
            'name': 'Test User',
            'email': 'test@example.com', 
            'password': 'password123'
        }
        
        is_valid = validate_user_data(test_data)
        print(f"   ✓ Data validation: {is_valid}")
        
        email_valid = validate_email(test_data['email'])
        print(f"   ✓ Email validation: {email_valid}")
        
        # Test 4: Service operation
        print("\n4. Testing service operation...")
        result = user_service.create_user(test_data)
        print(f"   ✓ Service create_user result: {result}")
        
        # Test 5: Flask app creation
        print("\n5. Testing Flask app...")
        from app import create_app
        app = create_app()
        print("   ✓ Flask app created")
        
        with app.test_client() as client:
            response = client.post('/users', 
                                 json=test_data,
                                 content_type='application/json')
            print(f"   ✓ HTTP response status: {response.status_code}")
            print(f"   ✓ HTTP response data: {response.get_json()}")
        
        print("\n=== All tests completed successfully! ===")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = test_components()
    sys.exit(0 if success else 1)
