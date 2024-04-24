import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize alien; set starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image; set rect attribute
        self.image = pygame.image.load('chapter_14/alien.bmp')
        self.rect = self.image.get_rect()

        # Start new alien at top right of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact horizontal position
        self.y = float(self.rect.y)


    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 50)
    

    def update(self):
        """Move alien down"""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y
        