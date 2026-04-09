import pygame
from settings import *

class Raketka:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('g2/image/raketka.png') # присвоюємо змінній файл з малюнком ракетки
                                    # подивишся щодо адреси малюнка
        self.rect = self.image.get_rect()  # зробили нашу ракетку як прямокутник
        self.screen_rect = screen.get_rect()   #  створюємо прямокутник за розміром екрану
        self.rect.centerx = self.screen_rect.centerx      # координати центру по x ракетки виставити по центру екрана
        self.rect.bottom = self.screen_rect.bottom       # низ ракетки по низу екрана
        self.mright = False        # відслідковує, чи натиснута клавіша вправо
        self.mleft = False         # відслідковує, чи натиснута клавіша вліво

    def output(self):               # розміщуємо малюнок ракетки на прямокутнику на екрані
        self.screen.blit(self.image, self.rect)

    def update_raketka(self):       # оновлення позиції ракетки
        if self.mright and self.rect.right < self.screen_rect.right:    # якщо натиснута клавіша вправо і правий край ракетки менше правого краю вікна
            self.rect.centerx += SPEED_RAKETKA
        elif self.mleft  and self.rect.left > self.screen_rect.left:    # якщо натиснута клавіша вліво і лівий край ракетки більше лів краю вікна
            self.rect.centerx -= SPEED_RAKETKA
