import pygame
from config import *
from apple import Apple
from snake import Snake
from board import Board

if __name__ == '__main__':
    # inicjalizuje wszystkie podmoduły pygame
    pygame.init()
    # zwraca uchwyt do powierzchni wyświetlej (display Surface)
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    # obiekt pomagający śledzić czas i kontrolować framerate
    clock = pygame.time.Clock()

    # utwórz planszę
    board = Board()
    # utwórz jabłko
    apple = Apple(coords=(SQUARE_SIZE*5, SQUARE_SIZE*5))
    # utwórz snake
    snake = Snake()

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
        snake.set_direction(keys)
        snake.move()
        snake.check_collision(apple.get_coords())

        # Rysuj siatkę
        board.draw_grid(screen)
        # rysuj jabłko
        apple.draw(screen)
        # rysuj węża
        snake.draw(screen)
        # Aktualizuj ekran
        pygame.display.flip()
