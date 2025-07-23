##  Change 1: Updated to an Easier Setup Process for Convenience

###  Option 1: Automated Setup

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

###  Option 2: Manual Setup

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

---

##  Change 2: Added a Migration Script for Password Hashing

Migrated legacy plaintext passwords to hashed ones using `werkzeug`.

### 🧪 Migration Script

```bash
# Migrate plaintext passwords to hashed passwords using werkzeug
python migrations/migrate_passwords.py
```

---

##  Change 3: Separation of Concerns

All logic was previously jammed into a single file (yikes). Now, the project structure is modular and clean:

```
Current File Hierarchy:
├── app.py                 # Main Flask application
├── config/               # Configuration management
├── core/                 # Dependency injection
├── db/                   # Database layer
├── models/               # Data models  
├── repositories/         # Repository pattern
├── services/             # Business logic
├── routes/               # API endpoints
├── utils/                # Utilities & validators
├── tests/                # Complete test suite (44 tests)
├── requirements.txt      # Dependencies
├── README.md             # Documentation
└── .env.example          # Environment template
```

---

##  Change 4: Added Validators

No validation existed earlier for `name`, `email`, and `password` fields. Now added custom validators placed in the `utils` directory.

---

##  Change 5: Major Security Concern – Leaking Passwords!

Fixed the `GET /users` endpoint that was irresponsibly returning user passwords in the response. Huge fix.

---

##  Change 6: SQL Injection Prevention

Implemented parameterized queries (`?` placeholders) to sanitize all user inputs, preventing SQL injection vulnerabilities.

---

##  Change 7: JWT Authentication Added

For better security, JWT-based authentication has been implemented for the login endpoint. Tokens are returned upon successful login and required for protected routes.

---

##  Change 8: Added Testing

A complete test suite has been added using `pytest`. Includes:

- Unit & integration tests  
- Security checks  
- Coverage for user creation, updates, deletion, and login  
- 44 tests in total  
- Isolated testing environment

---

##  Change 9: Rate Limiting

Implemented rate limiting to prevent brute-force attacks:

- Login endpoint: 5 requests/min  
- Entire app: 100 requests/hour

Helps ensure fair usage and protects against abuse.

---

##  Change 10: Input Sanitization

Sanitized all user inputs (email, name, password) to defend against XSS and other injection attacks. Validations added before data processing.