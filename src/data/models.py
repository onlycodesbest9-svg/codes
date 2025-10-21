"""Data models for RecursiveLearn."""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class LessonSection:
    """A section within a lesson."""
    title: str
    content: str  # HTML or markdown content
    examples: List[Dict] = field(default_factory=list)
    

@dataclass
class Lesson:
    """A complete lesson module."""
    id: int
    title: str
    description: str
    sections: List[LessonSection] = field(default_factory=list)
    exercises: List['Exercise'] = field(default_factory=list)
    completed: bool = False
    

@dataclass
class Exercise:
    """Practice exercise."""
    id: str
    question: str
    answer: str  # Expected answer
    hints: List[str] = field(default_factory=list)
    difficulty: str = "beginner"  # beginner, intermediate, advanced
    relation: Optional[str] = None
    initial_conditions: Optional[Dict] = None
    

@dataclass
class UserProgress:
    """Track user progress."""
    lessons_completed: List[int] = field(default_factory=list)
    exercises_completed: List[str] = field(default_factory=list)
    scores: Dict[str, int] = field(default_factory=dict)
    badges: List[str] = field(default_factory=list)
    total_score: int = 0
    last_updated: str = field(default_factory=lambda: datetime.now().isoformat())
    

@dataclass
class Badge:
    """Achievement badge."""
    id: str
    name: str
    description: str
    icon: str
    requirement: str  # Description of how to earn
    earned: bool = False
    date_earned: Optional[str] = None


@dataclass
class Settings:
    """Application settings."""
    theme: str = "light"  # light or dark
    graph_color_scheme: str = "default"
    font_size: int = 12
    accent_color: str = "#2196F3"
    instructor_pin: str = "1234"
    show_step_by_step: bool = True
    auto_save: bool = True


@dataclass
class Quiz:
    """Quiz model."""
    id: str
    title: str
    description: str
    questions: List[Dict] = field(default_factory=list)  # {question, options, correct_answer}
    time_limit: int = 0  # minutes, 0 = no limit
    created_by: str = "instructor"
    created_date: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class QuizAttempt:
    """Student quiz attempt."""
    quiz_id: str
    student_id: str
    answers: Dict[str, str] = field(default_factory=dict)
    score: float = 0.0
    completed: bool = False
    start_time: str = field(default_factory=lambda: datetime.now().isoformat())
    end_time: Optional[str] = None


@dataclass
class StudentRecord:
    """Student record for instructor tracking."""
    student_id: str
    name: str = ""
    email: str = ""
    lessons_completed: List[int] = field(default_factory=list)
    exercises_completed: List[str] = field(default_factory=list)
    quiz_attempts: List[QuizAttempt] = field(default_factory=list)
    total_score: int = 0
    last_login: str = field(default_factory=lambda: datetime.now().isoformat())
    registration_date: str = field(default_factory=lambda: datetime.now().isoformat())
