import json
import logging
import re
from base64 import b64encode

from ..test.conftest import flask_connection


def test_page_404(flask_connection):
    response = flask_connection.get(
        "/random_route",
    )
    assert response.status_code == 404


def test_homepage(flask_connection):
    response = flask_connection.get(
        "/",
    )
    response
    print(f"{str(response.data)}")
    assert response.status_code == 302


def test_status(flask_connection):
    response = flask_connection.get(
        "/status",
    )
    response
    print(f"{str(response.data)}")
    assert response.status_code == 200


# def test_docs(flask_connection):
# response = flask_connection.post(
#     "/api/v1/games",
#     json={"name": "Fortnite 43", "price": 71.7, "space": 1073741824},
#     content_type="application/json"
# )
# response
# print(f"{str(response.data)}")
# assert response.status_code == 200
