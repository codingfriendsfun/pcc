import sys
import pygame

from settings import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init()
        ##set up the clock
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200,600))
        pygame.display.set_caption("Alien Invasion")
        ##set the background color
        self.bg_color = (60, 60, 90)
    def run_game(self):
        """start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()