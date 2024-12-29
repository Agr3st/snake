import pygame
from constants import *
from apple import Apple
from snake import Snake
from board import Board

# GAME PARAMETERS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SQUARES_NUM = 20
SQUARE_SIZE = SCREEN_WIDTH // SQUARES_NUM
SQUARE_COLOR_DARK = '#124F11'
SQUARE_COLOR_LIGHT = '#195D16'
SNAKE_START_LENGTH = 3
SNAKE_START_HEAD_CORDS = (0, 0)
SNAKE_COLOR = '#B57533'
SNAKE_HEAD_COLOR = '#FFBB36'
CLOCK_TICK_LIMIT = 7
direction = RIGHT

# PYGAME SETUP
# inicjalizuje wszystkie podmoduły pygame
pygame.init()
# zwraca uchwyt do powierzchni wyświetlej (display Surface)
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
# obiekt pomagający śledzić czas i kontrolować framerate
clock = pygame.time.Clock()

def check_direction(prev_direction, keys):
    if keys[pygame.K_UP]:
        if prev_direction == DOWN:
            return DOWN
        return UP
    elif keys[pygame.K_DOWN]:
        if prev_direction == UP:
            return UP
        return DOWN
    elif keys[pygame.K_RIGHT]:
        if prev_direction == LEFT:
            return LEFT
        return RIGHT
    elif keys[pygame.K_LEFT]:
        if prev_direction == RIGHT:
            return RIGHT
        return LEFT
    else:
        return prev_direction

if __name__ == '__main__':
    # utwórz planszę
    board = Board(SCREEN_WIDTH, SCREEN_HEIGHT, SQUARE_SIZE)
    # utwórz jabłko
    apple = Apple(SQUARE_SIZE)
    # utwórz snake
    snake = Snake(SQUARE_SIZE, SNAKE_START_LENGTH, SNAKE_START_HEAD_CORDS)

    # Wyczyść ekran na czarno
    # screen.fill((0, 0, 0))
    # Rysuj siatkę
    board.draw_grid(screen, SQUARE_COLOR_LIGHT, SQUARE_COLOR_DARK)
    # rysuj jabłko
    apple.draw(screen, 0, 0)
    # rysuj węża
    snake.draw(screen, SNAKE_HEAD_COLOR, SNAKE_COLOR)

    # Aktualizuj ekran
    pygame.display.flip()

    i = 0
    running = True
    while running:
        # This limits the while loop to a max of 60 times per second.
        clock.tick(CLOCK_TICK_LIMIT)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                running = False  # Flag that we are done so we exit this loop

        # sterowanie
        keys = pygame.key.get_pressed()
        direction = check_direction(direction, keys)

        snake.move(direction)

        # Rysuj siatkę
        board.draw_grid(screen, SQUARE_COLOR_LIGHT, SQUARE_COLOR_DARK)
        # rysuj jabłko
        apple.draw(screen, SQUARE_SIZE*3, SQUARE_SIZE*3)
        # rysuj węża
        snake.draw(screen, SNAKE_HEAD_COLOR, SNAKE_COLOR)
        # Aktualizuj ekran
        pygame.display.flip()

        # tymaczosowo
        #i += SQUARE_SIZE
       # if i // SCREEN_WIDTH > 0 or i // SCREEN_HEIGHT > 0:
        #    i = 0