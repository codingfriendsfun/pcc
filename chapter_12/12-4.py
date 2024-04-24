import sys
import pygame


class Wolf:
    """A class to create a woofer."""

    def __init__(self, BlueScreen):
        """Initialize the woof and center it."""

        self.screen = BlueScreen.screen
        self.screen_rect = BlueScreen.screen.get_rect()

        self.image = pygame.image.load('wolf.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Wolf movement.
        self.wolf_speed = .5

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        """Draw the woof at its current location."""

        self.screen.blit(self.image, self.rect)


    def update(self):
        """Update the wolves position based on the movement flag."""
        
        # Update the woofs x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.wolf_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.wolf_speed
        
        # Update the woofs y value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.wolf_speed
        
        if self.moving_up and self.rect.top > 0:
            self.y -= self.wolf_speed

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y


class BlueScreen:
    """Create a Pygame window with a blue screen."""


    def __init__(self):
        """Initialize background color attribute."""

        pygame.init()

        self.bg_color = (0, 0, 255)
        self.screen = pygame.display.set_mode((1200,700))
        self.wolf = Wolf(self)


    def launch_game(self):
        """Create a woof game."""

        while True:

            self._check_events()
            self.wolf.update()
            self._update_screen()


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

        if event.key == pygame.K_RIGHT:
            self.wolf.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.wolf.moving_left = True

        elif event.key == pygame.K_DOWN:
            self.wolf.moving_down = True

        elif event.key == pygame.K_UP:
            self.wolf.moving_up = True

        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """Respond to key releases."""

        if event.key == pygame.K_RIGHT:
            self.wolf.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.wolf.moving_left = False

        elif event.key == pygame.K_DOWN:
            self.wolf.moving_down = False

        elif event.key == pygame.K_UP:
            self.wolf.moving_up = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
       
        self.screen.fill(self.bg_color)
        self.wolf.blitme()

        pygame.display.flip()
           

if __name__ == '__main__':
    # Make a game instance, and run the game.
    blue_bg = BlueScreen()
    blue_bg.launch_game()
