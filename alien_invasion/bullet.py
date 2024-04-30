import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        #store the bullet's position as a float
        self.x = float(self.rect.x)

    def draw_bullet(self):
        """draw a bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """move the bullet up the screen"""
        self.x +=self.settings.bullet_speed

        self.rect.x = self.x
