"""Practice panel for RecursiveLearn."""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QTextEdit, QGroupBox, QComboBox, QListWidget,
    QMessageBox, QProgressBar
)
from PySide6.QtCore import Qt

from ..data.lessons import get_all_lessons
from ..data.models import UserProgress, Exercise
from ..utils.file_manager import FileManager
from ..core.recurrence_solver import compute_sequence


class PracticePanel(QWidget):
    """Panel for practice exercises."""
    
    def __init__(self, progress: UserProgress, file_manager: FileManager):
        super().__init__()
        
        self.progress = progress
        self.file_manager = file_manager
        self.current_exercise = None
        self.exercises = self.load_all_exercises()
        
        self.setup_ui()
        
    def load_all_exercises(self):
        """Load all exercises from lessons."""
        exercises = []
        lessons = get_all_lessons()
        
        for lesson in lessons:
            exercises.extend(lesson.exercises)
        
        return exercises
        
    def setup_ui(self):
        """Setup the user interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("🧠 Practice Exercises")
        title.setObjectName("titleLabel")
        layout.addWidget(title)
        
        # Progress bar
        progress_layout = QHBoxLayout()
        progress_label = QLabel(f"Completed: {len(self.progress.exercises_completed)}/{len(self.exercises)}")
        progress_layout.addWidget(progress_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(len(self.exercises))
        self.progress_bar.setValue(len(self.progress.exercises_completed))
        progress_layout.addWidget(self.progress_bar)
        
        layout.addLayout(progress_layout)
        
        # Filter
        filter_layout = QHBoxLayout()
        filter_label = QLabel("Difficulty:")
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["All", "Beginner", "Intermediate", "Advanced"])
        self.difficulty_combo.currentTextChanged.connect(self.filter_exercises)
        
        filter_layout.addWidget(filter_label)
        filter_layout.addWidget(self.difficulty_combo)
        filter_layout.addStretch()
        
        layout.addLayout(filter_layout)
        
        # Exercise list
        list_group = QGroupBox("Exercises")
        list_layout = QVBoxLayout(list_group)
        
        self.exercise_list = QListWidget()
        self.exercise_list.itemClicked.connect(self.load_exercise)
        list_layout.addWidget(self.exercise_list)
        
        layout.addWidget(list_group)
        
        # Update list
        self.filter_exercises("All")
        
        # Exercise display
        exercise_group = QGroupBox("Current Exercise")
        exercise_layout = QVBoxLayout(exercise_group)
        
        self.question_label = QLabel("Select an exercise to begin")
        self.question_label.setWordWrap(True)
        self.question_label.setStyleSheet("font-size: 14px; font-weight: 600; margin: 10px;")
        exercise_layout.addWidget(self.question_label)
        
        # Answer input
        answer_layout = QHBoxLayout()
        answer_label = QLabel("Your Answer:")
        answer_label.setStyleSheet("font-weight: 600;")
        self.answer_input = QLineEdit()
        self.answer_input.setPlaceholderText("Enter your answer here...")
        self.answer_input.setMinimumHeight(40)
        
        answer_layout.addWidget(answer_label)
        answer_layout.addWidget(self.answer_input)
        exercise_layout.addLayout(answer_layout)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        hint_btn = QPushButton("💡 Show Hint")
        hint_btn.clicked.connect(self.show_hint)
        btn_layout.addWidget(hint_btn)
        
        check_btn = QPushButton("✓ Check Answer")
        check_btn.clicked.connect(self.check_answer)
        btn_layout.addWidget(check_btn)
        
        btn_layout.addStretch()
        
        exercise_layout.addLayout(btn_layout)
        
        # Feedback
        self.feedback_display = QTextEdit()
        self.feedback_display.setReadOnly(True)
        self.feedback_display.setMaximumHeight(150)
        exercise_layout.addWidget(self.feedback_display)
        
        layout.addWidget(exercise_group)
        
    def filter_exercises(self, difficulty: str):
        """Filter exercises by difficulty."""
        self.exercise_list.clear()
        
        for ex in self.exercises:
            if difficulty == "All" or ex.difficulty.capitalize() == difficulty:
                completed_mark = "✓ " if ex.id in self.progress.exercises_completed else ""
                diff_emoji = {"beginner": "🟢", "intermediate": "🟡", "advanced": "🔴"}.get(ex.difficulty, "⚪")
                
                self.exercise_list.addItem(f"{completed_mark}{diff_emoji} {ex.id}: {ex.question[:50]}...")
                
    def load_exercise(self, item):
        """Load selected exercise."""
        # Find exercise by ID
        text = item.text()
        ex_id = text.split(":")[0].strip().replace("✓ ", "").replace("🟢 ", "").replace("🟡 ", "").replace("🔴 ", "")
        
        for ex in self.exercises:
            if ex.id == ex_id:
                self.current_exercise = ex
                break
        
        if self.current_exercise:
            self.question_label.setText(f"Q: {self.current_exercise.question}")
            self.answer_input.clear()
            self.feedback_display.clear()
            
    def show_hint(self):
        """Show a hint for the current exercise."""
        if not self.current_exercise or not self.current_exercise.hints:
            QMessageBox.information(self, "No Hints", "No hints available for this exercise.")
            return
        
        hints_text = "\n".join(f"{i+1}. {hint}" for i, hint in enumerate(self.current_exercise.hints))
        
        QMessageBox.information(
            self,
            "Hints 💡",
            f"Here are some hints:\n\n{hints_text}"
        )
        
    def check_answer(self):
        """Check the user's answer."""
        if not self.current_exercise:
            QMessageBox.warning(self, "No Exercise", "Please select an exercise first.")
            return
        
        user_answer = self.answer_input.text().strip()
        
        if not user_answer:
            QMessageBox.warning(self, "No Answer", "Please enter an answer.")
            return
        
        # Normalize answers for comparison
        correct_answer = self.current_exercise.answer.replace(" ", "").lower()
        user_answer_norm = user_answer.replace(" ", "").lower()
        
        if user_answer_norm == correct_answer:
            # Correct!
            self.feedback_display.setPlainText(
                "🎉 Correct! Well done!\n\n"
                f"The answer is: {self.current_exercise.answer}"
            )
            
            # Mark as completed
            if self.current_exercise.id not in self.progress.exercises_completed:
                self.progress.exercises_completed.append(self.current_exercise.id)
                self.progress.total_score += 50
                self.file_manager.save_progress(self.progress)
                
                # Update progress bar
                self.progress_bar.setValue(len(self.progress.exercises_completed))
                
                # Update list
                self.filter_exercises(self.difficulty_combo.currentText())
                
                QMessageBox.information(
                    self,
                    "Excellent Work! ✅",
                    f"+50 points earned!\nTotal Score: {self.progress.total_score}"
                )
        else:
            # Incorrect
            self.feedback_display.setPlainText(
                "❌ Not quite right. Try again!\n\n"
                "Click 'Show Hint' for help."
            )
