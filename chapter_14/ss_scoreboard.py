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

        # Prep initial score images
        self.prep_score()
        self.prep_high_score()


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
    

    def prep_high_score(self):
        """Turn high score into rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.border_color)
        
        # Center high score at top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def show_score(self):
        """Draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)


    def check_high_score(self):
        """Check for new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
