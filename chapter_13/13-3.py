import sys

import pygame

from raindrop import Raindrop

class RainGame:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game; create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()

        # Screen settings
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_width = 1200
        self.screen_height = 800
        pygame.display.set_caption("Rain Game")

        self.raindrops = pygame.sprite.Group()

        self._create_rain()

        # Set bg color
        self.bg_color = (105, 105, 105)

    def _create_rain(self):
        """Create rain"""
        # Modeled after PCC _create_fleet()
        # Create raindrops on screen until out of room
        # Half a raindrop's space around each raindrop
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.screen_height - 3 * raindrop_height):
            while current_x < (self.screen_width - 1 * raindrop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 1 * raindrop_width

            # Finished row: reset x; increment y
            current_x = raindrop_width
            current_y += 2 * raindrop_height

    def _check_rain_edges(self):
        """Respond appropriately if rain falls of screen"""
        for raindrop in self.raindrops.copy():
            if raindrop.check_bottom():
                self.raindrops.remove(raindrop)

    def _create_raindrop(self, x_position, y_position):
        """Create raindrop to place in rain"""
        new_raindrop = Raindrop(self)
        new_raindrop.x = x_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)

    def run_game(self):
        """Start main game loop"""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Check keydown events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def _update_raindrops(self):
        """Check if raindrop has fallen off screen; update positions"""
        self._check_rain_edges()
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += 1

    def _update_screen(self):
        """Update images on screen; flip to new screen"""
        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make game instance; run game
    rg = RainGame()
    rg.run_game()