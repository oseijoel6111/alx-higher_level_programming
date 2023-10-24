#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.

    Note:
        The size attribute is made private to control the type and value
        of this attribute. You will see in later tasks how to get, update,
        and validate the size value.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square (default is 0).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
