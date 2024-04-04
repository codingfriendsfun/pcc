import pygame

class Cat:
    """A class to manage a cat."""

    def __init__(self, bs_game):
        """Initialize the ship and set its starting position."""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('chapter_12/cat.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)