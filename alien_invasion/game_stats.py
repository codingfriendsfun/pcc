import json
from pathlib import Path


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""

        self.settings = ai_game.settings
        
        self.high_score = self._get_high_score()

        self.reset_stats()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _get_high_score(self):
        """Retrieve the games highest score."""

        path = Path('high_score.json')

        if path.exists():
            contents = path.read_text()
            self.high_score = int(json.loads(contents))

        else:
            self.high_score = 0

        return self.high_score
    

    def save_high_score(self):
        """Save the high score after each session."""

        path = Path('high_score.json')

        contents = json.dumps(self.high_score)
        path.write_text(contents)

        