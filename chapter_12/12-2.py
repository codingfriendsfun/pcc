import sys
import pygame


class Wolf:
    """A class to create a woofer."""

    def __init__(self, BlueScreen):
        """Initialize the woof and center it."""

        self.screen = BlueScreen.screen
        self.screen_rect = BlueScreen.screen.get_rect()

        self.image = pygame.image.load('wolf.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center


    def blitme(self):
        """Draw the woof at its current location."""
        self.screen.blit(self.image, self.rect)


class BlueScreen:
    """Create a Pygame window with a blue screen."""


    def __init__(self):
        """Initialize background color attribute."""

        pygame.init()

        self.bg_color = (0, 0, 255)
        self.screen = pygame.display.set_mode((1200,700))
        self.wolf = Wolf(self)


    def launch_window(self):
        """Display a blue window."""

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.wolf.blitme()
            
            pygame.display.flip()
           

if __name__ == '__main__':
    # Make a game instance, and run the game.
    blue_bg = BlueScreen()
    blue_bg.launch_window()
