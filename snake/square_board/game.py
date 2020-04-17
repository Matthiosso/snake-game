import pygame

from snake.square_board.items.snake import Snake
from snake.square_board.items.food import Food
from snake.utils.color import Color
from snake.utils.direction import Direction


class SquareBoardGame:
    def __init__(self, rows=20, cols=25, width=30, height=30, margin=3, clock_fps=10):

        self.cols = cols
        self.rows = rows

        self.width = width
        self.height = height

        self.margin = margin
        self.score_band_height = 30

        self.window_size = [self.cols*self.width + self.margin,
                            self.rows*self.height + self.margin + self.score_band_height]
        self.screen = None
        self.clock_fps = clock_fps

        self.background_color = Color.BLACK.value
        self.font_size = self.score_band_height

        self.grid = [[Color.WHITE.value for i in range(self.rows)]
                     for j in range(self.cols)]

        self.food = None
        self.snake = None

    def start(self):
        pygame.init()
        pygame.display.set_caption('Snake game by Matthiosso')
        self.screen = pygame.display.set_mode(self.window_size)
        self.font_style = pygame.font.SysFont(None, self.font_size)

        self.reset_game()
        self.play()

        self.end()

    def reset_game(self):
        self.snake = Snake(int(self.cols / 2), int(self.rows / 2))
        self.food = Food(self.cols, self.rows)

    def draw(self):
        self.screen.fill(self.background_color)
        for col in range(len(self.grid)):
            for row in range(len(self.grid[col])):
                pygame.draw.rect(self.screen, self.grid[col][row], [(self.width * col + self.margin),
                                                                    (self.height * row + self.margin),
                                                                    self.width-self.margin,
                                                                    self.height-self.margin])
        for snake_part in self.snake.body:
            pygame.draw.rect(self.screen, Color.GREEN.value, [self.width * snake_part[0] + self.margin,
                                                              self.height * snake_part[1] + self.margin,
                                                              self.width-self.margin,
                                                              self.height-self.margin])
        pygame.draw.rect(self.screen, Color.RED.value, [self.width * self.food.pos_x + self.margin,
                                                        self.height * self.food.pos_y + self.margin,
                                                        self.width-self.margin,
                                                        self.height-self.margin])
        self.message('Score: {}'.format(self.snake.size))
        pygame.display.update()

    def message(self, message):
        mesg = self.font_style.render('{}'.format(message), True, Color.WHITE.value)
        self.screen.blit(mesg, [0, self.rows * self.height + self.margin])

    def play(self):
        game_over = False
        game_close = False
        direction = None
        clock = pygame.time.Clock()
        while not game_over:
            while game_close:
                self.screen.fill(Color.BLACK.value)
                self.message("You Lost (Score: {})! Press Q-Quit or C-Play Again".format(self.snake.size))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            return self.end()
                        if event.key == pygame.K_c:
                            self.reset_game()
                            game_close = False
                            direction = None
                    if event.type == pygame.QUIT:
                        return self.end()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.end()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                    elif event.key == pygame.K_x:
                        # Ici: En cliquant sur X on change la couleur du tableau
                        new_color = Color.get_random_value()
                        while new_color == Color.WHITE.value or new_color == self.background_color:
                            new_color = Color.get_random_value()
                        self.background_color = new_color
                    else:
                        new_direction = Direction.from_pygame_command(event.key)
                        if new_direction is not None and \
                                (direction is None or self.snake.size < 2 or
                                 not Direction.kept_same_direction(direction, new_direction)):
                            direction = new_direction
            if self.snake.headx() >= self.cols or self.snake.headx() < 0 \
                    or self.snake.heady() >= self.rows or self.snake.heady() < 0:
                game_close = True
            if direction is not None:
                if not self.snake.move(direction.value):
                    game_close = True
            if self.snake.headx() == self.food.pos_x and self.snake.heady() == self.food.pos_y:
                self.snake.grow_up()
                self.food = Food(self.cols, self.rows)
                while self.snake_and_food_collapse():
                    self.food = Food(self.cols, self.rows)
            clock.tick(self.clock_fps)
            self.draw()

    def end(self):
        pygame.quit()

    def snake_and_food_collapse(self):
        for snake_part in self.snake.body:
            if snake_part[0] == self.food.pos_x and snake_part[1] == self.food.pos_y:
                return True
        return False
