# Alien Invasion Pygame window

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        

        # display settings
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #initialize ship after window since ship uses window info
        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop for the game."""

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
        # Watch for quit
        for event in pygame.event.get():
            # if user presses exit window button
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    # create instance of game object, and run the game
    ai = AlienInvasion()
    ai.run_game()


