
from werkzeug.security import check_password_hash
from models.user import User

class AuthService:
    

    @staticmethod
    def authenticate(email, password):
        
        user = User.find_by_email(email)
        if not user:
            return None
        
        stored_password = user.password
        
        # Ensure stored_password is not None before checking
        if stored_password and check_password_hash(stored_password, password):
            return user
        
        return None

    