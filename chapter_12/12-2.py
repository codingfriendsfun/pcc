import pygame
import sys
from cat import Cat

class BlueSky: 
    """Class to make a Pygame screen with a blue background"""
    
    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

        # Set bg color
        self.bg_color = (135, 206, 235)
        
        # Add cat
        self.cat = Cat(self)
    
    def run_game(self):
        """Start loop for game, enable quit"""
        while True: 
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw screen during each pass through loop
            self.screen.fill(self.bg_color)
            self.cat.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, run the game
    bs = BlueSky()
    bs.run_game()