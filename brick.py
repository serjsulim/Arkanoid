import pygame
from settings import *

class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_WIDTH)

    def drow(self, screen):
        pygame.draw.rect(screen, BRICK_COLOR, self.rect)

    def get_bricks(self):
        pass