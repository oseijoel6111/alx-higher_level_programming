#!/usr/bin/python3
class Square:
    """
    This is a Square class.

    Attributes:
        __size (int): The size of the square.

    Note:
        The size attribute is made private to control the type and value
        of this attribute. You will see in later tasks how to get, update,
        and validate the size value.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
