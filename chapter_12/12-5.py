import sys

import pygame

class BlankGame:
    """Overall class to manage game assets/behavior"""

    def __init__(self):
        """Initialize game; create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blank Game")

    def run_game(self):
        """Start main game loop"""
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event)

            # Make most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    bg = BlankGame()
    bg.run_game()