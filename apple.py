import pygame
import os
from config import *

class Apple:
    def __init__(self, size=SQUARE_SIZE):
        self.img = pygame.image.load(os.path.join('img', 'apple.png')).convert_alpha()
        self.img_scaled = pygame.transform.scale(self.img, (size, size))
        self.coords = [SQUARE_SIZE, SQUARE_SIZE]

    def draw(self, screen):
        screen.blit(self.img_scaled, self.coords)

    def set_coords(self, coords):
        self.coords = coords

    def get_coords(self):
        return self.coords

# <a href="https://www.flaticon.com/free-icons/fruit" title="fruit icons">Fruit icons created by Freepik - Flaticon</a>