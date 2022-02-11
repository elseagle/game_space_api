from flask import Blueprint, request, jsonify, render_template
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from jsonschema import validate as json_validate

try:
    from app import db
    from utils.game_schema import validator, game_schema
    from utils.game_combination import get_game_combination
except ImportError:
    from ..app import db
    from ..utils.game_schema import validator, game_schema
    from ..utils.game_combination import get_game_combination

main = Blueprint("main", __name__, url_prefix="/api/v1")


@main.route("/status", methods=["GET", "HEAD"])
def status():
    try:
        db.session.execute(text("SELECT 1"))
        health_status = {"database": "healthy"}
        status = 200
    except:
        health_status = {"database": "unhealthy"}
        status = 502

    return jsonify(health_status), status


@main.route("/games", methods=["POST"])
def save_game():
    data = request.json

    if not data:
        return (
            jsonify(
                {"status": "error", "message": "please input a valid request body"}
            ),
            403,
        )

    try:
        json_validate(instance=data, schema=game_schema)
    except Exception as e:
        return (
            jsonify({"status": "error", "data": data, "message": str(e.message)}),
            400,
        )

    try:
        validator(data)
        name, price, space = data["name"], data["price"], data["space"]

    except Exception as e:
        return jsonify({"status": "error", "data": data, "message": str(e)}), 400

    try:
        db.engine.execute(
            f"""
        INSERT INTO game(name, price, space) VALUES 
        ('{name}', {price}, {space});
        """
        )
    except IntegrityError:
        return (
            jsonify(
                {
                    "status": "error",
                    "data": data,
                    "message": "A game with that name already exists in the database",
                }
            ),
            400,
        )

    return jsonify(data), 201


@main.route("/best_value_games", methods=["POST"])
def get_best_value_games():
    pen_drive_space = request.args.get("pen_drive_space")
    try:
        pen_drive_space = int(str(pen_drive_space))

        if pen_drive_space < 0:
            raise ValueError("Negative integer")
    except ValueError:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": f"Pen drive space of {pen_drive_space} bytes is not a positive integer",
                }
            ),
            400,
        )

    records = db.engine.execute(
        f"""
        SELECT * FROM game
        WHERE space <= {pen_drive_space}
        ORDER BY space ASC;
    """
    )
    print([record for record in db.engine.execute("SELECT * FROM game;")])
    print("\n")
    game_list = [
        {"name": record[1], "price": record[2], "space": record[3]}
        for record in records
    ]
    print(game_list)

    return jsonify(get_game_combination(game_list, pen_drive_space)), 200
