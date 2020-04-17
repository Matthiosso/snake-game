import pygame

from snake.utils.color import Color


class SquareBoardGame:
    def __init__(self, rows=10, cols=10, width=50, height=50, margin=3, clock_fps=30):

        self.cols = cols
        self.rows = rows

        self.width = width
        self.height = height

        self.margin = margin

        self.window_size = [self.cols*self.width + self.margin, self.rows*self.height + self.margin + 50]
        self.screen = None
        self.clock_fps = clock_fps

        self.background_color = Color.BLACK.value

        self.grid = [[Color.WHITE.value for i in range(self.rows)]
                     for j in range(self.cols)]

    def start(self):
        pygame.init()
        pygame.display.set_caption('Snake game by Matthiosso')
        self.screen = pygame.display.set_mode(self.window_size)

        self.listen_events()

        self.end()

    def draw(self):
        self.screen.fill(self.background_color)
        for col in range(len(self.grid)):
            for row in range(len(self.grid[col])):
                pygame.draw.rect(self.screen, self.grid[col][row], [(self.width * col + self.margin),
                                                                    (self.height * row + self.margin),
                                                                    self.width-self.margin,
                                                                    self.height-self.margin])
        pygame.display.update()

    def listen_events(self):
        game_over = False
        clock = pygame.time.Clock()
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                    if event.key == pygame.K_x:
                        # Ici: En cliquant sur X on change la couleur du tableau
                        new_color = Color.get_random_value()
                        while new_color == Color.WHITE.value or new_color == self.background_color:
                            new_color = Color.get_random_value()
                        self.background_color = new_color
            clock.tick(self.clock_fps)
            self.draw()

    def end(self):
        pygame.quit()
