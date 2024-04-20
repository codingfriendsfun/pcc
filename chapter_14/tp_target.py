import pygame

class Target:
    """A class to manage the target"""

    def __init__(self, tp_game):
        """Create target along right side of screen"""
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()
        self.color = self.settings.target_color

        # Create rect at (0, 0) and set correct position
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
                                self.settings.target_height)
        self.rect.center = self.screen_rect.midright
        
        # Store horizontal position as a float
        self.y = float(self.rect.y)


    def draw_target(self):
        """Draw target to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
