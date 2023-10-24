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

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
