
class Snake:

    def __init__(self, pos_x, pos_y, size=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size

    def move(self, direction):
        if len(direction) < 2:
            raise Exception('La direction donnée est incorrecte : ' + direction)
        self.pos_x += direction[0]
        self.pos_y += direction[1]
