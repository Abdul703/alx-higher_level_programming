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

    def area(self):
        """
        compute the area of the square

        Returns:
            int: area of the square
        """
        return self.__size**2

    @property
    def size(self):
        """
        getter for the size

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the value of the size to new value

        Args:
            value (int): new value for the size
        """
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        print square shape using #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
