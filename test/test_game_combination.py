from ..test.conftest import get_games, get_pen_drive_space
from ..utils.game_combination import get_game_combination
def test_get_game_combination(get_games, get_pen_drive_space):
    game_combination = get_game_combination(get_games, get_pen_drive_space)

    assert len(game_combination["games"]) == 5