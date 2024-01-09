#!/usr/bin/python3
"""
Module that provides a geometry classes
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle class that inherit from Rectangle

    Args:
        Rectangle (class): parent class
    """

    def __init__(self, size):
        """initialiaze size

        Args:
            size (int): the size of the square
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """compute the area of square

        Returns:
            int: area of square
        """
        return self.__size**2
