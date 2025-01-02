import pygame
from config import *

class Snake:
    def __init__(self, size=SQUARE_SIZE, length=SNAKE_START_LENGTH, head_coords=SNAKE_START_HEAD_CORDS):
        """
        :param size: size of a single rectangle
        :param length: number of rectangles
        :param head_coords: x, y pair
        """
        self.coords = []
        self.size = size
        self.direction = RIGHT
        x, y = head_coords
        for i in range(length):
            self.coords.append((x - i * size, y))

    def get_head_coords(self):
        return self.coords[0]

    def get_coords(self):
        return self.coords

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

    def eat_apple(self):
        last_x, last_y = self.coords[-1]
        prev_last_x, prev_last_y = self.coords[-2]
        if prev_last_x > last_x and prev_last_y == last_y:
            self.coords.append((last_x - SQUARE_SIZE, last_y))
        elif prev_last_x < last_x and prev_last_y == last_y:
            self.coords.append((last_x + SQUARE_SIZE, last_y))
        elif prev_last_y > last_y and prev_last_x == last_x:
            self.coords.append((last_x, last_y - SQUARE_SIZE))
        elif prev_last_y < last_y and prev_last_x == last_x:
            self.coords.append((last_x, last_y + SQUARE_SIZE))

    def check_collision(self):
        # snake's body
        for coords in self.coords[1:]:
            if coords == self.coords[0]:
                # game over
                return False

        # walls
        head_x, head_y = self.coords[0]
        if head_x < 0 or head_y < 0 or head_x + self.size > SCREEN_WIDTH or head_y + self.size > SCREEN_HEIGHT:
            return False

        return True