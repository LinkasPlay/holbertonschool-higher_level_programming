#!/usr/bin/python3
"""
This module defines a function add_integer that adds two numbers.
It validates the types of the inputs, casts floats to integers,
and raises a TypeError if the inputs are not integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers after validating their types and casting floats to integers.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
