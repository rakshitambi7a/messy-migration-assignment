## Change 1: Updated to an easier setup process for convenience
#### Option 1: Automated Setup
```bash
# Clone/download this repository
# Navigate to the assignment directory
cd messy-migration

# For Unix/Linux/macOS:
./setup.sh

# For Windows:
setup.bat

# Or using Make (if available):
make setup

# Start the application
# On Unix/Linux/macOS:
source venv/bin/activate && python app.py

# On Windows:
venv\Scripts\activate && python app.py

# The API will be available at http://localhost:5000
```
#### Option 2: Manual Setup
```bash
# Clone/download this repository
# Navigate to the assignment directory
cd messy-migration

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Unix/Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```
## Change 2: Added a migration script for password hashing using werkzeug for legacy plaintext passwords
### Migration Script
```bash
# Migrate plaintext passwords to hashed passwords using werkzeug
python migrations/migrate_passwords.py
```
## Change 3: Seperation of Concerns: 
Since all the logic was in one giant file. A nightmare for code organization. Seperated the routes, services and db connection logic into their respective files/directories
``` The current files heirarchy:

```
## Change 4: Added Validators:
There was no validation in place for the name, email and password fields, created validators and added to the utils directory.

## Change 5: Major Security Concern: The GET /users endpoint was leaking user passwords!
The GET /users endpoint was returning user password along with the other details, fixed.

## Change 6: SQL injection Prevention
This code prevents SQL injection by using parameterized queries with placeholders (?) and passing values separately in tuples, which automatically escapes and sanitizes user input before database execution.

## Change 7: Added JWT Authentication for login
For "production-ready purposes", since the login endpoint was not secure, added JWT authentication to the login endpoint. The JWT token is returned in the response and should be used for subsequent requests that require authentication.

## Change 8: Added Testing
Added a test suite using pytest to ensure the application works as expected. The tests cover user creation, retrieval, updating, and deletion, as well as login functionality. Added the testing environment as well.

