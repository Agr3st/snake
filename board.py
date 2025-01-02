import pygame
from config import *

class Board:
    def __init__(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, square_size=SQUARE_SIZE):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.square_size = SQUARE_SIZE
        self.grid_surface = pygame.Surface((self.width, self.height))
        self._draw_static_grid()

    def _draw_static_grid(self, light_color=SQUARE_COLOR_LIGHT, dark_color=SQUARE_COLOR_DARK):
        i = 0
        for x in range(0, self.width, self.square_size):
            for y in range(0, self.height, self.square_size):
                square_color = dark_color if i % 2 == 0 else light_color
                rectangle = pygame.Rect(x, y, self.square_size, self.square_size)
                pygame.draw.rect(surface=self.grid_surface, color=square_color, rect=rectangle)
                i += 1
            i += 1

    def draw_grid(self, screen):
        screen.blit(self.grid_surface, (0, 0))
