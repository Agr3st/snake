import pygame
from config import *

class Snake:
    def __init__(self):
        self.coords = []
        self.size = SQUARE_SIZE
        self.direction = RIGHT
        x, y = SNAKE_START_HEAD_CORDS
        for i in range(SNAKE_START_LENGTH):
            self.coords.append((x - i * self.size, y))

    def get_head_coords(self):
        return self.coords[0]

    def get_coords(self):
        return self.coords

    def draw(self, screen, head_color=SNAKE_HEAD_COLOR, color=SNAKE_COLOR):
        for i, coords in enumerate(self.coords):
            x, y = coords
            rectangle = pygame.Rect(x, y, self.size, self.size)
            if i == 0:
                pygame.draw.rect(surface=screen, color=head_color, rect=rectangle)
            else:
                pygame.draw.rect(surface=screen, color=color, rect=rectangle)

    def set_direction(self, keys):
        opposite_directions = {UP: DOWN, DOWN: UP, RIGHT: LEFT, LEFT: RIGHT}

        if keys[pygame.K_UP]:
            if self.direction == opposite_directions[UP]:
                return
            self.direction = UP
        elif keys[pygame.K_DOWN]:
            if self.direction == opposite_directions[DOWN]:
                return
            self.direction = DOWN
        elif keys[pygame.K_RIGHT]:
            if self.direction == opposite_directions[RIGHT]:
                return
            self.direction = RIGHT
        elif keys[pygame.K_LEFT]:
            if self.direction == opposite_directions[LEFT]:
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
        """
        :return: True if there is a collision, otherwise False
        """
        # Collision between the snake and itself
        if len(self.coords) != len(set(self.coords)):
            return True

        # Collision between the snake and walls
        head_x, head_y = self.coords[0]
        if head_x < 0 or head_y < 0 or head_x + self.size > SCREEN_WIDTH or head_y + self.size > SCREEN_HEIGHT:
            return True

        return False