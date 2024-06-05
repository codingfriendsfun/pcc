import sys
import pygame

from settings import Settings
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """A class to represent a single star in the sky"""
    
    def __init__(self, ai_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        ##load the star image and set its rect attribute.
        self.image = pygame.image.load('onedrive/documents/pcc/chapter_13/images/star.bmp')
        self.rect = self.image.get_rect()

        ## Start each new star near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        ## store the star's exact horizontal position

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class Stars:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.stars = pygame.sprite.Group()
        self._create_stars()
        pygame.display.set_caption("Stars baby Stars!!")

    def _create_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 2 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += randint(1,10)*star_width

            current_x = star_width
            current_y += randint(1,10) * star_height

    def _create_star(self, x_position, y_position):
        """create an star and place it in a row"""
        new_star= Star(self)
        new_star.x = x_position
        new_star.y = y_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)
    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._update_screen()            
            self.clock.tick(60)
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    starprog = Stars()
    starprog.run_game()