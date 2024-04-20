import sys
from time import sleep

import pygame

from target_practice import Ship
from target_practice import Settings

class TargetPractice:
    """Overall class to manage game assets and behaviors"""

    def __init__(self):
        """Initialize game, create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        self.ship = Ship(self)

    
    def run_game(self):
        """Start main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        
        # Enable arrow key movement
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        # Enable WASD movement
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True

    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        # Enable arrow key movement
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

        # Enable WASD movement
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False
            

    def _update_screen(self):
        """Update images on screen; flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Make game instance; run game
    tp = TargetPractice()
    tp.run_game()
