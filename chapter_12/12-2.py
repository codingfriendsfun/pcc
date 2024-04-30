import sys
import pygame

from settings import Settings
from luffy import Luffy

class LuffyInvasion:
    def __init__(self):
        pygame.init()
        ##set up the clock
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Luffy Invasion")

        self.luffy = Luffy(self)
        ##set the background color
        self.bg_color = (60, 60, 90)
        
    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()            
            self.clock.tick(60)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.luffy.blitme()

        pygame.display.flip()


    def _check_events(self):
        """respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

if __name__ == '__main__':
    ai = LuffyInvasion()
    ai.run_game()