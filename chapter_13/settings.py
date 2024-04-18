class Settings:
    """A class to store settings for Sideways Shooter"""

    def __init__(self):
        """Initialize game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (105, 105, 105)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = -10
        # fleet_direction 1 is down, -1 is up
        self.fleet_direction = 1
