import sys
import pygame
from random import randint
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star in the fleet."""

    def __init__(self, ai_game):
        """Initialize the start and its starting position."""

        super().__init__()
        self.screen = ai_game.screen

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)

        self.max_stars = 100


class BlueScreen:
    """Create a Pygame window with a blue screen."""


    def __init__(self):
        """Initialize background color attribute."""

        pygame.init()

        self.bg_color = (0, 0, 15)

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        
        self.stars = pygame.sprite.Group()

        self._create_stars()



    def launch_window(self):
        """Display a night sky with stars."""

        while True:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            self.screen.fill(self.bg_color)
            self.stars.draw(self.screen)

            pygame.display.flip()
           
    def _create_stars(self):
        """Create the night sky."""

        star = Star(self)
        star_width, star_height = star.rect.size

        star_count = 0

        while star_count != star.max_stars:

            current_x = randint(0 , (self.screen_width - star_width))
            current_y = randint(0,(self.screen_height - star_height))

            self._create_star(current_x, current_y)

            star_count += 1


    def _create_star(self, x_position, y_position):
        """Create an star and place it in the row."""

        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    blue_bg = BlueScreen()
    blue_bg.launch_window()
