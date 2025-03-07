import pytest
from calculator import add, subtract


@pytest.fixture
def calculator_setup():
    print("Setting up the Enviornment")
    return {}


def test_add(calculator_setup):
    assert add(3, 4) == 7


def test_subtraction(calculator_setup):
    assert subtract(5, 4) == 1
