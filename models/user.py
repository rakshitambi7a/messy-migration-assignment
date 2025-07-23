from werkzeug.security import generate_password_hash, check_password_hash
from db.database import Database

class User:
    def __init__(self, user_id=None, name=None, email=None, password=None):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.db = Database()
    
    @classmethod
    def find_by_id(cls, user_id):
        db = Database()
        result = db.execute_one(
            "SELECT * FROM users WHERE id = ?", 
            (user_id,)
        )
        if result:
            return cls(result['id'], result['name'], result['email'], result['password'])
        return None
    
    @classmethod
    def find_by_email(cls, email):
        db = Database()
        result = db.execute_one(
            "SELECT * FROM users WHERE email = ?", 
            (email,)
        )
        if result:
            return cls(result['id'], result['name'], result['email'], result['password'])
        return None
    
    @classmethod
    def get_all(cls):
        db = Database()
        results = db.execute_query("SELECT * FROM users")
        return [cls(row['id'], row['name'], row['email'], row['password']) for row in results]
    
    def save(self):
        if self.id:
            # Update existing user
            self.db.execute_query(
                "UPDATE users SET name = ?, email = ? WHERE id = ?",
                (self.name, self.email, self.id)
            )
        else:
            # Create new user
            if self.password is None:
                raise ValueError("Password cannot be None for a new user.")
            
            hashed_password = generate_password_hash(self.password)
            self.db.execute_query(
                "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                (self.name, self.email, hashed_password)
            )
            # Get the last inserted row ID for SQLite
            result = self.db.execute_one("SELECT last_insert_rowid() as id")
            self.id = result['id'] if result else None
    
    def delete(self):
        if self.id:
            self.db.execute_query("DELETE FROM users WHERE id = ?", (self.id,))
    
    @classmethod
    def search_by_name(cls, name):
        db = Database()
        results = db.execute_query(
            "SELECT * FROM users WHERE name LIKE ?", 
            (f"%{name}%",)
        )
        return [cls(row['id'], row['name'], row['email'], row['password']) for row in results]
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
            # Never include password in output
        }