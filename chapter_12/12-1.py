import sys
import pygame


class BlueScreen:
    """Create a Pygame window with a blue screen."""


    def __init__(self):
        """Initialize background color attribute."""

        pygame.init()

        self.bg_color = (0, 0, 255)
        self.screen = pygame.display.set_mode((1200,700))


    def launch_window(self):
        """Display a blue window."""

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()
           

if __name__ == '__main__':
    # Make a game instance, and run the game.
    blue_bg = BlueScreen()
    blue_bg.launch_window()
