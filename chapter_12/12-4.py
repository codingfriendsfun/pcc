import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        ##set up the clock
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        ##set the background color
        self.bg_color = (60, 60, 90)
        
    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()            
            self.clock.tick(60)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


    def _check_events(self):
        """respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    if event.key == pygame.K_UP:
                        self.ship.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.ship.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    if event.key == pygame.K_UP:
                        self.ship.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.ship.moving_down = False
                

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()