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

    def draw(self, screen, head_color, color):
        # mozna utworzyc 1 obiekt Rect i tylko go przesuwac, żeby rysować kolejne kwadraty snake'a
        for i, coords in enumerate(self.coords):
            x, y = coords
            rectangle = pygame.Rect(x, y, self.size, self.size)
            if i == 0:
                pygame.draw.rect(surface=screen, color=head_color, rect=rectangle)
            else:
                pygame.draw.rect(surface=screen, color=color, rect=rectangle)


    def move(self, direction):
        head_x, head_y = self.coords[0]
        if direction == UP:
            self.coords.insert(0, (head_x, head_y - self.size))
        elif direction == DOWN:
            self.coords.insert(0, (head_x, head_y + self.size))
        elif direction == RIGHT:
            self.coords.insert(0, (head_x + self.size, head_y))
        elif direction == LEFT:
            self.coords.insert(0, (head_x - self.size, head_y))
        self.coords.pop()
