import sys
import json
from time import sleep
from pathlib import Path

import pygame

from settings5 import Settings
from ship5 import Ship
from bullet import Bullet
from alien import Alien
from game_stats5 import GameStats
from button5 import Button
from scoreboard5 import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game; create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create instance to store game stats; create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start game in inactive state
        self.game_active = False

        # Make Play button
        self.play_button = Button(self, "Play")


    def run_game(self):
        """Start main loop for game"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                path = Path('chapter_14/high_score.json')
                path.write_text(json.dumps(self.stats.high_score))
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    # Keyboard/mouse input

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_ESCAPE:
            path = Path('chapter_14/high_score.json')
            path.write_text(json.dumps(self.stats.high_score))
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        # Enable arrow key movement
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        
        # Enable WASD movement
        elif event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True


    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    
    def _check_play_button(self, mouse_pos):
        """Start new game when player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset game settings
            self.settings.initialize_dynamic_settings()

            # Reset game stats
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Get rid of any remaining bullets/aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create new fleet; center ship
            self._create_fleet()
            self.ship.center_ship()


    # Bullet functions

    def _fire_bullet(self):
        """Create a new bullet; add it to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets; get rid of old bullets"""
        # Update positions
        self.bullets.update()

        # Get rid of off screen bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            
        self._check_bullet_alien_collisions()

    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet/alien collisions"""
        # Remove any that have collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # Destroy existing bullets; create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()


    # Ship functions

    def _ship_hit(self):
        """Respond to ship being hit by alien"""
        if self.stats.ships_left > 0:
            # Decrement ships_left, update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of remaining bullets/aliens
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


    # Alien functions

    def _update_aliens(self):
        """Check if fleet at edge; update positions"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting bottom of screen
        self._check_aliens_bottom()


    def _check_fleet_edges(self):
        """Respond appropriately if alien reaches edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    
    def _change_fleet_direction(self):
        """Drop fleet; change fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _check_aliens_bottom(self):
        """Check if any aliens reached bottom of screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Same as if ship was hit
                self._ship_hit()
                break

    
    def _create_fleet(self):
        """Create fleet of aliens"""
        # Create alien; keep adding more till no room; spacing between aliens
        #   is one alien width/height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished row; reset x, increment y
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_position, y_position):
        """Create alien; place in fleet"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    # Screen functions    

    def _update_screen(self):
        """Update images; flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw score info
        self.sb.show_score()

        # Draw play button if game inactive
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make game instance; run game
    ai = AlienInvasion()
    ai.run_game()

