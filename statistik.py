import pygame
from settings import *

def draw_message(screen, text, TEXT_COLOR, y_offset):
    font = pygame.font.Font(None, 50)
    message = font.render(text, True, TEXT_COLOR)
    rect = message.get_rect(center = (WIDTH//2, HEIGHT//2+ y_offset))
    screen.blit(message, rect)
