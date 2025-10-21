"""
RecursiveLearn - Main Entry Point

An offline Windows application for solving and visualizing recursive sequences.
Designed for Discrete Mathematics students.
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from src.ui.main_window import MainWindow


def main():
    """Main application entry point."""
    
    # Create application
    app = QApplication(sys.argv)
    
    # Set application metadata
    app.setApplicationName("RecursiveLearn")
    app.setApplicationDisplayName("RecursiveLearn - Master Recursive Sequences")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("RecursiveLearn")
    app.setOrganizationDomain("recursivelearn.edu")
    
    # Set default font
    default_font = QFont("Segoe UI", 11)
    app.setFont(default_font)
    
    # Enable high DPI scaling
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Run application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
