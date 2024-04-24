import pygame.font
from pygame.sprite import Group

from ss_ship import SmallShip


class Scoreboard:
    """Class to report scoring info"""

    def __init__(self, ss_game):
        """Initialize scorekeeping attributes"""
        self.ss_game = ss_game
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ss_game.settings
        self.stats = ss_game.stats

        # Font settings for score info
        self.text_color = (105, 105, 105)
        self.font = pygame.font.SysFont(None, 32)

        # Prep initial images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_ships(self):
        """Show ships left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = SmallShip(self.ss_game)
            ship.rect.x = 4 + ship_number * ship.rect.width
            ship.rect.y = 4
            self.ships.add(ship)
            

    def prep_level(self):
        """Turn level into rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
            self.settings.border_color)
        
        # Position level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 1.5

    
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


    def prep_score(self):
        """Turn score into rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, 
                                            self.settings.border_color)
        
        # Display score at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 6


    def show_score(self):
        """Draw scoreboard images to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def check_high_score(self):
        """Check for new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
