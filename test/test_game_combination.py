from ..test.conftest import get_games, get_pen_drive_space
from ..utils.game_combination import get_game_combination


def test_max_space(get_games, get_pen_drive_space):
    game_combination = get_game_combination(get_games, get_pen_drive_space)
    assert len(game_combination["games"]) == 5
    assert get_pen_drive_space == game_combination["total_space"]


def test_below_total_space(get_games, get_pen_drive_space):
    game_combination = get_game_combination(get_games, get_pen_drive_space - 103000345)
    assert len(game_combination["games"]) < 5
    assert get_pen_drive_space >= game_combination["total_space"]
