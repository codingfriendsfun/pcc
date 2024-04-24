class Settings:
    """A class to store settings for Sideways Shooter"""

    def __init__(self):
        """Initialize game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (105, 105, 105)
        self.border_color = (0, 0, 0)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = -15

        # Game settings
        self.speedup_scale = 1.1
        # How quickly alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction 1 is down, -1 is up
        self.fleet_direction = 1

        # Score settings
        self.alien_points = 50
        self.bullet_miss_pts = -10


    def increase_speed(self):
        """Increase speed and points"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
