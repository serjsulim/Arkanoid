import pygame
import controls
from settings import * 
from random import choice

class Boll:
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(WIDTH//2, HEIGHT//2, RADIUS_BOLL, RADIUS_BOLL)
        self.color = BOLL_COLOR
        self.speed_x = SPEED_BOLL_X
        self.speed_y = SPEED_BOLL_Y

    def speed_random(self):
        return choice((-1.1, -1, -0.9, -1.1, -1, -0.9, -1.1, -1, -0.9, 0.9, 1, 1.1))

    def update(self, raketka):
        self.raketka = raketka
        self.rect.x -= self.speed_x      # рух по х
        self.rect.y -= self.speed_y      # рух по у

        if self.rect.left <= 0 or self.rect.right >= WIDTH:    # відбиття від лівої та правої стінок
            self.speed_x *= -1

        if self.rect.top <= 0:           # відбиття від стелі
            self.speed_y *= -1 

        #if self.rect.bottom >= self.raketka.rect.top and (self.raketka.rect.left < self.rect.centerx < self.raketka.rect.right):
        if self.rect.colliderect(self.raketka): # якщо м'яч доторкнувся до ракетки
            self.speed_y *= -1     # відбиття від ракетки
            self.speed_x = SPEED_BOLL_X * self.speed_random()    # випадковий множник
            self.rect.centery -= RADIUS_BOLL//2

        if self.rect.bottom >= HEIGHT:   # програш, коли м'яч не відбили
            controls.running = False


    def draw_boll(self):              # малюємо м'яч на екран
        pygame.draw.ellipse(self.screen, self.color, self.rect)
        

