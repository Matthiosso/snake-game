import random


class Food:

    def __init__(self, board_width, board_height, snake_block):
        self.pos_x = round(random.randrange(0, (board_width - snake_block) / 10.0) * 10.0)
        self.pos_y = round(random.randrange(0, (board_height - snake_block) / 10.0) * 10.0)
