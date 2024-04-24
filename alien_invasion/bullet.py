import pygame
from pygame.sprite import _Group, Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""


    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""

        super().__init__()
        