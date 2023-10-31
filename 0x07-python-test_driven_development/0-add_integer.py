#!/usr/bin/python3
"""This module defines a function for integer addition."""

def add_integer(a, b=98):
    """
    Return the integer addition of two numbers.

    Arguments:
    a (int or float): The first number.
    b (int or float): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b, as an integer.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a and b must be integers or floats")
    
    return int(a) + int(b)
