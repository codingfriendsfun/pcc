# Alien Invasion Pygame window

import sys
import os
import pygame
from settings import Settings
from ship import Ship
from alien_logs import AlienLogger


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self, log_level):
        """Initialize the game, and create game resources."""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.logs = AlienLogger(__name__, log_level)
        
        # determine cwd
        cwd = os.getcwd()
        self.logs.logger.info(f"Running from: {cwd}")

        # display settings
        self.logs.logger.info(f"Initializing window.")
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.logs.logger.debug("Window initialization complete.")
        

        #initialize ship after window since ship uses window info
        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop for the game."""

        self.logs.logger.info("Starting game.")
        while True:
            # look for input
            self._check_events()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)
            

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        # Watch for input
        for event in pygame.event.get():
            # if user presses exit window button
            if event.type == pygame.QUIT:
                self.logs.logger.info("User chose to quit game.")
                sys.exit()


if __name__ == '__main__':
    # create instance of game object, and run the game
    ai = AlienInvasion("INFO")
    ai.run_game()


