# Settings class for Alien Invasion

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self, sw=1200, sh=800, bgc=(30, 30, 30)):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = sw
        self.screen_height = sh
        self.bg_color = bgc