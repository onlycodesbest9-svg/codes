@echo off
REM RecursiveLearn Launcher for Windows

REM Check if virtual environment exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Run the application
python main.py

REM Keep window open if there's an error
if errorlevel 1 pause
