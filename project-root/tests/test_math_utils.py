"""Importing pyetst library and Importing necessary functions"""

import pytest
from src.math_utils import add, subtract, multiply, divide


def test_add():
    """
    Tests the add function.
    """
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10


def test_subtract():
    """
    Tests the subtract function.
    """
    assert subtract(3, 2) == 1
    assert subtract(5, 10) == -5
    assert subtract(0, 0) == 0
    assert subtract(-3, -3) == 0


def test_multiply():
    """
    Tests the multiply function.
    """
    assert multiply(3, 2) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(-4, -4) == 16


def test_divide():
    """
    Tests the divide function.
    """
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(7, 2) == 3.5  # Ensure float division works

    # Test division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)
