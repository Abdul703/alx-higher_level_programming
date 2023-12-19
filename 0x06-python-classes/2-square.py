#!/usr/bin/python3
"""
A module for square-related operations.
"""


class Square:
    """
    a class representing square.

    Attributes:
    - __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initiate the size of the square object.

        Args:
            size (int): size of the square object created.
        """

        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")

        self.__size = size
