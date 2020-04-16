import enum
import pygame.constants


class Direction(enum.Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

    @staticmethod
    def from_pygame_command(command):
        pygame_command_mapping = {
            pygame.K_LEFT: Direction.LEFT,
            pygame.K_RIGHT: Direction.RIGHT,
            pygame.K_UP: Direction.UP,
            pygame.K_DOWN: Direction.DOWN
        }
        return pygame_command_mapping.get(command, None)

    def scaled_value(self, scale):
        return tuple([scale*x for x in self.value])
