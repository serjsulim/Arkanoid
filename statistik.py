import pygame
from settings import *

def draw_message(screen, text, text_color = TEXT_COLOR, y_offset = 0):
    font = pygame.font.Font(None, 150)
    message = font.render(text, True, text_color)
    rect = message.get_rect(center = (WIDTH//2, HEIGHT//2+ y_offset))
    screen.blit(message, rect)
