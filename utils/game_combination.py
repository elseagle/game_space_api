from decimal import Decimal


def get_game_combination(game_list, pen_drive_space):
    total_value = 0.0
    best_game_combination = {
        "games": [],
        "total_space": 0,
        "remaining_space": pen_drive_space,
        "total_value": total_value,
    }

    for i in range(len(game_list) + 1):
        for j in range(i):
            sub_list = game_list[j:i]

            if (
                pen_drive_space - sum([x["space"] for x in sub_list]) >= 0
                and sum([Decimal(str(x["price"])) for x in sub_list]) > total_value
            ):
                total_value = sum([Decimal(str(x["price"])) for x in sub_list])

                best_game_combination = {
                    "games": game_list[j:i],
                    "total_space": sum([x["space"] for x in sub_list]),
                    "remaining_space": pen_drive_space
                    - sum([x["space"] for x in sub_list]),
                    "total_value": float(total_value),
                }

    return best_game_combination
