# 12-2. Game Character

import sys
import pygame

class GameChar:
    def __init__(self):
        self.char_screen = screen
        self.char_screen_rect = screen.get_rect()
        self.char_image = pygame.image.load('images/char.bmp')
        self.char_rect = self.char_image.get_rect()
        self.char_rect.center = self.char_screen_rect.center

    def blit_char(self):
        self.char_screen.blit(self.char_image, self.char_rect)


def init_gameplay():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        charSprite.blit_char()
        pygame.display.flip()

pygame.init()
screen = screen = pygame.display.set_mode((1200, 800))
bg_color = (107,107,110)
pygame.display.set_caption("Game Character")
charSprite = GameChar()

if __name__ == '__main__':
    init_gameplay()
    pygame.run_game()