"""Main application window for RecursiveLearn."""

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QStackedWidget, QLabel, QMessageBox
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon, QFont, QCursor

from .styles import get_stylesheet
from .mode_selection import ModeSelectionDialog
from .lesson_panel import LessonPanel
from .solver_panel import SolverPanel
from .visualizer_panel import VisualizerPanel
from .practice_panel import PracticePanel
from .settings_panel import SettingsPanel
from ..utils.file_manager import FileManager
from ..data.models import UserProgress, Settings


class MainWindow(QMainWindow):
    """Main application window."""
    
    theme_changed = Signal(str)
    
    def __init__(self):
        super().__init__()
        
        # Initialize file manager
        self.file_manager = FileManager()
        
        # Load settings and progress
        self.settings = self.file_manager.load_settings()
        self.progress = self.file_manager.load_progress()
        
        # User mode (student or instructor)
        self.user_mode = None
        
        # Setup UI
        self.setWindowTitle("RecursiveLearn - Master Recursive Sequences")
        self.setMinimumSize(1200, 800)
        
        # Show mode selection dialog
        self.show_mode_selection()
        
    def show_mode_selection(self):
        """Show mode selection dialog."""
        mode_dialog = ModeSelectionDialog(self)
        mode_dialog.mode_selected.connect(self.set_mode)
        
        if mode_dialog.exec():
            # Mode was selected, continue with UI setup
            self.setup_main_ui()
        else:
            # Dialog was closed without selection, exit app
            self.close()
    
    def set_mode(self, mode: str):
        """Set user mode (student or instructor)."""
        self.user_mode = mode
        
        # Update window title
        if mode == 'instructor':
            self.setWindowTitle("RecursiveLearn - Instructor Mode")
        else:
            self.setWindowTitle("RecursiveLearn - Student Mode")
    
    def setup_main_ui(self):
        """Setup main user interface after mode selection."""
        # Apply theme
        self.apply_theme()
        
        # Create central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Create layout
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create sidebar and main content
        self.create_sidebar()
        self.create_main_content()
        
        # Connect signals
        self.theme_changed.connect(self.on_theme_changed)
        
    def create_sidebar(self):
        """Create navigation sidebar."""
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setMaximumWidth(250)
        sidebar.setStyleSheet("""
            QWidget#sidebar {
                background-color: """ + ('#2D2D2D' if self.settings.theme == 'dark' else '#FFFFFF') + """;
                border-right: 2px solid """ + ('#424242' if self.settings.theme == 'dark' else '#E0E0E0') + """;
            }
        """)
        
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setSpacing(5)
        sidebar_layout.setContentsMargins(10, 20, 10, 10)
        
        # App title
        title = QLabel("📚 RecursiveLearn")
        title_font = QFont("Segoe UI", 20, QFont.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #1565C0; margin-bottom: 5px;")
        sidebar_layout.addWidget(title)
        
        # Mode indicator
        mode_text = "👨‍🏫 Instructor" if self.user_mode == 'instructor' else "🎓 Student"
        mode_color = "#FF9800" if self.user_mode == 'instructor' else "#2196F3"
        mode_label = QLabel(mode_text)
        mode_label.setAlignment(Qt.AlignCenter)
        mode_label.setStyleSheet(f"color: {mode_color}; font-size: 13px; font-weight: 600; margin-bottom: 10px;")
        sidebar_layout.addWidget(mode_label)
        
        # Subtitle
        subtitle = QLabel("Master Recursive Sequences")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #757575; font-size: 12px; margin-bottom: 20px;")
        sidebar_layout.addWidget(subtitle)
        
        # Navigation buttons
        self.nav_buttons = []
        
        nav_items = [
            ("📘 Lessons", "lessons"),
            ("🧮 Solver", "solver"),
            ("📊 Visualizer", "visualizer"),
            ("🧠 Practice", "practice"),
            ("⚙️ Settings", "settings")
        ]
        
        for text, page_id in nav_items:
            btn = QPushButton(text)
            btn.setCheckable(True)
            btn.setMinimumHeight(55)
            btn.setCursor(QCursor(Qt.PointingHandCursor))
            
            # Use lambda with default argument to capture current page_id
            def make_handler(p):
                return lambda: self.navigate_to(p)
            
            btn.clicked.connect(make_handler(page_id))
            
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding-left: 20px;
                    font-size: 15px;
                    font-weight: 500;
                    background-color: transparent;
                    border: none;
                    border-radius: 8px;
                    color: """ + ('#E0E0E0' if self.settings.theme == 'dark' else '#424242') + """;
                }
                QPushButton:hover {
                    background-color: """ + ('#383838' if self.settings.theme == 'dark' else '#E3F2FD') + """;
                }
                QPushButton:checked {
                    background-color: """ + ('#0D47A1' if self.settings.theme == 'dark' else '#2196F3') + """;
                    color: white;
                    font-weight: 700;
                }
            """)
            sidebar_layout.addWidget(btn)
            self.nav_buttons.append((btn, page_id))
        
        # Set first button as checked
        self.nav_buttons[0][0].setChecked(True)
        
        sidebar_layout.addStretch()
        
        # Progress info (only show in student mode)
        if self.user_mode == 'student':
            progress_label = QLabel(f"🏆 Score: {self.progress.total_score}")
            progress_label.setStyleSheet("margin-top: 10px; padding: 10px; font-size: 13px; font-weight: 600;")
            sidebar_layout.addWidget(progress_label)
            
            badges_label = QLabel(f"🎖️ Badges: {len(self.progress.badges)}")
            badges_label.setStyleSheet("padding: 10px; font-size: 13px; font-weight: 600;")
            sidebar_layout.addWidget(badges_label)
        
        self.main_layout.addWidget(sidebar)
        
    def create_main_content(self):
        """Create main content area with stacked pages."""
        self.content_stack = QStackedWidget()
        
        # Create pages
        self.lesson_panel = LessonPanel(self.progress, self.file_manager)
        self.solver_panel = SolverPanel(self.file_manager)
        self.visualizer_panel = VisualizerPanel()
        self.practice_panel = PracticePanel(self.progress, self.file_manager)
        self.settings_panel = SettingsPanel(self.settings, self.file_manager, self.user_mode)
        
        # Add pages to stack
        self.content_stack.addWidget(self.lesson_panel)
        self.content_stack.addWidget(self.solver_panel)
        self.content_stack.addWidget(self.visualizer_panel)
        self.content_stack.addWidget(self.practice_panel)
        self.content_stack.addWidget(self.settings_panel)
        
        # Connect settings panel signals
        self.settings_panel.theme_changed.connect(self.on_theme_changed)
        
        self.main_layout.addWidget(self.content_stack)
        
    def navigate_to(self, page_id: str):
        """Navigate to a specific page."""
        # Update button states
        for btn, pid in self.nav_buttons:
            btn.setChecked(pid == page_id)
        
        # Switch page
        page_index = {
            "lessons": 0,
            "solver": 1,
            "visualizer": 2,
            "practice": 3,
            "settings": 4
        }.get(page_id, 0)
        
        self.content_stack.setCurrentIndex(page_index)
    
    def apply_theme(self):
        """Apply the current theme."""
        stylesheet = get_stylesheet(self.settings.theme)
        self.setStyleSheet(stylesheet)
    
    def on_theme_changed(self, theme: str):
        """Handle theme change."""
        self.settings.theme = theme
        self.apply_theme()
        
        # Update sidebar colors
        self.central_widget.setParent(None)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.create_sidebar()
        self.create_main_content()
        
        # Navigate back to current page
        current_index = 0
        for i, (btn, _) in enumerate(self.nav_buttons):
            if btn.isChecked():
                current_index = i
                break
        self.content_stack.setCurrentIndex(current_index)
        
    def closeEvent(self, event):
        """Handle window close event."""
        # Save progress and settings
        self.file_manager.save_progress(self.progress)
        self.file_manager.save_settings(self.settings)
        
        event.accept()
