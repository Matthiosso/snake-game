import pygame
from snake.common.board import Board
from snake.common.color import Color
from snake.common.direction import Direction
from snake.common.food import Food
from snake.common.snake import Snake


class Game:

    def __init__(self):
        self.game = 'toto'
        self.board = None
        self.snake = None
        self.food = None

    def start(self):
        pygame.init()
        pygame.display.set_caption('Snake game by Matthiosso')
        self.board = Board(800, 600, 10, 30)
        self.snake = Snake(self.board.width/2, self.board.height/2)
        self.food = Food(self.board.width, self.board.height, self.board.snake_block)

        game_over = False
        game_close = False
        direction = None

        clock = pygame.time.Clock()

        while not game_over:

            while game_close:
                self.board.fill_white()
                self.board.message("You Lost! Press Q-Quit or C-Play Again", Color.RED)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.start()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    new_direction = Direction.from_pygame_command(event.key)
                    if new_direction is not None:
                        direction = new_direction
            if self.snake.pos_x >= self.board.width or self.snake.pos_x < 0 \
                    or self.snake.pos_y >= self.board.height or self.snake.pos_y < 0:
                game_close = True

            self.move_snake(direction)

            self.board.fill_white()
            self.board.draw(Color.BLACK, self.snake)
            self.board.draw(Color.BLUE, self.food)
            if self.snake.pos_x == self.food.pos_x and self.snake.pos_y == self.food.pos_y:
                self.board.message('Yummy !', Color.BLUE)
            pygame.display.update()

            clock.tick(self.board.snake_speed)

        pygame.time.wait(5)

        pygame.quit()
        quit()

    def move_snake(self, direction):
        if direction is not None:
            self.snake.move(direction.scaled_value(self.board.snake_block))

