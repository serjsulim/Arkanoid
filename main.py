import pygame
import os                            # Das Dateisystem
import controls
from settings import *               # із файлу settings імпортуємо усе
from raketka import Raketka          # імпортуємо з файлу raketka клас Raketka 
from boll import Boll
from brick import Brick

def run():            
    
    pygame.init()      # ініціюємо модуль pygame
    clock = pygame.time.Clock()  # змінна для створення FPS
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # створюємо вікно 
    pygame.display.set_caption('Arkanoid')           # заголовок вікна
    raketka = Raketka(screen)                  # створюємо ракетку з рядка 3 імпорту з файла ракетка
    boll = Boll(screen)                              # створюємо м'яч
    bricks = [Brick(x, y) for x in range (50, WIDTH - 50, 80) for y in range (50, 200, 30)]

    while controls.running:
        controls.events(screen, raketka)           # відслідковуємо натискання клавіш для руху ракетки
        raketka.update_raketka()                   # оновити положення ракетки ()              
        controls.update(BG_COLOR, screen, raketka, boll)
        boll.update(raketka)
        clock.tick(FPS)  # вказуємо, щоб даний цикл while виконувався FPS раз на секунду

    pygame.quit()
    
run()

