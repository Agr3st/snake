import pygame
import os
from config import *

# pomysł: można dodać zielone jabłka (zatrute), które zmieniają kolor węża na zielony (zatruty), i zmniejsza
# on wtedy swój rozmiar o 1

class Apple:
    def __init__(self, size=SQUARE_SIZE):
        """
        :param size: board's square size
        """
        self.img = pygame.image.load(os.path.join('img', 'apple.png')).convert_alpha()
        self.img_scaled = pygame.transform.scale(self.img, (size, size))

    def draw(self, screen, coords):
        """
        :param screen: surface handler
        :param coords: tuple (x, y)
        """
        screen.blit(self.img_scaled, coords)

# <a href="https://www.flaticon.com/free-icons/fruit" title="fruit icons">Fruit icons created by Freepik - Flaticon</a>