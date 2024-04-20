import pygame
from pygame.sprite import Sprite

class Settings:
    """A class to store settings for Target Practice"""
    
    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (105, 105, 105)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_misses = 3

        # Target settings
        self.target_speed = 2
        self.target_width = 15
        self.target_height = 75
        self.target_color = (205, 205, 205)
        # target_direction 1 is down, -1 is up
        self.target_direction = 1