import sys
import pygame.font
import pygame
from pygame.sprite import Sprite


class Button:
    """A class to build buttons for the game."""

    def __init__(self, target_practice, msg):
        """Initialize button attributes."""

        self.screen = target_practice.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center  

        # The button message needs to be prepper only once.
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""

        self.msg_image = self.font.render(
                            msg, True, self.text_color, self.button_color)
        
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """Draw blank button and then draw message."""

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
 

class Ship:
    """A class to manage the ship."""

    def __init__(self, target_practice):
        """Initialize the ship and set its starting position."""

        self.screen = target_practice.screen
        self.settings = target_practice.settings
        self.screen_rect = target_practice.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
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


class Settings:
    """A class to store all the settings for Target Practice."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 3.5

        # Bullet Settings
        self.bullet_speed = 100
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        self.max_attempts = 3

        # Target Settings
        self.target_speed = 10
        self.target_width = 15
        self.target_height = 100
        self.target_color = (60, 60, 60)
        self.target_direction = 1


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, target_practice):
        """Create a bullet object at the ship's current position."""

        super().__init__()
        self.screen = target_practice.screen
        self.settings = target_practice.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = target_practice.ship.rect.midright

        # Store the bullet's position as a float.
        self.x = float(self.rect.x)


    def update(self):
        """Move the bullet to the right."""

        # Update the exact position of the bullet.
        self.x += self.settings.bullet_speed

        # Update the rect position.
        self.rect.x = self.x


    def draw_bullet(self):
        """Draw the bullet to the screen."""

        pygame.draw.rect(self.screen, self.color, self.rect)


class Target:
    """A class to manage the target."""

    def __init__(self, target_practice):        

        self.screen = target_practice.screen
        self.settings = target_practice.settings
        self.color = self.settings.target_color

        # Create a target rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
                                self.settings.target_height)

        self.rect.x = self.settings.screen_width - (self.rect.width * 2)
        self.rect.y = self.settings.screen_height - (self.rect.height * 2)

        # Store the target's position as a float.
        self.y = float(self.rect.y)


    def update(self):
        """Move the target up and down."""

        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y
    

    def check_edges(self):
        """Return True if target is at edge of screen."""

        screen_rect = self.screen.get_rect()

        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)


    def draw_target(self):
        """Draw the target to the screen."""

        pygame.draw.rect(self.screen, self.color, self.rect)


class TargetPractice:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Target Practice')

        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pygame.sprite.Group()

        self.game_active = False

        self.play_button = Button(self, "Play")


    def run_game(self):
        """Start the main loop for the game."""

        while True:

            self._check_events()

            if self.game_active:

                self.ship.update()
                self._update_target()
                self._update_bullets()

            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Respond to keypresses and mouse events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""

        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_UP:
            self.ship.moving_up = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """Respond to key releases."""

        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

        elif event.key == pygame.K_UP:
            self.ship.moving_up = False


    def _check_play_button(self, mouse_pos):
        """Check the status of the play button."""

        if self.play_button.rect.collidepoint(mouse_pos):

            self.game_active = True
            self.bullets.empty()
            self.ship.center_ship()


    def _update_target(self):
        """Update targets behavior."""

        self.target.update()
        self._check_target_edges()


    def _check_target_edges(self):
        """Change target directions if a screen edge is hit."""

        if self.target.check_edges():
            self.settings.target_direction *= -1


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""

        # Update bullet position.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():

            if bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)

                if self.settings.max_attempts > 0:
                    self.settings.max_attempts -= 1

                    if self.settings.max_attempts == 0:
                        self._reset_game()

                else:
                    self._reset_game()


    def _reset_game(self):
        """Reset the game."""

        self.settings.max_attempts = 3
        self.game_active = False
        self.ship.center_ship()


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.target.draw_target()

        if not self.game_active:
             self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = TargetPractice()
    ai.run_game()
