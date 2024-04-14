import sys
import pygame
from star import Star

class StarNotgame:
    """Class to manage game assets and behavior"""
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_width = 1200
        self.screen_height = 800
        pygame.display.set_caption("Star Not-Game")
        self.stars = pygame.sprite.Group()

        self._create_starry_night()

        # Set background color
        self.bg_color = (105, 105, 105)


    def _create_starry_night(self):
        """Create starfield"""
        # Make one star, then more until there's no more room
        # Space around stars is one star width and one star height
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.screen_height - 2 * star_height):
            while current_x < (self.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            # Finished a row, reset x and increment y
            current_x = star_width
            current_y += 2 * star_height

        
    def _create_star(self, x_position, y_position):
        """Create a star and place it in the night"""
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)
    

    def run_game(self):
        """Start main loop for game"""
        while True: 
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    
    
    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            
    def _update_screen(self):
        """Update images on screen, flip to new screen"""
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make game instance, run game
    sg = StarNotgame()
    sg.run_game()
