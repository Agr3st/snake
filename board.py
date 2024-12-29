import pygame

class Board:
    def __init__(self, width, height, square_size):
        self.width = width
        self.height = height
        self.square_size = square_size

    def draw_grid(self, screen, light_color, dark_color):
        i = 0
        for x in range(0, self.width, self.square_size):
            for y in range(0, self.height, self.square_size):
                square_color = dark_color if i % 2 == 0 else light_color
                rectangle = pygame.Rect(x, y, self.square_size, self.square_size)
                pygame.draw.rect(surface=screen, color=square_color, rect=rectangle)
                i += 1
            i += 1