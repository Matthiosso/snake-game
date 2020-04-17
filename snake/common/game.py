import pygame
from snake.common.board import Board
from snake.utils.color import Color
from snake.utils.direction import Direction
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
        self.board = Board(800, 600, 10, 10)
        self.snake = Snake(self.board.width/2, self.board.height/2)
        self.food = Food(self.board.width, self.board.height, self.board.snake_block)

        game_over = False
        game_close = False
        game_paused = False
        direction = None

        clock = pygame.time.Clock()

        while not game_over:
            while game_close:
                self.board.fill_white()
                self.board.message("You Lost (Score: {})! Press Q-Quit or C-Play Again".format(self.snake.size),
                                   Color.RED)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.start()
                    if event.type == pygame.QUIT:
                        game_over = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_paused = not game_paused
                    elif not game_paused:
                        new_direction = Direction.from_pygame_command(event.key)

                        if new_direction is not None and \
                                (direction is None or self.snake.size < 2 or
                                 not Direction.kept_same_direction(direction, new_direction)):
                            direction = new_direction
            if not game_paused:
                if self.snake.headx() >= self.board.width or self.snake.headx() < 0 \
                        or self.snake.heady() >= self.board.height or self.snake.heady() < 0:
                    game_close = True

                self.board.fill_white()

                if direction is not None:
                    if not self.snake.move(direction.scaled_value(self.board.snake_block)):
                        game_close = True

                if self.snake.headx() == self.food.pos_x and self.snake.heady() == self.food.pos_y:
                    self.board.message('Yummy !', Color.BLUE)
                    self.snake.grow_up()
                    self.food = Food(self.board.width, self.board.height, self.board.snake_block)
                self.draw()
                pygame.display.update()

            clock.tick(self.board.snake_speed)

        pygame.time.wait(5)

        pygame.quit()
        quit()

    def draw(self):
        self.board.draw(self.snake)
        self.board.draw(self.food)
        self.board.score(self.snake.size)
