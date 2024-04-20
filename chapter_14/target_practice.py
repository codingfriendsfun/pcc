import pygame

class Ship:
    """A class to manage ship for Target Practice"""
    
    def __init__(self, tp_game):
        """Initialize ship; set starting position"""
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()

        # Load image; get rect
        self.image = pygame.image.load('chapter_14/ship2.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at left center of screen
        self.rect.midleft = self.screen_rect.midleft

        # Store float for ship's exact vertical position
        self.y = float(self.rect.y)

        # Movement flags; start with still ship
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update position based on movement flags"""
        # Update y value, not rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect from self.y
        self.rect.y = self.y


    def center_ship(self):
        """Center ship on screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)


    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

class Settings:
    """A class to store settings for Target Practice"""
    
    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (105, 105, 105)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
