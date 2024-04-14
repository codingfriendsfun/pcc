import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star"""
    
    def __init__(self, sg_game):
        """Initialize star and set starting location"""
        super().__init__()
        self.screen = sg_game.screen

        # Load image and set rect attribute
        self.image = pygame.image.load('chapter_13/star.bmp')
        self.rect = self.image.get_rect()

        # Start each star in top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal postition
        self.x = float(self.rect.x)