
class Snake:

    def __init__(self, pos_x, pos_y, size=1):
        self.body = [[pos_x, pos_y]]
        self.size = size

    def head(self):
        return self.body[-1]

    def headx(self):
        return self.head()[0]

    def heady(self):
        return self.head()[1]

    def move(self, direction):
        if len(direction) < 2:
            raise Exception('La direction donnée est incorrecte : ' + direction)
        self.body.append([self.headx() + direction[0], self.heady() + direction[1]])

        # Supprime la queue lors d'un déplacement sans manger
        if len(self.body) > self.size:
            del self.body[0]

        # Cas du serpent qui se mord la queue
        for body_part in self.body[:-1]:
            if body_part == self.head():
                return False
        return True

    def grow_up(self):
        self.size += 1

    def __str__(self):
        return 'Snake ({}) : {}'.format(self.size, self.body)
