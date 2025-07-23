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