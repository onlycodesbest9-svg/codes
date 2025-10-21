"""Settings panel for RecursiveLearn."""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QGroupBox, QComboBox, QSpinBox, QLineEdit, QCheckBox,
    QMessageBox, QInputDialog
)
from PySide6.QtCore import Qt, Signal

from ..data.models import Settings
from ..utils.file_manager import FileManager


class SettingsPanel(QWidget):
    """Panel for application settings."""
    
    theme_changed = Signal(str)
    
    def __init__(self, settings: Settings, file_manager: FileManager):
        super().__init__()
        
        self.settings = settings
        self.file_manager = file_manager
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("⚙️ Settings")
        title.setObjectName("titleLabel")
        layout.addWidget(title)
        
        # Appearance group
        appearance_group = QGroupBox("Appearance")
        appearance_layout = QVBoxLayout(appearance_group)
        
        # Theme selection
        theme_layout = QHBoxLayout()
        theme_label = QLabel("Theme:")
        theme_label.setMinimumWidth(150)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark"])
        self.theme_combo.setCurrentText(self.settings.theme.capitalize())
        self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_combo)
        theme_layout.addStretch()
        appearance_layout.addLayout(theme_layout)
        
        # Font size
        font_layout = QHBoxLayout()
        font_label = QLabel("Font Size:")
        font_label.setMinimumWidth(150)
        self.font_spin = QSpinBox()
        self.font_spin.setMinimum(10)
        self.font_spin.setMaximum(20)
        self.font_spin.setValue(self.settings.font_size)
        font_layout.addWidget(font_label)
        font_layout.addWidget(self.font_spin)
        font_layout.addStretch()
        appearance_layout.addLayout(font_layout)
        
        # Graph color scheme
        graph_layout = QHBoxLayout()
        graph_label = QLabel("Graph Color Scheme:")
        graph_label.setMinimumWidth(150)
        self.graph_combo = QComboBox()
        self.graph_combo.addItems(["Default", "Pastel", "Vibrant", "Monochrome"])
        self.graph_combo.setCurrentText(self.settings.graph_color_scheme.capitalize())
        graph_layout.addWidget(graph_label)
        graph_layout.addWidget(self.graph_combo)
        graph_layout.addStretch()
        appearance_layout.addLayout(graph_layout)
        
        layout.addWidget(appearance_group)
        
        # Solver group
        solver_group = QGroupBox("Solver Options")
        solver_layout = QVBoxLayout(solver_group)
        
        self.show_steps_cb = QCheckBox("Show step-by-step solutions by default")
        self.show_steps_cb.setChecked(self.settings.show_step_by_step)
        solver_layout.addWidget(self.show_steps_cb)
        
        self.auto_save_cb = QCheckBox("Auto-save solutions")
        self.auto_save_cb.setChecked(self.settings.auto_save)
        solver_layout.addWidget(self.auto_save_cb)
        
        layout.addWidget(solver_group)
        
        # Instructor mode group
        instructor_group = QGroupBox("Instructor Mode")
        instructor_layout = QVBoxLayout(instructor_group)
        
        pin_layout = QHBoxLayout()
        pin_label = QLabel("PIN Code:")
        pin_label.setMinimumWidth(150)
        self.pin_input = QLineEdit()
        self.pin_input.setEchoMode(QLineEdit.Password)
        self.pin_input.setText(self.settings.instructor_pin)
        self.pin_input.setMaximumWidth(200)
        pin_layout.addWidget(pin_label)
        pin_layout.addWidget(self.pin_input)
        pin_layout.addStretch()
        instructor_layout.addLayout(pin_layout)
        
        access_btn = QPushButton("🔓 Access Instructor Mode")
        access_btn.clicked.connect(self.access_instructor_mode)
        instructor_layout.addWidget(access_btn)
        
        layout.addWidget(instructor_group)
        
        # Data management group
        data_group = QGroupBox("Data Management")
        data_layout = QVBoxLayout(data_group)
        
        location_label = QLabel(f"Data location: {self.file_manager.base_dir}")
        location_label.setWordWrap(True)
        location_label.setStyleSheet("font-size: 11px; color: #757575;")
        data_layout.addWidget(location_label)
        
        data_btn_layout = QHBoxLayout()
        
        open_folder_btn = QPushButton("📁 Open Data Folder")
        open_folder_btn.clicked.connect(self.open_data_folder)
        data_btn_layout.addWidget(open_folder_btn)
        
        reset_btn = QPushButton("🔄 Reset Progress")
        reset_btn.setObjectName("secondaryButton")
        reset_btn.clicked.connect(self.reset_progress)
        data_btn_layout.addWidget(reset_btn)
        
        data_btn_layout.addStretch()
        data_layout.addLayout(data_btn_layout)
        
        layout.addWidget(data_group)
        
        # Save button
        layout.addStretch()
        
        save_btn = QPushButton("💾 Save Settings")
        save_btn.setMinimumHeight(45)
        save_btn.clicked.connect(self.save_settings)
        layout.addWidget(save_btn)
        
        # About
        about_label = QLabel(
            "<center>"
            "<b>RecursiveLearn v1.0</b><br>"
            "Educational tool for Discrete Mathematics<br>"
            "Built with Python & PySide6"
            "</center>"
        )
        about_label.setStyleSheet("margin-top: 20px; color: #757575; font-size: 11px;")
        layout.addWidget(about_label)
        
    def on_theme_changed(self, theme: str):
        """Handle theme change."""
        theme_lower = theme.lower()
        self.settings.theme = theme_lower
        self.theme_changed.emit(theme_lower)
        
    def save_settings(self):
        """Save current settings."""
        self.settings.font_size = self.font_spin.value()
        self.settings.graph_color_scheme = self.graph_combo.currentText().lower()
        self.settings.show_step_by_step = self.show_steps_cb.isChecked()
        self.settings.auto_save = self.auto_save_cb.isChecked()
        self.settings.instructor_pin = self.pin_input.text()
        
        self.file_manager.save_settings(self.settings)
        
        QMessageBox.information(self, "Saved", "Settings saved successfully!")
        
    def access_instructor_mode(self):
        """Access instructor mode with PIN."""
        pin, ok = QInputDialog.getText(
            self,
            "Instructor Mode",
            "Enter PIN:",
            QLineEdit.Password
        )
        
        if ok:
            if pin == self.settings.instructor_pin:
                QMessageBox.information(
                    self,
                    "Access Granted",
                    "Welcome to Instructor Mode!\n\n"
                    "You can now:\n"
                    "• Add custom exercises\n"
                    "• View student progress\n"
                    "• Manage lesson content"
                )
            else:
                QMessageBox.warning(self, "Access Denied", "Incorrect PIN.")
                
    def open_data_folder(self):
        """Open the data folder in file explorer."""
        import os
        import platform
        
        path = str(self.file_manager.base_dir)
        
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":  # macOS
            os.system(f'open "{path}"')
        else:  # Linux
            os.system(f'xdg-open "{path}"')
            
    def reset_progress(self):
        """Reset user progress."""
        reply = QMessageBox.question(
            self,
            "Confirm Reset",
            "Are you sure you want to reset all progress?\n\n"
            "This will delete:\n"
            "• Completed lessons\n"
            "• Exercise scores\n"
            "• Earned badges\n\n"
            "This action cannot be undone!",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            from ..data.models import UserProgress
            new_progress = UserProgress()
            self.file_manager.save_progress(new_progress)
            
            QMessageBox.information(self, "Reset Complete", "Progress has been reset.")
