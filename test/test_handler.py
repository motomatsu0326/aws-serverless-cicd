import pytest

from src import handler


def test_hello():
    assert "Hello Serverless !" == handler.hello("","")
