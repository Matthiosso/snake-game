import random


class Food:

    def __init__(self, board_width, board_height):
        self.pos_x = round(random.randrange(0, board_width))
        self.pos_y = round(random.randrange(0, board_height))
