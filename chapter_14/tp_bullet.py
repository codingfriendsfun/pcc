import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets"""
    
    def __init__(self, tp_game):
        """Create bullet object at ship's current position"""
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.bullet_color

        # Create bullet rect at (0, 0) and set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = tp_game.ship.rect.midright

        # Store bullet's position as a float
        self.x = float(self.rect.x)


    def update(self):
        """Move bullet across screen"""
        self.x += self.settings.bullet_speed
        # Update rect position
        self.rect.x = self.x

    
    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
