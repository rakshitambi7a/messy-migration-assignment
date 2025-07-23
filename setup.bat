@echo off
REM Setup script for User Management API (Windows)
REM This script creates a virtual environment and installs dependencies

echo 🚀 Setting up User Management API...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH. Please install Python 3.8+ and try again.
    pause
    exit /b 1
)

echo ✅ Python detected

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
) else (
    echo 📦 Virtual environment already exists
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Initialize database
echo 🗄️  Initializing database...
python init_db.py

echo.
echo ✅ Setup complete!
echo.
echo To start the application:
echo   1. Activate the virtual environment: venv\Scripts\activate.bat
echo   2. Run the application: python app.py
echo.
echo To deactivate the virtual environment later, run: deactivate

pause
