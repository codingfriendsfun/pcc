# ship class for Alien Invasion

import pygame
import os
from alien_logs import AlienLogger

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        self.logs = AlienLogger(__name__)
        self.logs.logger.info(f"Initializing ship.")

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # determine cwd
        cwd = os.getcwd()
        self.logs.logger.debug(f"Working Directory: {cwd}.")
        index = cwd.find("Alien_Invasion")
        if index > 0:
            cwd = cwd[:index]
        image_path = f'{cwd}/Alien_Invasion/images/ship.bmp'
        self.logs.logger.debug(f"Ship Image: {image_path}")

        # Load the ship image and get its rect
        self.image = pygame.image.load(f'{cwd}/Alien_Invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

        self.logs.logger.debug("Ship initialization complete.")


    def update(self):
        """Update the ship's position based on the movement flag."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.logs.logger.debug("Moving ship right within screen dimensions.")
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.logs.logger.debug("Moving ship left within screen dimensions.")
            self.rect.x -= 1


    def blitme(self):
        """Draw the ship at its current location."""

        self.logs.logger.debug("Drawing Ship.")
        self.screen.blit(self.image, self.rect)
