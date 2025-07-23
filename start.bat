@echo off
REM Quick start script for User Management API (Windows)
REM This script activates the virtual environment and starts the application

if not exist "venv" (
    echo ❌ Virtual environment not found. Please run setup.bat first.
    pause
    exit /b 1
)

echo 🚀 Starting User Management API...
call venv\Scripts\activate.bat
python app.py
