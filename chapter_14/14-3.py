import sys
from time import sleep

import pygame

from tp_ship import Ship
from tp_settings2 import Settings
from tp_bullet import Bullet
from tp_target import Target
from tp_game_stats import GameStats
from button import Button

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
        self.game_active = False

        # Make the Play button
        self.play_button = Button(self, "Click or press space to play")


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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Start a new game when player clicks button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()


    def _start_game(self):
        """Start the game"""
        # Reset game statistics
        self.stats.reset_stats()
        self.game_active = True

        # Reset game settings
        self.settings.initialize_dynamic_settings()

        # Get rid of any remaining bullets
        self.bullets.empty()

        # Center the ship
        self.ship.center_ship()

        # Hide mouse cursor
        pygame.mouse.set_visible(False)

    
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE and self.game_active:
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

        # Start game with space bar
        elif event.key == pygame.K_SPACE and not self.game_active:
            self._start_game()

    
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
            
            # Speedup game when succesful hit
            self.settings.increase_speed()

    
    def _bullet_miss(self, bullet):
        """Respond when a bullet misses the target"""
        if self.stats.misses_left > 1:
            self.bullets.remove(bullet)
            self.stats.misses_left -= 1
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


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

        # Draw play button if game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make game instance; run game
    tp = TargetPractice()
    tp.run_game()
