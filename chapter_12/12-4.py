# 12-4. Rocket

import sys
import pygame

class Rocket:
    def __init__(self):
        self.rocket_screen = screen
        self.rocket_screen_rect = screen.get_rect()
        self.rocket_image = pygame.image.load('images/char.bmp')
        self.rocket_rect = self.rocket_image.get_rect()
        self.rocket_rect.center = self.rocket_screen_rect.center
        self.moving_down, self.moving_left, self.moving_right, self.moving_up = False, False, False, False

    def update(self):
        """Update the rocket's position based on the movement flag."""

        if self.moving_right and self.rocket_rect.right < self.rocket_screen_rect.right:
            self.rocket_rect.x += 1
        if self.moving_left and self.rocket_rect.left > 0:
            self.rocket_rect.x -= 1
        if self.moving_up and self.rocket_rect.bottom < self.rocket_screen_rect.bottom:
            self.rocket_rect.y -= 1
        if self.moving_down and self.rocket_rect.top > 0:
            self.rocket_rect.y += 1
        

    def blit_rocket(self):
        self.rocket_screen.blit(self.rocket_image, self.rocket_rect)


    def check_events(self):
        """Respond to keypresses and mouse events."""

        # Watch for input
        for event in pygame.event.get():
            # if user presses exit window button
            if event.type == pygame.QUIT:
                sys.exit()

            # else if key event
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            

    def _check_keydown_events(self, event):
        """Respond to keypresses."""

        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.moving_left = True
        elif event.key == pygame.K_UP:
            # Move the ship up
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move the ship down
            self.moving_down = True

               

    def _check_keyup_events(self, event):
        """Respond to key releases."""

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # Stop moving the ship to the right
                self.moving_right = False
            elif event.key == pygame.K_LEFT:
                # Stop moving the ship to the left
                self.moving_left = False
            elif event.key == pygame.K_UP:
                # Move the ship to the left
                self.moving_up = False
            elif event.key == pygame.K_DOWN:
                # Move the ship to the left
                self.moving_down = False
            elif event.key == pygame.K_q:
                sys.exit()
            


def init_gameplay():
    while True:
        rocketSprite.check_events()
        rocketSprite.update()

        screen.fill(bg_color)
        rocketSprite.blit_rocket()
        pygame.display.flip()

pygame.init()
screen = screen = pygame.display.set_mode((1200, 800))
bg_color = (107,107,110)
pygame.display.set_caption("Rocket")
rocketSprite = Rocket()

if __name__ == '__main__':
    init_gameplay()
    pygame.run_game()