from flask import Blueprint, request, jsonify, g
from models.user import User
from utils.validators import UserValidator
from services.auth_service import AuthService
from services.jwt_service import token_required, optional_token

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET'])
@optional_token
def get_all_users():
    """Get all users. Authentication is optional for this endpoint."""
    users = User.get_all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.find_by_id(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/profile', methods=['GET'])
@token_required
def get_profile():
    """
    Get current user's profile. Requires JWT authentication.
    Demonstrates protected route functionality.
    """
    current_user = g.current_user
    return jsonify({
        "message": "Profile retrieved successfully",
        "user": current_user.to_dict(),
        "authenticated": True
    })

@user_bp.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user with the provided data.
    Expects JSON payload with 'name', 'email', and 'password'.
    Returns a success message and user details on success, or an error message on failure.
    """
    try:
        # Step 1: Get and validate JSON data
        data = request.get_json()
        print(f"DEBUG: Received data: {data}")
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Step 2: Check required fields exist
        required_fields = ['name', 'email', 'password']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        print(f"DEBUG: About to validate data")
        
        # Step 3: Validate data
        errors = UserValidator.validate_user_data(data)
        if errors:
            print(f"DEBUG: Validation errors: {errors}")
            return jsonify({"errors": errors}), 400
        
        print(f"DEBUG: About to create user object")
        
        # Step 4: Create user object
        user = User(
            name=data['name'].strip(),
            email=data['email'].strip(),
            password=data['password']
        )
        
        print(f"DEBUG: User object created, about to save")
        
        # Step 5: Save user
        user.save()
        
        print(f"DEBUG: User saved successfully")
        
        return jsonify({"message": "User created", "user": user.to_dict()}), 201
    
    except ValueError as e:
        print(f"DEBUG: ValueError caught: {str(e)}")
        return jsonify({"error": f"Invalid data: {str(e)}"}), 400
    except AttributeError as e:
        print(f"DEBUG: AttributeError caught: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Invalid attribute in data: {str(e)}"}), 400
    except Exception as e:
        print(f"DEBUG: Unexpected error caught: {str(e)}")
        print(f"DEBUG: Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = User.find_by_id(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        user.name = data.get('name', user.name).strip()
        user.email = data.get('email', user.email).strip()
        
        user.save()
        return jsonify({"message": "User updated", "user": user.to_dict()})
    
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.find_by_id(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        user.delete()
        return jsonify({"message": "User deleted"})
    
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@user_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name', '').strip()
    if not name:
        return jsonify({"error": "Please provide a name to search"}), 400
    
    users = User.search_by_name(name)
    return jsonify([user.to_dict() for user in users])