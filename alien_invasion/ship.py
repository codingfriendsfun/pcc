import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('onedrive/documents/pcc/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #store a float for the ships exact horizontal position.
        self.x = float(self.rect.x)

        #movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movment flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x +=self.settings.ship_speed
        elif self.moving_left and self.rect.left >0:
            self.x -=self.settings.ship_speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -=self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y +=self.settings.ship_speed
        
        #update the rect object from self.x
        self.rect.x = self.x
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)