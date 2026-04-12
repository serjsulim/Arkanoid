import pygame
from settings import *
from boll import Boll

class Brick:
    def __init__(self):
        self.rect = []
        for x in range (50, WIDTH - 50, 80):
            for y in range (50, 200, 30):
                self.rect.append(pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT))
                print(x, y, end = ' ')
            print()
    def drow(self, screen, boll):
        for brick in self.rect:
            if brick.colliderect(boll):
                self.rect.remove(brick)
            pygame.draw.rect(screen, BRICK_COLOR, brick)


    def get_bricks(self): #думати, тут шо попало
        pass
        #self.bricks =[Brick(x, y) for x in range (50, WIDTH - 50, 80) for y in range (50, 200, 30)]