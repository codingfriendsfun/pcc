import json
from pathlib import Path

class GameStats:
    """Track statistics for Sideways Shooter"""

    def __init__(self, ss_game):
        """Initialize stats"""
        self.settings = ss_game.settings
        self.reset_stats()
        self.alien_hits = 0

        # High score should never be reset
        path = Path('chapter_14/ss_high_score.json')
        if path.exists():
            self.high_score = json.loads(path.read_text())
        else:
            self.high_score = 0
        self.start_high_score = self.high_score

    
    def reset_stats(self):
        """Initialize stats that can change during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
