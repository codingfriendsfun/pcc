import pygame

class Border:
    """Class to hold border"""

    def __init__(self, bs_game):
        self.screen = bs_game.screen
        self.color = (0, 0, 0)

        # Create rect
        self.rect = pygame.Rect(0, 0, 1200, 50)

    def draw_border(self):
        """Draw border to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)