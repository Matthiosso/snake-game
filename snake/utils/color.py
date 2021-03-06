import enum
import random


class Color(enum.Enum):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 102)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)

    @staticmethod
    def get_random_value():
        return random.choice(list(Color)).value
