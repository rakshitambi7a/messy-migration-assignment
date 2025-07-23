import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def migrate_plaintext_to_bcrypt():
    """
    Migrate all plaintext passwords to hashed passwords using werkzeug.
    This function identifies plaintext passwords and converts them to hashed passwords.
    """
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Get all users
        cursor.execute("SELECT id, email, password FROM users")
        users = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return
    
    migration_count = 0
    
    for user_id, email, stored_password in users:
        # Check if password is already hashed
        # Werkzeug hashes start with "pbkdf2:sha256:"
        if isinstance(stored_password, bytes):
            stored_password = stored_password.decode('utf-8')
            
        if stored_password.startswith("pbkdf2:sha256:"):
        try:
            hashed_password = generate_password_hash(stored_password)
        except Exception as e:
            print(f"Error hashing password for user {email} (ID: {user_id}): {e}")
            continue
            continue
        
        # This is a plaintext password, convert to hashed password
        print(f"Migrating password for user {email} (ID: {user_id})")
        
        # Generate hashed password
        hashed_password = generate_password_hash(stored_password)
        
        # Update the database
        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (hashed_password, user_id))
        migration_count += 1
    
    # Commit all changes
    conn.commit()
    conn.close()
    
    print(f"\nMigration completed!")
    print(f"Total passwords migrated: {migration_count}")
    print(f"Total users processed: {len(users)}")

if __name__ == '__main__':
    # Run the migration
    migrate_plaintext_to_bcrypt()