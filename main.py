import pygame
import os                            # Das Dateisystem
import controls
from settings import *               # із файлу settings імпортуємо усе
from raketka import Raketka          # імпортуємо з файлу raketka клас Raketka 
from boll import Boll
from brick import Brick
import statistik

def run():            
    
    pygame.init()      # ініціюємо модуль pygame
    clock = pygame.time.Clock()  # змінна для створення FPS
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # створюємо вікно 
    pygame.display.set_caption('Arkanoid')           # заголовок вікна
    raketka = Raketka(screen)                  # створюємо ракетку з рядка 3 імпорту з файла ракетка
    boll = Boll(screen)                              # створюємо м'яч
    bricks = Brick()

    while controls.running:
        controls.events(screen, raketka)           # відслідковуємо натискання клавіш для руху ракетки
        raketka.update_raketka()                   # відслідковуємо, куди рухати ракетку              
        controls.update(BG_COLOR, screen, raketka, boll, bricks) # відслідковуємо взаємодії
        
        
        clock.tick(FPS)  # вказуємо, щоб даний цикл while виконувався FPS раз на секунду

    if controls.win:
        screen.fill(BG_COLOR)                   # замалювати все вікно фоновим кольором
        statistik.draw_message(screen, "YOU WON, NEXT LEVEL", TEXT_COLOR, 0 )
        pygame.display.flip()                   # промалювати кадр
    input()
    
run()

pygame.quit()
