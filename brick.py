import pygame
from settings import *
from boll import Boll

class Brick:
    def __init__(self):
        self.rect = []                         # змінна для списку усіх цеглин    
        for x in range (50, WIDTH - 50, 80):   # перебираємо стовпці
            for y in range (50, 200, 30):     # перебираємо рядки
                self.rect.append(pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)) # створюємо цеглини
            
    def drow(self, screen, boll):             # взаємодія цеглин з м'ячем
        self.boll = boll
        for brick in self.rect:               # перебираємо усі цеглини
            if brick.colliderect(boll):       # якщо м'яч дотикається до цеглини
                self.rect.remove(brick)       # видаляємо цеглину і наступними рядками змінюємо рух м'яча
                self.boll.speed_x = self.boll.speed_x // abs(self.boll.speed_x) * SPEED_BOLL_X * boll.speed_random()
                self.boll.speed_y *= -1

            pygame.draw.rect(screen, BRICK_COLOR, brick)     # малюємо цеглини на екрані
