import pygame

class Rocket:
    """A class to build a spaceship"""

    def __init__(self, rs_game):
        """Initialize ship and set starting position"""
        self.screen = rs_game.screen
        self.screen_rect = rs_game.screen.get_rect()

        # Load ship image and get rect
        self.image = pygame.image.load('./chapter_12/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of screen
        self.rect.center = self.screen_rect.center

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update position based on movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1


    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)