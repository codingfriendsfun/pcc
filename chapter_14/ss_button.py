import pygame.font

class Button:
    """A class to build buttons for game"""

    def __init__(self, ai_game, msg):
        """Initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build button's rect object; center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message prep; only done once
        self._prep_msg(msg)