# Alien Invasion Pygame window

import sys
import os
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
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
        self.logs.logger.info(f"Initializing window in fullscreen.")
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.logs.logger.debug("Window initialization complete.")
        

        #initialize ship and other elements after window since ship uses window info
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Start the main loop for the game."""

        self.logs.logger.info("Starting game.")
        while True:
            # look for input
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Get rid of bullets that are no longer needed
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                    self.logs.logger.info(f"Deleting bullet outside window. {len(self.bullets)} bullets remain.")

            self._update_screen()

            # cycle pacing (ticks per second)
            self.clock.tick(60)


    def _check_events(self):
        """Respond to keypresses and mouse events."""

        # Watch for input
        for event in pygame.event.get():
            # if user presses exit window button
            if event.type == pygame.QUIT:
                self.logs.logger.info("User chose to quit game.")
                sys.exit()

            # else if key event
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _undef_events(self, event):
        """Log unknown input events"""
        self.logs.logger.debug(f"Unanticipated key event: \n\t- Event type: {pygame.event.event_name(event.type)}\n" +
                                   f"\t- Event key: {pygame.key.name(event.key)}") 
            

    def _check_keydown_events(self, event):
        """Respond to keypresses."""

        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.logs.logger.debug("Detected right arrow press.")
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.logs.logger.debug("Detected left arrow press.")
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        else: # other key event
            self._undef_events(event)
               

    def _check_keyup_events(self, event):
        """Respond to key releases."""

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # Stop moving the ship to the right
                self.logs.logger.debug("Detected right arrow release.")
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                # Stop moving the ship to the left
                self.logs.logger.debug("Detected left arrow release.")
                self.ship.moving_left = False
            elif event.key == pygame.K_q:
                self.logs.logger.info("User pressed q to quit game.")
                sys.exit()


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group.""" 

        if len(self.bullets) < self.settings.bullets_allowed:
            self.logs.logger.info("Creating bullet.")
            self.bullets.add(Bullet(self))
            self.logs.logger.info(f"Current # of Bullets: " +
                                    f"{len(self.bullets)}.")
        else: # too many bullets
            self.logs.logger.info("Max bullet limit reached.")


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # Make the most recently drawn screen visible
        self.logs.logger.debug("Updating screen.")
        pygame.display.flip()


if __name__ == '__main__':
    # create instance of game object, and run the game
    ai = AlienInvasion("INFO")
    ai.run_game()


