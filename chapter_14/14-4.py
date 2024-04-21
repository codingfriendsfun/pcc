import sys
from time import sleep

import pygame

from settings2 import Settings
from game_stats import GameStats
from button2 import EasyButton, NormalButton, HardButton
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create instance to store game stats
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start game in inactive state
        self.game_active = False

        # Make the difficulty buttons
        self.easy_mode = EasyButton(self, "Start (Easy)")
        self.normal_mode = NormalButton(self, "Start (Normal)")
        self.hard_mode = HardButton(self, "Start (Hard)")


    def _create_fleet(self):
        """Create fleet of aliens"""
        # Create an alien and add aliens until no more room
        # Spacing around aliens is one alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished row: reset x, increment y
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
        """Create alien, place it in row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _check_fleet_edges(self):
        """Respond appropriately if alien has reached edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop entire fleet and change fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_buttons(mouse_pos)

    
    def _check_play_buttons(self, mouse_pos):
        """Start new game when player clicks Play"""
        easy_clicked = self.easy_mode.rect.collidepoint(mouse_pos)
        if easy_clicked and not self.game_active:
            self._start_game()

            # Reset game settings
            self.settings.initialize_easy_settings()

        normal_clicked = self.normal_mode.rect.collidepoint(mouse_pos)
        if normal_clicked and not self.game_active:
            self._start_game()
            
            # Reset game settings
            self.settings.initialize_normal_settings()

        hard_clicked = self.hard_mode.rect.collidepoint(mouse_pos)
        if hard_clicked and not self.game_active:
            self._start_game()

            # Reset game settings
            self.settings.initialize_hard_settings()

    
    def _start_game(self):
        """Start the game"""
        # Reset game stats
        self.stats.reset_stats()
        self.game_active = True

        # Get rid of remaining bullets/aliens
        self.bullets.empty()
        self.aliens.empty()

        # Create new fleet, center ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide mouse cursor
        pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE and self.game_active:
            self._fire_bullet()

        # Enable arrow movement
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        # Enable WASD movement
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_d:
            self.ship.moving_right = True


    def _check_keyup_events(self, event):
        """Respond to key releases."""
        # Arrow key movement
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        # WASD movement
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_d:
            self.ship.moving_right = False


    def _fire_bullet(self):
        """Create new bullet; add it to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Respond to bullet/alien collisions"""
        # Remove any bullets/aliens that collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Destroy bullets; create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()


    def _update_aliens(self):
        """Update position of all aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien/ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting bottom of screen
        self._check_aliens_bottom()


    def _ship_hit(self):
        """Respond to ship being hit by alien"""
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets/aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create new fleet; center ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """Check if aliens have reached bottom of screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw play buttons if game is inactive
        if not self.game_active:
            self.easy_mode.draw_button()
            self.normal_mode.draw_button()
            self.hard_mode.draw_button()
        
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    