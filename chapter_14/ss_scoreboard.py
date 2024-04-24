import pygame.font


class Scoreboard:
    """Class to report scoring info"""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for score info
        self.text_color = (105, 105, 105)
        self.font = pygame.font.SysFont(None, 48)

        # Prep initial score image
        self.prep_score()


    def prep_score(self):
        """Turn score into rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, 
                                            self.settings.border_color)
        
        # Display score at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 15


    def show_score(self):
        """Draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
