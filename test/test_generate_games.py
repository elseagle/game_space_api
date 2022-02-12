from ..utils.generate_games import generate


def test_generate_game():
    games = generate(10)
    assert len(games) == 10
    assert type(games[0]["space"]) == int
    assert type(games[0]["name"]) == str
    assert type(games[0]["price"]) == float
