# Settings class for Alien Invasion

from alien_logs import AlienLogger

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self, sw=1200, sh=800, bgc=(30, 30, 30)):
        """Initialize the game's settings."""

        self.logs = AlienLogger(__name__)
        self.logs.logger.info("Initializing Settings.")

        # Screen settings
        self.screen_width = sw
        self.screen_height = sh
        self.bg_color = bgc

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        