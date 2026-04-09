import pygame
import os                            # Das Dateisystem
import controls
from settings import *               # із файлу settings імпортуємо усе
from raketka import Raketka          # імпортуємо з файлу raketka клас Raketka 


def run():            
    
    running = True     #    змінна, яка показує, коли зупинити гру
    pygame.init()      # ініціюємо модуль pygame
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # створюємо вікно 
    pygame.display.set_caption('Arkanoid')           # заголовок вікна
    raketka = Raketka(screen)                  # створюємо ракетку з рядка 3 імпорту з файла ракетка


    while running:
        controls.events(screen, raketka)           # відслідковуємо натискання клавіш для руху ракетки
        raketka.update_raketka()                   # оновити положення ракетки ()              
        controls.update(BG_COLOR, screen, raketka)
       

run()

