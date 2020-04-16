#!/usr/bin/env python

from snake.common.game import Game


def run():
    game = Game()
    game.start()
    print('Jeu lancé')
    return game.game
