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


def test_homepage_redirect(flask_connection):
    response = flask_connection.get(
        "/",
    )
    response
    assert response.status_code == 302


def test_sawagger_url(flask_connection):
    response = flask_connection.get(
        "/static/swagger.json",
    )
    response
    assert response.status_code == 200


def test_docs_redirect(flask_connection):
    response = flask_connection.get(
        "/",
    )
    response
    assert response.status_code == 302

