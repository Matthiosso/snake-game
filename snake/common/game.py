import pygame
from snake.common.board import Board
from snake.common.color import Color
from snake.common.direction import Direction
from snake.common.snake import Snake


class Game:

    def __init__(self):
        self.game = 'toto'
        self.board = Board(500, 500, 10, 30)
        self.snake = Snake(self.board.width/2, self.board.height/2)

    def start(self):
        pygame.init()
        pygame.display.set_caption('Snake game by Matthiosso')
        self.board.start()

        game_over = False

        clock = pygame.time.Clock()

        direction = None
        while not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    direction = Direction.from_pygame_command(event.key)
            if self.snake.pos_x >= self.board.width or self.snake.pos_x < 0 \
                    or self.snake.pos_y >= self.board.height or self.snake.pos_y < 0:
                game_over = True
            self.move_snake(direction)
            pygame.display.update()
            clock.tick(self.board.snake_speed)
        self.board.message('You lost', Color.RED.value)
        pygame.display.update()
        pygame.time.wait(5)

        pygame.quit()
        quit()

    def move_snake(self, direction):
        if direction is not None:
            self.snake.move(direction.scaled_value(self.board.snake_block))
        self.board.fill_white()
        self.board.draw(Color.BLACK, self.snake)
