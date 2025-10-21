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
