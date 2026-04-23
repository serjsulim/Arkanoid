import pygame
from settings import *
from boll import Boll
import controls
from map import *

class Brick:
    def __init__(self, level):
        self.level = level
        self.map = level_map[level]
        self.rect = []                         # змінна для списку усіх цеглин    
        br_width = WIDTH // 11.1
        for y in range(len(self.map)):
            for x in range(len(self.map[1])):
                self.rect.append([pygame.Rect((int(0.1 * br_width + 1.1 * br_width * x)), 50 + 1.3 * y * BRICK_HEIGHT, br_width, BRICK_HEIGHT), self.map[y][x]]) # створюємо цеглини

        # for x in range (BRICK_HOME, WIDTH - BRICK_HOME, BRICK_WIDTH + 10):   # перебираємо стовпці
        #     for y in range (50, 200, 30):     # перебираємо рядки
        #         self.rect.append(pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)) # створюємо цеглини
            
    def drow(self, screen, boll):             # взаємодія цеглин з м'ячем
        self.boll = boll
        for brick in self.rect:               # перебираємо усі цеглини
            if brick[0].colliderect(boll):       # якщо м'яч дотикається до цеглини
                self.rect.remove(brick)       # видаляємо цеглину і наступними рядками змінюємо рух м'яча
                #self.boll.speed_x = self.boll.speed_x // abs(self.boll.speed_x) * SPEED_BOLL_X * boll.speed_random()
                self.boll.speed_y *= -1
            if len(self.rect) == 0:           # якщо усі цеглини знищено
                controls.running = False      # гра закінчена
                controls.win = True           # виграш

            pygame.draw.rect(screen, BRICK_COLOR[brick[1]], brick[0])     # малюємо цеглини на екрані
