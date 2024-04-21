# 12-1. Blue Sky

import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
bg_color = (20,150,255)

pygame.display.set_caption("Blue Sky")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(bg_color)
    pygame.display.flip()

if __name__ == '__main__':
    pygame.run_game()