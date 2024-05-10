class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """initialize the game's settings."""
        ##screen settings
        self.screen_width = 1250
        self.screen_height = 700
        self.bg_color = (60,60,90)

        #ship settings
        self.ship_speed = 10

        #bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250,250,250)
        self.bullets_allowed = 10