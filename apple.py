import pygame
import os
from config import *
from random import randint, choice

# pomysł: można dodać zielone jabłka (zatrute), które zmieniają kolor węża na zielony (zatruty), i zmniejsza
# on wtedy swój rozmiar o 1

class Apple:
    def __init__(self, size=SQUARE_SIZE):
        """
        :param size: board's square size
        """
        self.img = pygame.image.load(os.path.join('img', 'apple.png')).convert_alpha()
        self.img_scaled = pygame.transform.scale(self.img, (size, size))
        self.coords = [SQUARE_SIZE, SQUARE_SIZE]

    def draw(self, screen):
        """
        :param screen: surface handler
        """
        screen.blit(self.img_scaled, self.coords)

    def set_cords(self, coords):
        self.coords = coords

    def get_coords(self):
        return self.coords

# <a href="https://www.flaticon.com/free-icons/fruit" title="fruit icons">Fruit icons created by Freepik - Flaticon</a>