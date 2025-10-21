@echo off
REM RecursiveLearn Installation Script for Windows

echo ========================================
echo RecursiveLearn Installation
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org
    pause
    exit /b 1
)

echo Python found!
echo.

REM Create virtual environment (optional but recommended)
echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Warning: Could not create virtual environment
    echo Proceeding with global installation...
) else (
    echo Virtual environment created successfully!
    call venv\Scripts\activate.bat
)

echo.
echo Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo To run RecursiveLearn:
echo   1. Double-click run.bat
echo   OR
echo   2. Run: python main.py
echo.
pause
