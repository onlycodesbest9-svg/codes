"""Lesson panel for RecursiveLearn."""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QListWidget, QTextBrowser, QScrollArea, QMessageBox
)
from PySide6.QtCore import Qt

from ..data.lessons import get_all_lessons
from ..data.models import UserProgress
from ..utils.file_manager import FileManager


class LessonPanel(QWidget):
    """Panel for displaying interactive lessons."""
    
    def __init__(self, progress: UserProgress, file_manager: FileManager):
        super().__init__()
        
        self.progress = progress
        self.file_manager = file_manager
        self.lessons = get_all_lessons()
        self.current_lesson = None
        self.current_section = 0
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface."""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # Left side - Lesson list
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_widget.setMaximumWidth(300)
        
        title = QLabel("📚 Lesson Modules")
        title.setObjectName("sectionTitle")
        left_layout.addWidget(title)
        
        self.lesson_list = QListWidget()
        self.lesson_list.itemClicked.connect(self.on_lesson_selected)
        
        for lesson in self.lessons:
            completed_mark = "✓ " if lesson.id in self.progress.lessons_completed else ""
            self.lesson_list.addItem(f"{completed_mark}Lesson {lesson.id}: {lesson.title}")
        
        left_layout.addWidget(self.lesson_list)
        
        layout.addWidget(left_widget)
        
        # Right side - Lesson content
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
        # Lesson title
        self.lesson_title = QLabel("Select a lesson to begin")
        self.lesson_title.setObjectName("titleLabel")
        right_layout.addWidget(self.lesson_title)
        
        # Lesson description
        self.lesson_desc = QLabel("")
        self.lesson_desc.setWordWrap(True)
        self.lesson_desc.setStyleSheet("margin-bottom: 15px; font-size: 13px; color: #757575;")
        right_layout.addWidget(self.lesson_desc)
        
        # Content browser
        self.content_browser = QTextBrowser()
        self.content_browser.setOpenExternalLinks(False)
        self.content_browser.setStyleSheet("padding: 15px;")
        right_layout.addWidget(self.content_browser)
        
        # Navigation buttons
        nav_layout = QHBoxLayout()
        
        self.prev_btn = QPushButton("⬅️ Previous")
        self.prev_btn.clicked.connect(self.previous_section)
        self.prev_btn.setEnabled(False)
        
        self.next_btn = QPushButton("Next ➡️")
        self.next_btn.clicked.connect(self.next_section)
        self.next_btn.setEnabled(False)
        
        self.complete_btn = QPushButton("✓ Mark Lesson Complete")
        self.complete_btn.clicked.connect(self.mark_complete)
        self.complete_btn.setEnabled(False)
        
        nav_layout.addWidget(self.prev_btn)
        nav_layout.addStretch()
        nav_layout.addWidget(self.complete_btn)
        nav_layout.addWidget(self.next_btn)
        
        right_layout.addLayout(nav_layout)
        
        layout.addWidget(right_widget)
        
    def on_lesson_selected(self, item):
        """Handle lesson selection."""
        index = self.lesson_list.currentRow()
        self.current_lesson = self.lessons[index]
        self.current_section = 0
        
        self.lesson_title.setText(f"Lesson {self.current_lesson.id}: {self.current_lesson.title}")
        self.lesson_desc.setText(self.current_lesson.description)
        
        self.display_section()
        
    def display_section(self):
        """Display the current section."""
        if not self.current_lesson or self.current_section >= len(self.current_lesson.sections):
            return
        
        section = self.current_lesson.sections[self.current_section]
        
        # Build HTML content
        html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; }}
                h3 {{ color: #2196F3; margin-top: 20px; }}
                h4 {{ color: #424242; margin-top: 15px; }}
                ul, ol {{ margin-left: 20px; }}
                li {{ margin: 8px 0; }}
                p {{ margin: 10px 0; }}
                b {{ color: #1976D2; }}
            </style>
        </head>
        <body>
            <h2>{section.title}</h2>
            {section.content}
        </body>
        </html>
        """
        
        self.content_browser.setHtml(html)
        
        # Update navigation buttons
        self.prev_btn.setEnabled(self.current_section > 0)
        self.next_btn.setEnabled(self.current_section < len(self.current_lesson.sections) - 1)
        
        # Enable complete button on last section
        is_last = self.current_section == len(self.current_lesson.sections) - 1
        self.complete_btn.setEnabled(is_last)
        
    def previous_section(self):
        """Go to previous section."""
        if self.current_section > 0:
            self.current_section -= 1
            self.display_section()
            
    def next_section(self):
        """Go to next section."""
        if self.current_section < len(self.current_lesson.sections) - 1:
            self.current_section += 1
            self.display_section()
            
    def mark_complete(self):
        """Mark current lesson as complete."""
        if not self.current_lesson:
            return
        
        if self.current_lesson.id not in self.progress.lessons_completed:
            self.progress.lessons_completed.append(self.current_lesson.id)
            self.progress.total_score += 100
            self.file_manager.save_progress(self.progress)
            
            # Update list
            index = self.current_lesson.id - 1
            self.lesson_list.item(index).setText(
                f"✓ Lesson {self.current_lesson.id}: {self.current_lesson.title}"
            )
            
            QMessageBox.information(
                self,
                "Congratulations! 🎉",
                f"You've completed Lesson {self.current_lesson.id}!\n\n"
                f"+100 points earned\n"
                f"Total Score: {self.progress.total_score}"
            )
