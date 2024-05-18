import pygame.font
from pygame.sprite import Sprite
import json
from pathlib import Path
from pygame.sprite import Group


class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_limit = 1

        # Bullet Settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_advance_speed = 15
       
        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""

        self.ship_speed = 3.5
        self.bullet_speed = 2.0
        self.alien_speed = 3.5

        # Scoring settings
        self.alien_points = 50

        self.fleet_direction = 1


    def increase_speed(self):
        """Increase speed settings."""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)    


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""

        self.settings = ai_game.settings
        
        self.high_score = self._get_high_score()

        self.reset_stats()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _get_high_score(self):
        """Retrieve the games highest score."""

        path = Path('high_score.json')

        if path.exists():
            contents = path.read_text()
            self.high_score = int(json.loads(contents))

        else:
            self.high_score = 0

        return self.high_score
    

    def save_high_score(self):
        """Save the high score after each session."""

        path = Path('high_score.json')

        contents = json.dumps(self.high_score)
        path.write_text(contents)


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact horizontal position.
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving.
        self.moving_down = False
        self.moving_up = False


    def update(self):
        """Update the ship's position based on the movement flag."""

        # Update the ship's y value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.y.
        self.rect.y = self.y


    def blitme(self):
        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Center the ship on the y-axis."""

        self.rect.midleft = self.screen_rect.midleft  
        self.y = float(self.rect.y)      


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""

        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        # Store the bullet's position as a float.
        self.x = float(self.rect.x)


    def update(self):
        """Move the bullet up the screen."""

        # Update the exact position of the bullet.
        self.x += self.settings.bullet_speed

        # Update the rect position.
        self.rect.x = self.x


    def draw_bullet(self):
        """Draw the bullet to the screen."""

        pygame.draw.rect(self.screen, self.color, self.rect)


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alient and its starting position."""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact vertical position.
        self.y = float(self.rect.y)


    def check_edges(self):
        """Return True if alien hits the edge of a screen."""

        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)


    def update(self):
        """Move the alien down."""

        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y


class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        
        self._set_button(msg)
        self.rect.centery = self.screen_rect.centery

        # The button message needs to be prepper only once.
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""

        self.msg_image = self.font.render(
                            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def _set_button(self, msg):

        if msg.lower() == 'easy':

            self.rect.centerx = self.screen_rect.centerx - 1.5 * self.rect.width

        elif msg.lower() == 'medium':
            
            self.rect.centerx = self.screen_rect.centerx

        elif msg.lower() == 'hard':

            self.rect.centerx = self.screen_rect.centerx + 1.5 * self.rect.width

        return self.rect.centerx


    def draw_button(self):
        """Draw blank button and then draw message."""

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()


    def prep_score(self):
        """Turn the score into a rendered image."""

        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"

        self.score_image = self.font.render(score_str, True,
                                self.text_color, self.settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Turn the high score into a rendered image."""

        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"

        self.high_score_image = self.font.render(high_score_str, True,
                                self.text_color, self.settings.bg_color)
        
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        """Turn the level into a rendered image."""

        level_str = str(self.stats.level)

        self.level_image = self.font.render(level_str, True,
                                self.text_color, self.settings.bg_color)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def show_score(self):
        """Draw scores and level to the screen."""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)


    def check_high_score(self):
        """Check to see if there's a new high score."""

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
