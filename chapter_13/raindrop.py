import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in the rain"""

    def __init__(self, rain_game):
        """Initialize raindrop and set starting position"""
        super().__init__()
        self.screen = rain_game.screen
        self.rain_speed = 2.0

        # Load image; set rect attribute
        self.image = pygame.image.load('chapter_13/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each raindrop at top left
        self.rect.x = self.rect.width
        self.rect.y - self.rect.height

        self.y = float(self.rect.y)

    def check_bottom(self):
        """Return True if raindrop has fallen off screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom)