import sys
from time import sleep

import pygame

from ss_settings import Settings
from ss_game_stats import GameStats
from ss_ship import Ship
from ss_bullet import Bullet
from ss_alien import Alien
from ss_button import Button
from ss_scoreboard import Scoreboard
from ss_border import Border

class SidewaysShooter: 
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game, create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height) )
        
        pygame.display.set_caption("Sideways Shooter")

        # Create instance to store game stats and score
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.border = Border(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start game in active state
        self.game_active = False

        # Play button
        self.play_button = Button(self, "Play")


    def run_game(self):
        """Start main game loop"""
        while True: 
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(60)


    def _create_fleet(self):
        """Create fleet of aliens"""
        # Create alien; add more aliens until out of room
        # Spacing between aliens is 1 alien width/height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = (alien_width * 3), alien_height
        while current_x < (self.settings.screen_width - 1 * alien_width):
            while current_y < (self.settings.screen_height - 1 * alien_height):
                self._create_alien(current_x, current_y)
                current_y += 2 * alien_width

            # Finished column; reset y, increment x
            current_y = alien_height
            current_x += 2 * alien_width


    def _create_alien(self, x_position, y_position):
        """Create alien, place it in column"""
        new_alien = Alien(self)
        new_alien.y = y_position
        new_alien.rect.y = y_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)


    def _check_fleet_edges(self):
        """Respond appropriately when alien reaches edge of screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

        
    def _change_fleet_direction(self):
        """Shift fleet left and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.x += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        # Enable arrow key movement
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        # Enable WASD movement
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True


    def _check_keyup_events(self, event):
        """Respond to key releases"""
                # Enable arrow key movement
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

        # Enable WASD movement
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False


    def _check_play_button(self, mouse_pos):
        """Start new game when player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset game settings
            self.settings.initialize_dynamic_settings()

            # Reset game stats
            self.stats.reset_stats()
            self.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()

            # Remove bullets/aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create new ship; center it
            self._create_fleet()
            self.ship.center_ship()

            # Hide cursor
            pygame.mouse.set_visible(False)


    def _fire_bullet(self):
        """Create new bullet; add bullets to group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets; get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Get rid of offscreen bullets
        right_edge = self.settings.screen_width
        for bullet in self.bullets.copy():
            if bullet.rect.right >= right_edge:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Respond appropriately to alien/bullet collisions"""
        # Remove any aliens/bullets that have collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
    
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1 
            self.sb.prep_level()
 

    def _update_aliens(self):
        """Check if fleet is at edge of screen; then update posotions"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check for aliens hitting bottom of screen
        self._check_aliens_left()


    def _check_aliens_left(self):
        """Check if any aliens have reached past the ship"""
        for alien in self.aliens.sprites():
            if alien.rect.left < 0:
                # Treat this same as if ship got hit
                self._ship_hit()
                break


    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1

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

    
    def _update_screen(self):
        """Update images on screen; flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.border.draw_border()

        # Draw scoreboard
        self.sb.show_score()

        # Draw play button if game inactive
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make game instance; run game
    ss = SidewaysShooter()
    ss.run_game()
    