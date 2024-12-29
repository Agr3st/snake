import pygame
import os

# pomysł: można dodać zielone jabłka (zatrute), które zmieniają kolor węża na zielony (zatruty), i zmniejsza
# on wtedy swój rozmiar o 1

class Apple:
    def __init__(self, size):
        """
        :param size: board's square size
        """
        self.img = pygame.image.load(os.path.join('img', 'apple.png')).convert_alpha()
        self.img_scaled = pygame.transform.scale(self.img, (size, size))

    def draw(self, screen, x, y):
        """
        :param screen: surface handler
        :param x: x coord for left top corner of the square
        :param y: y coord for left top corner of the square
        :return:
        """
        screen.blit(self.img_scaled, (x,  y))

# <a href="https://www.flaticon.com/free-icons/fruit" title="fruit icons">Fruit icons created by Freepik - Flaticon</a>