"""Mode selection screen for RecursiveLearn."""

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QLineEdit, QMessageBox, QWidget
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


class ModeSelectionDialog(QDialog):
    """Dialog for selecting Student or Instructor mode."""
    
    mode_selected = Signal(str)  # Emits 'student' or 'instructor'
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("RecursiveLearn - Welcome")
        self.setModal(True)
        self.setMinimumSize(600, 500)
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)
        
        # Title
        title = QLabel("Welcome to RecursiveLearn")
        title_font = QFont("Segoe UI", 32, QFont.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #1565C0; margin-bottom: 10px;")
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Master Recursive Sequences")
        subtitle_font = QFont("Segoe UI", 16)
        subtitle.setFont(subtitle_font)
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #757575; margin-bottom: 20px;")
        layout.addWidget(subtitle)
        
        # Description
        desc = QLabel("Choose your mode to get started:")
        desc_font = QFont("Segoe UI", 14)
        desc.setFont(desc_font)
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet("color: #424242; margin-bottom: 10px;")
        layout.addWidget(desc)
        
        layout.addSpacing(20)
        
        # Student Mode Button
        student_container = QWidget()
        student_container.setStyleSheet("""
            QWidget {
                background-color: white;
                border: 2px solid #E0E0E0;
                border-radius: 12px;
            }
            QWidget:hover {
                border: 2px solid #2196F3;
                background-color: #F5F9FF;
            }
        """)
        student_layout = QVBoxLayout(student_container)
        student_layout.setContentsMargins(30, 30, 30, 30)
        student_layout.setSpacing(15)
        
        student_icon = QLabel("🎓")
        student_icon.setAlignment(Qt.AlignCenter)
        student_icon.setStyleSheet("font-size: 64px; border: none; background: transparent;")
        student_layout.addWidget(student_icon)
        
        student_title = QLabel("Student Mode")
        student_title_font = QFont("Segoe UI", 18, QFont.Bold)
        student_title.setFont(student_title_font)
        student_title.setAlignment(Qt.AlignCenter)
        student_title.setStyleSheet("color: #212121; border: none; background: transparent;")
        student_layout.addWidget(student_title)
        
        student_desc = QLabel("• Learn interactive lessons\n• Solve practice exercises\n• Visualize sequences\n• Track your progress")
        student_desc_font = QFont("Segoe UI", 13)
        student_desc.setFont(student_desc_font)
        student_desc.setAlignment(Qt.AlignCenter)
        student_desc.setStyleSheet("color: #616161; border: none; background: transparent; line-height: 1.8;")
        student_layout.addWidget(student_desc)
        
        student_btn = QPushButton("Start Learning")
        student_btn.setMinimumHeight(50)
        student_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: 600;
                padding: 12px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #0D47A1;
            }
        """)
        student_btn.clicked.connect(self.select_student_mode)
        student_layout.addWidget(student_btn)
        
        layout.addWidget(student_container)
        
        # Instructor Mode Button
        instructor_container = QWidget()
        instructor_container.setStyleSheet("""
            QWidget {
                background-color: white;
                border: 2px solid #E0E0E0;
                border-radius: 12px;
            }
            QWidget:hover {
                border: 2px solid #FF9800;
                background-color: #FFF8F0;
            }
        """)
        instructor_layout = QVBoxLayout(instructor_container)
        instructor_layout.setContentsMargins(30, 30, 30, 30)
        instructor_layout.setSpacing(15)
        
        instructor_icon = QLabel("👨‍🏫")
        instructor_icon.setAlignment(Qt.AlignCenter)
        instructor_icon.setStyleSheet("font-size: 64px; border: none; background: transparent;")
        instructor_layout.addWidget(instructor_icon)
        
        instructor_title = QLabel("Instructor Mode")
        instructor_title_font = QFont("Segoe UI", 18, QFont.Bold)
        instructor_title.setFont(instructor_title_font)
        instructor_title.setAlignment(Qt.AlignCenter)
        instructor_title.setStyleSheet("color: #212121; border: none; background: transparent;")
        instructor_layout.addWidget(instructor_title)
        
        instructor_desc = QLabel("• Manage student progress\n• Create custom exercises\n• View analytics\n• Customize content")
        instructor_desc_font = QFont("Segoe UI", 13)
        instructor_desc.setFont(instructor_desc_font)
        instructor_desc.setAlignment(Qt.AlignCenter)
        instructor_desc.setStyleSheet("color: #616161; border: none; background: transparent; line-height: 1.8;")
        instructor_layout.addWidget(instructor_desc)
        
        instructor_btn = QPushButton("Enter with PIN")
        instructor_btn.setMinimumHeight(50)
        instructor_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: 600;
                padding: 12px;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
            QPushButton:pressed {
                background-color: #E65100;
            }
        """)
        instructor_btn.clicked.connect(self.select_instructor_mode)
        instructor_layout.addWidget(instructor_btn)
        
        layout.addWidget(instructor_container)
        
        layout.addStretch()
        
    def select_student_mode(self):
        """Select student mode."""
        self.mode_selected.emit('student')
        self.accept()
        
    def select_instructor_mode(self):
        """Select instructor mode with PIN verification."""
        from ..utils.file_manager import FileManager
        
        # Load settings to get PIN
        file_manager = FileManager()
        settings = file_manager.load_settings()
        
        # Create PIN dialog
        pin_dialog = QDialog(self)
        pin_dialog.setWindowTitle("Instructor Mode - PIN Required")
        pin_dialog.setModal(True)
        pin_dialog.setMinimumSize(400, 200)
        
        pin_layout = QVBoxLayout(pin_dialog)
        pin_layout.setContentsMargins(30, 30, 30, 30)
        pin_layout.setSpacing(20)
        
        # Title
        pin_title = QLabel("Enter Instructor PIN")
        pin_title_font = QFont("Segoe UI", 16, QFont.Bold)
        pin_title.setFont(pin_title_font)
        pin_title.setAlignment(Qt.AlignCenter)
        pin_title.setStyleSheet("color: #212121;")
        pin_layout.addWidget(pin_title)
        
        # PIN input
        pin_input = QLineEdit()
        pin_input.setEchoMode(QLineEdit.Password)
        pin_input.setPlaceholderText("Enter PIN (default: 1234)")
        pin_input.setMinimumHeight(45)
        pin_input.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                padding: 10px;
                border: 2px solid #BDBDBD;
                border-radius: 6px;
            }
            QLineEdit:focus {
                border: 2px solid #FF9800;
            }
        """)
        pin_layout.addWidget(pin_input)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setMinimumHeight(40)
        cancel_btn.setMinimumWidth(100)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #EEEEEE;
                color: #212121;
                border: 2px solid #BDBDBD;
                border-radius: 6px;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
        """)
        cancel_btn.clicked.connect(pin_dialog.reject)
        
        verify_btn = QPushButton("Verify PIN")
        verify_btn.setMinimumHeight(40)
        verify_btn.setMinimumWidth(100)
        verify_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
        """)
        
        def verify_pin():
            entered_pin = pin_input.text()
            if entered_pin == settings.instructor_pin:
                pin_dialog.accept()
                self.mode_selected.emit('instructor')
                self.accept()
            else:
                QMessageBox.warning(
                    pin_dialog,
                    "Incorrect PIN",
                    "The PIN you entered is incorrect.\n\nPlease try again or contact your administrator.",
                    QMessageBox.Ok
                )
                pin_input.clear()
                pin_input.setFocus()
        
        verify_btn.clicked.connect(verify_pin)
        pin_input.returnPressed.connect(verify_pin)
        
        btn_layout.addWidget(cancel_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(verify_btn)
        
        pin_layout.addLayout(btn_layout)
        
        # Show PIN dialog
        pin_input.setFocus()
        pin_dialog.exec()
