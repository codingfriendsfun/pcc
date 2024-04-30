import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        pygame.init()
        ##set up the clock
        self.clock = pygame.time.Clock()
        #set up settings
        self.settings = Settings()
        ##self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion")

        
        
    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            ##bullets before ship makes the bullets appear on a higher layer so they draw more naturally. 
            self.bullets.update()
            self._update_bullets()
            print(len(self.bullets))
            self.ship.update()            
            self._update_screen()            
            self.clock.tick(60)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.right >= self.settings.screen_width:
                    self.bullets.remove(bullet)
    def _check_events(self):
        """respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False 

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
                

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()