import pygame

from snake.common.color import Color


class Board:
    def __init__(self, width, height, snake_block=10, snake_speed=30):
        self.width = width
        self.height = height
        self.snake_block = snake_block
        self.snake_speed = snake_speed

        self.board = None
        self.font_style = None

    def start(self):
        self.board = pygame.display.set_mode((self.width, self.height))
        self.font_style = pygame.font.SysFont(None, 50)

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.board.blit(mesg, [self.width / 2, self.height / 2])

    def fill_white(self):
        self.board.fill(Color.WHITE.value)

    def draw(self, color, snake):

        pygame.draw.rect(self.board, color.value, [snake.pos_x,
                                                   snake.pos_y,
                                                   self.snake_block,
                                                   self.snake_block])
