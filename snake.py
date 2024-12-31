import pygame
from config import *

class Snake:
    def __init__(self, size=SQUARE_SIZE, length=SNAKE_START_LENGTH, head_coords=SNAKE_START_HEAD_CORDS):
        """
        :param size: size of a single rectangle
        :param length: number of rectangles
        :param head_coords: x, y pair
        """
        x, y = head_coords
        self.coords = []
        self.size = size
        self.direction = RIGHT
        for i in range(length):
            self.coords.append((x - i * size, y))

    def draw(self, screen, head_color=SNAKE_HEAD_COLOR, color=SNAKE_COLOR):
        # mozna utworzyc 1 obiekt Rect i tylko go przesuwac, żeby rysować kolejne kwadraty snake'a
        for i, coords in enumerate(self.coords):
            x, y = coords
            rectangle = pygame.Rect(x, y, self.size, self.size)
            if i == 0:
                pygame.draw.rect(surface=screen, color=head_color, rect=rectangle)
            else:
                pygame.draw.rect(surface=screen, color=color, rect=rectangle)

    def set_direction(self, keys):
        if keys[pygame.K_UP]:
            if self.direction == DOWN:
                return
            self.direction = UP
        elif keys[pygame.K_DOWN]:
            if self.direction == UP:
                return
            self.direction = DOWN
        elif keys[pygame.K_RIGHT]:
            if self.direction == LEFT:
                return
            self.direction = RIGHT
        elif keys[pygame.K_LEFT]:
            if self.direction == RIGHT:
                return
            self.direction = LEFT

    def move(self):
        head_x, head_y = self.coords[0]
        if self.direction == UP:
            self.coords.insert(0, (head_x, head_y - self.size))
        elif self.direction == DOWN:
            self.coords.insert(0, (head_x, head_y + self.size))
        elif self.direction == RIGHT:
            self.coords.insert(0, (head_x + self.size, head_y))
        elif self.direction == LEFT:
            self.coords.insert(0, (head_x - self.size, head_y))
        self.coords.pop()

    def check_collision(self, apple_cords):
        pass