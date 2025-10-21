#!/bin/bash
# RecursiveLearn Launcher for Linux/Mac

# Check if virtual environment exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the application
python3 main.py
