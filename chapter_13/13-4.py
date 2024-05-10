import sys
import pygame
from typing import Any
from pygame.sprite import Sprite


class Rain(Sprite):
    """A class to represent a single rain_drop in the storm."""

    def __init__(self, rain_program):
        """Initialize the rain drop and its starting position."""

        super().__init__()
        self.screen = rain_program.screen

        self.image = pygame.image.load('raindrop.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.rain_speed = .5

        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if rain is at edge of screen."""

        screen_rect = self.screen.get_rect()

        return (self.rect.bottom - (.5 * self.rect.height) >= screen_rect.bottom)

    def update(self):
        """Move the rain down."""

        self.y += self.rain_speed
        self.rect.y = self.y


class MainGame:
    """Create a Pygame window with a blue screen."""


    def __init__(self):
        """Initialize background color attribute."""

        pygame.init()

        self.bg_color = (255, 255, 255)
        self.screen = pygame.display.set_mode((1200,700))
        self.height = 700
        self.width = 1200
        self.showers = pygame.sprite.Group()

        self.create_storm()

    def launch_window(self):
        """Display a blue window."""

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            self._update_rain()

            self.showers.draw(self.screen)

            pygame.display.flip()

    def _update_rain(self):
        """Check if the storm is at an edge, then update positions."""
        self._remove_rain_drop()
        self.showers.update()

    def create_storm(self):
        """Create the storm."""

        # Create an rain_drop and keep adding showers until there is no room left.
        # Spacing between showers is one rain_drop width and one rain_drop height.
        rain_drop = Rain(self)
        rain_drop_width, rain_drop_height = rain_drop.rect.size

        current_x, current_y = rain_drop_width, rain_drop_height

        while current_y < (self.height - rain_drop_height):
           
            while current_x < (self.width - rain_drop_width):

                self._create_rain_drop(current_x, current_y)
                current_x += 1.5 * rain_drop_width
            
            # Finished a row; reset x value and increment y value.
            current_x = rain_drop_width
            current_y += 2 * rain_drop_height

    def _create_rain_drop(self, x_position, y_position):
        """Create an rain_drop and place it in the row."""

        new_rain_drop = Rain(self)
        new_rain_drop.y = y_position
        new_rain_drop.rect.x = x_position
        new_rain_drop.rect.y = y_position

        self.showers.add(new_rain_drop)

    def _remove_rain_drop(self):
        """Remove raindrops if they fall off the screen."""

        for raindrop in self.showers.copy():
            if raindrop.check_edges():
                raindrop.y = raindrop.rect.height
    

if __name__ == '__main__':
    # Make a game instance, and run the game.
    raining_prog = MainGame()
    raining_prog.launch_window()