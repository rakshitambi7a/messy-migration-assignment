from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from utils.validators import UserValidator

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Authenticate user with email and password.
    Supports both bcrypt hashed and legacy plaintext passwords.
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Extract email and password
        email = data.get('email', '').strip()
        password = data.get('password', '')
        
        # Validate input
        if not email:
            return jsonify({"error": "Email is required"}), 400
        
        if not password:
            return jsonify({"error": "Password is required"}), 400
        
        # Validate email format
        if not UserValidator.validate_email(email):
            return jsonify({"error": "Invalid email format"}), 400
        
        # Authenticate user
        user = AuthService.authenticate(email, password)
        
        if user:
            return jsonify({
                "status": "success",
                "message": "Login successful",
                "user": user.to_dict()
            }), 200
        else:
            return jsonify({
                "status": "failed",
                "message": "Invalid email or password"
            }), 401
    
    except Exception as e:
        # Log the error in production
        print(f"Login error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
