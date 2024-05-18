import pygame
import sys
from sideways_shooter_resources import Scoreboard, Settings, Ship
from sideways_shooter_resources import Bullet, Alien, GameStats, Button


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
        self.sb = Scoreboard(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = False

        self.play_button = Button(self, 'Play')


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


        def _start_game(self):
            """Begin a new game."""

            self.stats.reset_stats()

            self.settings.initialize_dynamic_settings()

            self.sb.prep_score()
            self.sb.prep_high_score()
            self.sb.prep_level()
            
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)




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

        if collisions:

            for alien in collisions.values():
                self.stats.score += self.settings.alien_points

            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

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


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()