import random

from ..utils.generate_games import generate


def test_generate_game():
    games = generate(10)
    assert len(games) == 10
    assert type(games[random.randint(0, 10)]["space"]) == int
    assert type(games[random.randint(0, 10)]["name"]) == str
    assert type(games[random.randint(0, 10)]["price"]) == float
