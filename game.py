import pygame
from config import *
from apple import Apple
from snake import Snake
from board import Board
from random import choice

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.clock_tick_limit = CLOCK_TICK_LIMIT
        self.board = Board()
        self.apple = Apple()
        self.snake = Snake()

        self.running = True

    def handle_events(self):
        """Handle user input and events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        self.snake.set_direction(keys)

    def update(self):
        """Update game state."""
        self.snake.move()
        self.running = not self.check_collisions()

    def check_collisions(self):
        """
        Check for collisions between the snake and apple, walls, or itself.
        :return: True if there is a collision between snake and walls or itself, otherwise False
        """
        # Collision between the snake and an apple
        if self.snake.get_head_coords() == tuple(self.apple.get_coords()):
            self.snake.eat_apple()
            apple_coords = self.generate_random_coords(self.snake.get_coords())
            self.apple.set_coords(apple_coords)
            # self.clock_tick_limit += 0.2

        # Collision between the snake and walls or itself
        return self.snake.check_collision()

    def render(self):
        """Render all game elements."""
        self.board.draw_grid(self.screen)
        self.apple.draw(self.screen)
        self.snake.draw(self.screen)
        pygame.display.flip()

    @staticmethod
    def generate_random_coords(snake_coords):
        """Generate random coordinates for the apple that don't overlap with the snake."""
        while True:
            x = choice(range(0, SCREEN_WIDTH, SQUARE_SIZE))
            y = choice(range(0, SCREEN_WIDTH, SQUARE_SIZE))
            if (x, y) not in snake_coords:
                break
        return [x, y]

    def run(self):
        """Main game loop."""
        while self.running:
            self.clock.tick(self.clock_tick_limit)
            self.handle_events()
            self.update()
            if self.running:
                self.render()

        pygame.quit()
