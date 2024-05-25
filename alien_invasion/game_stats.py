import json
from pathlib import Path

class GameStats:
    """Track statistics for game"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score shouldn't be reset
        path = Path('alien_invasion/high_score.json')
        if path.exists():
            self.high_score = json.loads(path.read_text())
        else:
            self.high_score = 0


    def reset_stats(self):
        """Initialize stats that can be changed during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        