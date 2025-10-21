"""Mode selection screen for RecursiveLearn."""

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QLineEdit, QMessageBox, QWidget, QFrame
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


class ModeSelectionDialog(QDialog):
    """Dialog for selecting Student or Instructor mode."""
    
    mode_selected = Signal(str, str)  # Emits (mode, user_id/pin)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("RecursiveLearn - Welcome")
        self.setModal(True)
        self.setMinimumSize(700, 650)
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("Welcome to RecursiveLearn")
        title_font = QFont("Segoe UI", 28, QFont.Bold)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #1565C0; margin-bottom: 5px;")
        title.setWordWrap(True)
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Master Recursive Sequences")
        subtitle_font = QFont("Segoe UI", 14)
        subtitle.setFont(subtitle_font)
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #757575; margin-bottom: 15px;")
        layout.addWidget(subtitle)
        
        # Description
        desc = QLabel("Choose your mode to get started:")
        desc_font = QFont("Segoe UI", 13, QFont.Bold)
        desc.setFont(desc_font)
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet("color: #424242; margin-bottom: 5px;")
        layout.addWidget(desc)
        
        layout.addSpacing(10)
        
        # Student Mode Button
        student_container = QFrame()
        student_container.setFrameShape(QFrame.StyledPanel)
        student_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 3px solid #E0E0E0;
                border-radius: 12px;
                padding: 5px;
            }
            QFrame:hover {
                border: 3px solid #2196F3;
                background-color: #F5F9FF;
            }
        """)
        student_layout = QVBoxLayout(student_container)
        student_layout.setContentsMargins(25, 20, 25, 20)
        student_layout.setSpacing(12)
        
        student_icon = QLabel("🎓")
        student_icon.setAlignment(Qt.AlignCenter)
        student_icon.setStyleSheet("font-size: 48px; border: none; background: transparent;")
        student_layout.addWidget(student_icon)
        
        student_title = QLabel("Student Mode")
        student_title_font = QFont("Segoe UI", 16, QFont.Bold)
        student_title.setFont(student_title_font)
        student_title.setAlignment(Qt.AlignCenter)
        student_title.setStyleSheet("color: #212121; border: none; background: transparent;")
        student_layout.addWidget(student_title)
        
        student_desc = QLabel("• Learn interactive lessons\n• Solve practice exercises\n• Take quizzes\n• Track your progress")
        student_desc_font = QFont("Segoe UI", 12)
        student_desc.setFont(student_desc_font)
        student_desc.setAlignment(Qt.AlignCenter)
        student_desc.setWordWrap(True)
        student_desc.setStyleSheet("color: #616161; border: none; background: transparent;")
        student_layout.addWidget(student_desc)
        
        student_btn = QPushButton("Continue as Student")
        student_btn.setMinimumHeight(45)
        student_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 15px;
                font-weight: 600;
                padding: 10px;
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
        instructor_container = QFrame()
        instructor_container.setFrameShape(QFrame.StyledPanel)
        instructor_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 3px solid #E0E0E0;
                border-radius: 12px;
                padding: 5px;
            }
            QFrame:hover {
                border: 3px solid #FF9800;
                background-color: #FFF8F0;
            }
        """)
        instructor_layout = QVBoxLayout(instructor_container)
        instructor_layout.setContentsMargins(25, 20, 25, 20)
        instructor_layout.setSpacing(12)
        
        instructor_icon = QLabel("👨‍🏫")
        instructor_icon.setAlignment(Qt.AlignCenter)
        instructor_icon.setStyleSheet("font-size: 48px; border: none; background: transparent;")
        instructor_layout.addWidget(instructor_icon)
        
        instructor_title = QLabel("Instructor Mode")
        instructor_title_font = QFont("Segoe UI", 16, QFont.Bold)
        instructor_title.setFont(instructor_title_font)
        instructor_title.setAlignment(Qt.AlignCenter)
        instructor_title.setStyleSheet("color: #212121; border: none; background: transparent;")
        instructor_layout.addWidget(instructor_title)
        
        instructor_desc = QLabel("• Upload lesson PDFs/files\n• Create quizzes & exercises\n• View student records\n• Manage student progress")
        instructor_desc_font = QFont("Segoe UI", 12)
        instructor_desc.setFont(instructor_desc_font)
        instructor_desc.setAlignment(Qt.AlignCenter)
        instructor_desc.setWordWrap(True)
        instructor_desc.setStyleSheet("color: #616161; border: none; background: transparent;")
        instructor_layout.addWidget(instructor_desc)
        
        # PIN info highlight
        pin_info = QLabel("🔐 Set your PIN on first login")
        pin_info_font = QFont("Segoe UI", 11, QFont.Bold)
        pin_info.setFont(pin_info_font)
        pin_info.setAlignment(Qt.AlignCenter)
        pin_info.setStyleSheet("""
            color: #FF6F00;
            background-color: #FFF3E0;
            border: 2px solid #FFB74D;
            border-radius: 6px;
            padding: 8px;
        """)
        instructor_layout.addWidget(pin_info)
        
        instructor_btn = QPushButton("Continue as Instructor")
        instructor_btn.setMinimumHeight(45)
        instructor_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 15px;
                font-weight: 600;
                padding: 10px;
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
        """Select student mode with student ID."""
        # Create student ID dialog
        from PySide6.QtWidgets import QInputDialog
        
        student_id, ok = QInputDialog.getText(
            self,
            "Student Login",
            "Enter your Student ID:\n(e.g., STU001, STU002, etc.)",
            QLineEdit.Normal,
            ""
        )
        
        if ok and student_id.strip():
            self.mode_selected.emit('student', student_id.strip())
            self.accept()
        elif ok:
            QMessageBox.warning(
                self,
                "Student ID Required",
                "Please enter your Student ID to continue."
            )
        
    def select_instructor_mode(self):
        """Select instructor mode with PIN setup or verification."""
        from ..utils.file_manager import FileManager
        
        # Load settings to get PIN
        file_manager = FileManager()
        settings = file_manager.load_settings()
        
        # Check if this is first time (default PIN)
        is_first_time = settings.instructor_pin == "1234"
        
        # Create PIN dialog
        pin_dialog = QDialog(self)
        if is_first_time:
            pin_dialog.setWindowTitle("Instructor Mode - Setup Your PIN")
        else:
            pin_dialog.setWindowTitle("Instructor Mode - Enter PIN")
        pin_dialog.setModal(True)
        pin_dialog.setMinimumSize(450, 280)
        
        pin_layout = QVBoxLayout(pin_dialog)
        pin_layout.setContentsMargins(30, 30, 30, 30)
        pin_layout.setSpacing(15)
        
        # Title
        if is_first_time:
            pin_title = QLabel("🔐 Create Your Instructor PIN")
            info_text = "This is your first time. Please create a secure PIN\n(4-8 digits recommended)"
        else:
            pin_title = QLabel("🔐 Enter Your Instructor PIN")
            info_text = "Enter your PIN to access Instructor Mode"
        
        pin_title_font = QFont("Segoe UI", 15, QFont.Bold)
        pin_title.setFont(pin_title_font)
        pin_title.setAlignment(Qt.AlignCenter)
        pin_title.setStyleSheet("color: #FF6F00; margin-bottom: 5px;")
        pin_layout.addWidget(pin_title)
        
        # Info label
        info_label = QLabel(info_text)
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setWordWrap(True)
        info_label.setStyleSheet("color: #616161; font-size: 12px; margin-bottom: 10px;")
        pin_layout.addWidget(info_label)
        
        # PIN input
        pin_input = QLineEdit()
        pin_input.setEchoMode(QLineEdit.Password)
        if is_first_time:
            pin_input.setPlaceholderText("Create your PIN (e.g., 1234, 5678)")
        else:
            pin_input.setPlaceholderText("Enter your PIN")
        pin_input.setMinimumHeight(50)
        pin_input.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                padding: 12px;
                border: 3px solid #FFB74D;
                border-radius: 8px;
                background-color: #FFF8F0;
            }
            QLineEdit:focus {
                border: 3px solid #FF9800;
                background-color: white;
            }
        """)
        pin_layout.addWidget(pin_input)
        
        # Confirm PIN input (only for first time)
        confirm_input = None
        if is_first_time:
            confirm_input = QLineEdit()
            confirm_input.setEchoMode(QLineEdit.Password)
            confirm_input.setPlaceholderText("Confirm your PIN")
            confirm_input.setMinimumHeight(50)
            confirm_input.setStyleSheet("""
                QLineEdit {
                    font-size: 18px;
                    padding: 12px;
                    border: 3px solid #FFB74D;
                    border-radius: 8px;
                    background-color: #FFF8F0;
                }
                QLineEdit:focus {
                    border: 3px solid #FF9800;
                    background-color: white;
                }
            """)
            pin_layout.addWidget(confirm_input)
        
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
        
        if is_first_time:
            verify_btn = QPushButton("✓ Create PIN & Continue")
        else:
            verify_btn = QPushButton("✓ Verify & Continue")
        verify_btn.setMinimumHeight(45)
        verify_btn.setMinimumWidth(120)
        verify_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 15px;
                font-weight: 700;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
        """)
        
        def verify_pin():
            entered_pin = pin_input.text().strip()
            
            if is_first_time:
                # Setup new PIN
                confirm_pin = confirm_input.text().strip() if confirm_input else ""
                
                if len(entered_pin) < 4:
                    QMessageBox.warning(
                        pin_dialog,
                        "PIN Too Short",
                        "Please create a PIN with at least 4 characters.",
                        QMessageBox.Ok
                    )
                    return
                
                if entered_pin != confirm_pin:
                    QMessageBox.warning(
                        pin_dialog,
                        "PINs Don't Match",
                        "The PINs you entered don't match.\n\nPlease try again.",
                        QMessageBox.Ok
                    )
                    pin_input.clear()
                    if confirm_input:
                        confirm_input.clear()
                    pin_input.setFocus()
                    return
                
                # Save new PIN
                settings.instructor_pin = entered_pin
                file_manager.save_settings(settings)
                
                QMessageBox.information(
                    pin_dialog,
                    "PIN Created Successfully",
                    f"Your instructor PIN has been set!\n\nPIN: {entered_pin}\n\n⚠️ Please remember this PIN for future logins.",
                    QMessageBox.Ok
                )
                
                pin_dialog.accept()
                self.mode_selected.emit('instructor', entered_pin)
                self.accept()
            else:
                # Verify existing PIN
                if entered_pin == settings.instructor_pin:
                    pin_dialog.accept()
                    self.mode_selected.emit('instructor', entered_pin)
                    self.accept()
                else:
                    QMessageBox.warning(
                        pin_dialog,
                        "Incorrect PIN",
                        "The PIN you entered is incorrect.\n\nPlease try again.",
                        QMessageBox.Ok
                    )
                    pin_input.clear()
                    pin_input.setFocus()
        
        verify_btn.clicked.connect(verify_pin)
        pin_input.returnPressed.connect(verify_pin)
        if confirm_input:
            confirm_input.returnPressed.connect(verify_pin)
        
        btn_layout.addWidget(cancel_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(verify_btn)
        
        pin_layout.addLayout(btn_layout)
        
        # Show PIN dialog
        pin_input.setFocus()
        pin_dialog.exec()
