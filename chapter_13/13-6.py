import pygame
import sys
from pygame.sprite import Sprite


class GameStats:
    """Track Statistics for Sideways Shooter."""

    def __init__(self, ai_game):
        """Initialize statistics."""

        self.settings = ai_game.settings
        self.reset_stats()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""

        self.ships_left = self.settings.ship_limit
        self.aliens_hit = self.settings.aliens_hit


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


class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 3.5
        self.ship_limit = 1

        # Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 300
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed = 3.5
        self.fleet_advance_speed = 15
        self.aliens_hit = 0
        
        # fleet_direction of 1 represents down; -1 represents up
        self.fleet_direction = 1


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


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')

        self.stats = GameStats(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = True


    def run_game(self):
        """Start the main loop for the game."""

        while True:

            self._check_events()

            if self.game_active:

                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Respond to keypresses and mouse events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
                
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

        self._check_bullet_alien_collision()


    def _check_bullet_alien_collision(self):
        """Respond do alien-bullet collision."""

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        for bullet, alien in collisions.items():
            
            if alien:
                self.stats.aliens_hit += 1 

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()


    def _update_aliens(self):
        """Update the position of all aliens in the fleet."""

        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_left_screen ()


    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _check_aliens_left_screen(self):
        """Check if aliens have hit the left side of the screen."""

        for alien in self.aliens.sprites():
            if alien.rect.x <= 0:
                self._ship_hit()
                break


    def _change_fleet_direction(self):
        """Advance the fleet to the left and change directions from down to up."""

        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_advance_speed

        self.settings.fleet_direction *= -1


    def _create_fleet(self):
        """Create the fleet of aliens."""

        # Create an alien and keep adding aliens until there is no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = (alien_width * 3), alien_height

        while current_x < (self.settings.screen_width - 3 * alien_width):

            while current_y < (self.settings.screen_height - 2 * alien_height):
                self._create_alien(current_x, current_y)
                current_y += 2.5 * alien_height

            # Finished a row; reset y value and increment x value.
            current_y = alien_height
            current_x += 2.5 * alien_width


    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""

        new_alien = Alien(self)
        new_alien.y = y_position
        new_alien.rect.y = y_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)


    def _ship_hit(self):
        """Respond to a ship being it by an alien."""

        self.game_active = False
        print("Game Over!")
        print(f"You shot {self.stats.aliens_hit} aliens!")
        sys.exit()


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()