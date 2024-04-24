import pygame

class Ship:
    """Class to manage the ship"""

    def __init__(self, ss_game):
        """Initialize ship; set starting position"""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load image; get rect
        self.image = pygame.image.load('chapter_14/ship2.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at left center of screen
        self.rect.midleft = self.screen_rect.midleft

        # Store float for ship's exact vertical position
        self.y = float(self.rect.y)

        # Movement flats; start with still ship
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update position based on movement flags"""
        # Update y value, not rect
        if self.moving_up and self.rect.top > 50:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.y
        self.rect.y = self.y


    def center_ship(self):
        """Center ship on screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)
        