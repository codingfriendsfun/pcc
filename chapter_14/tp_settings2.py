import pygame
from pygame.sprite import Sprite

class Settings:
    """A class to store settings for Target Practice"""
    
    def __init__(self):
        """Initialize game's static settings"""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (105, 105, 105)

        # Bullet settings
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_misses = 3

        # Target settings
        self.target_width = 15
        self.target_height = 75
        self.target_color = (205, 205, 205)

        # How quickly game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout game"""
        # Ship settings
        self.ship_speed = 2.5
        self.bullet_speed = 7
        self.target_speed = 2

        # target_direction 1 is down, -1 is up
        self.target_direction = 1


    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale
