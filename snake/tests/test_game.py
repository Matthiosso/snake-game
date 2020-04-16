import pytest

from snake.common.game import Game


@pytest.fixture
def my_test_game():
    return Game()


def test_game(my_test_game):
    assert my_test_game.game == "toto"
