import sys
import pygame

class TwelveFive:
    """Create an empty window and log keydown events."""


    def __init__(self):
        """Initialize game attributes."""

        pygame.init()

        self.screen = pygame.display.set_mode((100,100))        

    
    def run_game(self):
        """Launch and run the window."""

        while True:

            self._check_events()
            pygame.display.flip()


    def _check_events(self):
        """Check for key presses."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))



if __name__ == '__main__':
    # Make a game instance, and run the game.
    tf_game = TwelveFive()
    tf_game.run_game()
