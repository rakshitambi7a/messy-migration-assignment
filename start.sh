#!/bin/bash

# Quick start script for User Management API
# This script activates the virtual environment and starts the application

set -e

if [ ! -d "venv" ]; then
    echo " Virtual environment not found. Please run ./setup.sh first."
    exit 1
fi

echo " Starting User Management API..."
source venv/bin/activate
python app.py
