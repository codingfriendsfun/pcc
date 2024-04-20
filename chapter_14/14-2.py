import sys
from time import sleep

import pygame

from tp_ship import Ship
from tp_settings import Settings
from tp_bullet import Bullet
from tp_target import Target
from tp_game_stats import GameStats

class TargetPractice:
    """Overall class to manage game assets and behaviors"""

    def __init__(self):
        """Initialize game, create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pygame.sprite.Group()

        # Create instance to store game stats
        self.stats = GameStats(self)

        # Start game in active state
        self.game_active = True


    def _check_target_edges(self):
        """Respond appropriately when target reaches edge of screen"""
        if self.target.check_edges():
            self.settings.target_direction *= -1

    
    def run_game(self):
        """Start main game loop"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()
            
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    
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


    def _fire_bullet(self):
        """Create new bullet; add bullets to group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update bullet positions; get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Get rid of offscreen bullets
        right_edge = self.settings.screen_width
        for bullet in self.bullets.copy():
            if bullet.rect.right >= right_edge:
                self._bullet_miss(bullet)
                
        # Check for bullets that hit target, delete those bullets
        if pygame.sprite.spritecollideany(self.target, self.bullets):
            self.bullets.remove(bullet)

    
    def _bullet_miss(self, bullet):
        """Respond when a bullet misses the target"""
        if self.stats.misses_left > 1:
            self.bullets.remove(bullet)
            self.stats.misses_left -= 1
        else:
            self.game_active = False


    def _update_target(self):
        """Check if target is at edge of screen; then update positions"""
        self._check_target_edges()
        self.target.update()
            

    def _update_screen(self):
        """Update images on screen; flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Make game instance; run game
    tp = TargetPractice()
    tp.run_game()
