import pygame.font

class Button:
    """Class for button building"""

    def __init__(self, ai_game, msg):
        """Initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions, button properties
        self.width, self.height = 300, 50
        self.button_color = (0, 100, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build button's rect object, center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message prep (only needed once)
        self._prep_msg(msg)

    
    def _prep_msg(self, msg):
        """Turn msg into rendered image; center text on button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """Draw blank button; draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class EasyButton(Button):
    """Create button for game's easy mode"""

    def __init__(self, ai_game, msg):
        """
        Initialize aspects of parent class
        Then initialize aspects specific to the easy mode button
        """

        super().__init__(ai_game, msg)

        # Overwrite button's rect object location with left placement
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (275, 400)

    
    def _prep_msg(self, msg):
        """Turn msg into rendered image; center text on button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (275, 400)


class NormalButton(Button):
    """Create button for game's easy mode"""

    def __init__(self, ai_game, msg):
        """
        Initialize aspects of parent class
        Then initialize aspects specific to the easy mode button
        """

        super().__init__(ai_game, msg)


class HardButton(Button):
    """Create button for game's easy mode"""

    def __init__(self, ai_game, msg):
        """
        Initialize aspects of parent class
        Then initialize aspects specific to the easy mode button
        """

        super().__init__(ai_game, msg)

        # Overwrite button's rect object location with left placement
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (925, 400)

    
    def _prep_msg(self, msg):
        """Turn msg into rendered image; center text on button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (925, 400)

