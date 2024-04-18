import sys

import pygame

from rocket import Rocket

class RocketShip:
    """Overall class to manage game assets/behavior"""
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))

        pygame.display.set_caption("Rocket Ship")

        self.rocket = Rocket(self)

        # Background color
        self.bg_color = (105, 105, 105)


    def run_game(self):
        """Start main game loop"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Respond to key presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()

        # Enable WASD movement
        elif event.key == pygame.K_w:
            self.rocket.moving_up = True
        elif event.key == pygame.K_a:
            self.rocket.moving_left = True
        elif event.key == pygame.K_s:
            self.rocket.moving_down = True
        elif event.key == pygame.K_d:
            self.rocket.moving_right = True

        # Enable arrow key movement
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True        


    def _check_keyup_events(self, event):
        """Respond to key releases"""
        # Enable WASD movement
        if event.key == pygame.K_w:
            self.rocket.moving_up = False
        elif event.key == pygame.K_a:
            self.rocket.moving_left = False
        elif event.key == pygame.K_s:
            self.rocket.moving_down = False
        elif event.key == pygame.K_d:
            self.rocket.moving_right = False

        # Enable arrow key movement
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False


    def _update_screen(self):
        """Update images; flip to new screen"""
        self.screen.fill(self.bg_color)
        self.rocket.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Make game instance; run game
    rs = RocketShip()
    rs.run_game()