"""File management and data persistence."""

import json
import os
from pathlib import Path
from typing import Dict, Any
from ..data.models import UserProgress, Settings


class FileManager:
    """Manage local file storage for RecursiveLearn."""
    
    def __init__(self):
        self.base_dir = self._get_data_directory()
        self._ensure_directories()
        
    def _get_data_directory(self) -> Path:
        """Get the data storage directory."""
        # Use Documents folder
        if os.name == 'nt':  # Windows
            docs = Path.home() / 'Documents'
        else:  # Linux, Mac
            docs = Path.home() / 'Documents'
        
        data_dir = docs / 'RecursiveLearn_Data'
        return data_dir
    
    def _ensure_directories(self):
        """Create necessary directories if they don't exist."""
        self.base_dir.mkdir(parents=True, exist_ok=True)
        (self.base_dir / 'exports').mkdir(exist_ok=True)
        (self.base_dir / 'saved_problems').mkdir(exist_ok=True)
    
    def save_progress(self, progress: UserProgress):
        """Save user progress to file."""
        path = self.base_dir / 'progress.json'
        data = {
            'lessons_completed': progress.lessons_completed,
            'exercises_completed': progress.exercises_completed,
            'scores': progress.scores,
            'badges': progress.badges,
            'total_score': progress.total_score,
            'last_updated': progress.last_updated
        }
        
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_progress(self) -> UserProgress:
        """Load user progress from file."""
        path = self.base_dir / 'progress.json'
        
        if not path.exists():
            return UserProgress()
        
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            
            return UserProgress(
                lessons_completed=data.get('lessons_completed', []),
                exercises_completed=data.get('exercises_completed', []),
                scores=data.get('scores', {}),
                badges=data.get('badges', []),
                total_score=data.get('total_score', 0),
                last_updated=data.get('last_updated', '')
            )
        except Exception as e:
            print(f"Error loading progress: {e}")
            return UserProgress()
    
    def save_settings(self, settings: Settings):
        """Save application settings."""
        path = self.base_dir / 'settings.json'
        data = {
            'theme': settings.theme,
            'graph_color_scheme': settings.graph_color_scheme,
            'font_size': settings.font_size,
            'accent_color': settings.accent_color,
            'instructor_pin': settings.instructor_pin,
            'show_step_by_step': settings.show_step_by_step,
            'auto_save': settings.auto_save
        }
        
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_settings(self) -> Settings:
        """Load application settings."""
        path = self.base_dir / 'settings.json'
        
        if not path.exists():
            return Settings()
        
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            
            return Settings(
                theme=data.get('theme', 'light'),
                graph_color_scheme=data.get('graph_color_scheme', 'default'),
                font_size=data.get('font_size', 12),
                accent_color=data.get('accent_color', '#2196F3'),
                instructor_pin=data.get('instructor_pin', '1234'),
                show_step_by_step=data.get('show_step_by_step', True),
                auto_save=data.get('auto_save', True)
            )
        except Exception as e:
            print(f"Error loading settings: {e}")
            return Settings()
    
    def save_problem(self, name: str, data: Dict[str, Any]):
        """Save a solved problem."""
        path = self.base_dir / 'saved_problems' / f'{name}.json'
        
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_problem(self, name: str) -> Dict[str, Any]:
        """Load a saved problem."""
        path = self.base_dir / 'saved_problems' / f'{name}.json'
        
        if not path.exists():
            return {}
        
        with open(path, 'r') as f:
            return json.load(f)
    
    def list_saved_problems(self):
        """List all saved problems."""
        problems_dir = self.base_dir / 'saved_problems'
        if not problems_dir.exists():
            return []
        
        return [f.stem for f in problems_dir.glob('*.json')]
    
    def get_export_path(self, filename: str) -> Path:
        """Get path for exported file."""
        return self.base_dir / 'exports' / filename
    
    def load_custom_exercises(self) -> list:
        """Load custom exercises created by instructors."""
        path = self.base_dir / 'custom_exercises.json'
        
        if not path.exists():
            return []
        
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading custom exercises: {e}")
            return []
    
    def save_custom_exercises(self, exercises: list):
        """Save custom exercises."""
        path = self.base_dir / 'custom_exercises.json'
        
        with open(path, 'w') as f:
            json.dump(exercises, f, indent=2)
