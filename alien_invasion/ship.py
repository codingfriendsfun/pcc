import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize ship; set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image; get its rect
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store float for exact horizontal position
        self.x = float(self.rect.x)

        # Movement flags; start with still ship
        self.moving_right = False
        self.moving_left = False


    def center_ship(self):
        """Center ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


    def update(self):
        """Update ship's position based on movement flags"""
        # Update x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)
