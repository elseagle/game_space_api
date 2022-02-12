import pytest

from ..app import create_app


@pytest.fixture(scope="module")
def flask_connection():
    flask_app = create_app()
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope="session")
def get_games():
    games = [
        {"name": "FIFA22", "price": "500.92", "space": 2390222111},
        {"name": "FIFA21", "price": "100.99", "space": 4392221110},
        {"name": "Vanguard", "price": "600.12", "space": 2390232111},
        {"name": "Last of Us", "price": "50.92", "space": 1024678290},
        {"name": "Ghost", "price": "400.42", "space": 3290212191},
    ]
    return games


@pytest.fixture(scope="session")
def get_pen_drive_space(get_games):
    pen_drive_space = sum([x["space"] for x in get_games])
    return pen_drive_space
