class GameStats:
    """Track statistics for Target Practice"""

    def __init__(self, tp_game):
        """Initialize stats"""
        self.settings = tp_game.settings
        self.reset_stats()


    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.misses_left = self.settings.bullet_misses