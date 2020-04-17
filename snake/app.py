#!/usr/bin/env python

from snake.square_board.game import SquareBoardGame


def run():
    game = SquareBoardGame()
    game.start()
    print('Jeu lancé')