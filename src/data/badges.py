"""Badge system for gamification."""

from .models import Badge
from typing import List


def get_all_badges() -> List[Badge]:
    """Return all available badges."""
    return [
        Badge(
            id="first_lesson",
            name="First Steps",
            description="Complete your first lesson",
            icon="🎓",
            requirement="Complete 1 lesson"
        ),
        Badge(
            id="lesson_master",
            name="Lesson Master",
            description="Complete all lessons",
            icon="📚",
            requirement="Complete all 3 lessons"
        ),
        Badge(
            id="first_solve",
            name="Problem Solver",
            description="Solve your first recurrence relation",
            icon="🔍",
            requirement="Solve 1 problem"
        ),
        Badge(
            id="solver_expert",
            name="Solver Expert",
            description="Solve 10 recurrence relations",
            icon="🧮",
            requirement="Solve 10 problems"
        ),
        Badge(
            id="fibonacci_fan",
            name="Fibonacci Fan",
            description="Solve the Fibonacci sequence",
            icon="🌀",
            requirement="Solve Fibonacci relation"
        ),
        Badge(
            id="practice_champion",
            name="Practice Champion",
            description="Complete 10 practice exercises",
            icon="🏆",
            requirement="Complete 10 exercises"
        ),
        Badge(
            id="perfect_score",
            name="Perfect Score",
            description="Get 5 exercises correct on first try",
            icon="⭐",
            requirement="5 perfect answers"
        ),
        Badge(
            id="visualizer",
            name="Visual Learner",
            description="Plot 5 sequences",
            icon="📊",
            requirement="Create 5 plots"
        ),
        Badge(
            id="exporter",
            name="Documentation Master",
            description="Export 5 solutions to PDF or DOCX",
            icon="📄",
            requirement="Export 5 solutions"
        ),
        Badge(
            id="hundred_points",
            name="Century Club",
            description="Reach 100 points",
            icon="💯",
            requirement="Total score ≥ 100"
        ),
        Badge(
            id="five_hundred_points",
            name="High Achiever",
            description="Reach 500 points",
            icon="🌟",
            requirement="Total score ≥ 500"
        ),
        Badge(
            id="week_streak",
            name="Dedicated Learner",
            description="Use the app 7 days in a row",
            icon="📅",
            requirement="7-day streak"
        ),
        Badge(
            id="hanoi_master",
            name="Tower of Hanoi Master",
            description="Solve the Tower of Hanoi problem",
            icon="🗼",
            requirement="Solve Tower of Hanoi"
        ),
        Badge(
            id="compound_interest",
            name="Financial Guru",
            description="Solve a compound interest problem",
            icon="💰",
            requirement="Solve compound interest"
        ),
        Badge(
            id="all_difficulties",
            name="Challenge Accepted",
            description="Complete exercises of all difficulty levels",
            icon="🎯",
            requirement="Complete beginner, intermediate, and advanced exercises"
        )
    ]


def check_badge_earned(badge_id: str, progress) -> bool:
    """Check if a badge has been earned based on progress."""
    
    badge_checks = {
        "first_lesson": len(progress.lessons_completed) >= 1,
        "lesson_master": len(progress.lessons_completed) >= 3,
        "practice_champion": len(progress.exercises_completed) >= 10,
        "hundred_points": progress.total_score >= 100,
        "five_hundred_points": progress.total_score >= 500,
    }
    
    return badge_checks.get(badge_id, False)


def get_newly_earned_badges(progress, previous_badges: List[str]) -> List[Badge]:
    """Get badges that were just earned."""
    all_badges = get_all_badges()
    newly_earned = []
    
    for badge in all_badges:
        if badge.id not in previous_badges and check_badge_earned(badge.id, progress):
            newly_earned.append(badge)
    
    return newly_earned
