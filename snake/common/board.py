import pygame

from snake.utils.color import Color
from snake.common.food import Food
from snake.common.snake import Snake


class Board:
    def __init__(self, width, height, snake_block=10, snake_speed=30):
        self.width = width
        self.height = height
        self.snake_block = snake_block
        self.snake_speed = snake_speed

        self.board = pygame.display.set_mode((self.width, self.height))
        self.fontsize = 30
        self.font_style = pygame.font.SysFont(None, self.fontsize)

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color.value)
        self.board.blit(mesg, [0, 0])

    def score(self, score):
        mesg = self.font_style.render('Score: {}'.format(score), True, Color.RED.value)
        self.board.blit(mesg, [0, self.height-self.fontsize])

    def fill_white(self):
        self.board.fill(Color.WHITE.value)

    def draw(self, obj):
        if isinstance(obj, Snake):
            for body_part in obj.body:
                pygame.draw.rect(self.board, Color.GREEN.value, [body_part[0], body_part[1],
                                                           self.snake_block, self.snake_block])
        elif isinstance(obj, Food):
            pygame.draw.rect(self.board, Color.BLUE.value, [obj.pos_x, obj.pos_y,
                                                       self.snake_block, self.snake_block])
