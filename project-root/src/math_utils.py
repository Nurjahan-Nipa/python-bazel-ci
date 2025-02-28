"""
math_utils.py

This module provides basic mathematical operations.
"""


def add(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first number."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divides the first number by the second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
