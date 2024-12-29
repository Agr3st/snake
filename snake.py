import pygame
from constants import *

class Snake:
    def __init__(self, size, length, head_coords):
        """
        :param size: size of a single rectangle
        :param length: number of rectangles
        :param head_coords: x, y pair
        """
        x, y = head_coords
        self.coords = []
        self.size = size
        for i in range(length):
            self.coords.append((x - i * size, y))

    def draw(self, screen, color):
        # mozna utworzyc 1 obiekt Rect i tylko go przesuwac, żeby rysować kolejne kwadraty snake'a
        for x, y in self.coords:
            rectangle = pygame.Rect(x, y, self.size, self.size)
            pygame.draw.rect(surface=screen, color=color, rect=rectangle)

    def move(self, direction):
        # zmieniamy tylko
        head_x, head_y = self.coords[0]
        if direction == UP:
            self.coords.insert(0, (head_x, head_y - self.size))
            self.coords.pop()
        elif direction == DOWN:
            self.coords.insert(0, (head_x, head_y + self.size))
            self.coords.pop()
        elif direction == RIGHT:
            self.coords.insert(0, (head_x + self.size, head_y))
            self.coords.pop()
        elif direction == LEFT:
            self.coords.insert(0, (head_x - self.size, head_y))
            self.coords.pop()
