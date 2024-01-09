#!/usr/bin/python3
"""
Module that provides a geometry classes
"""


class BaseGeometry:
    """A geometry base class"""

    def area(self):
        """area of the provided shape"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validate value

        Args:
            name (str): name of the value
            value (int): the integer value of name

        Raises:
            TypeError: if value is not an int
            ValueError: value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """Rectangle class that inherit from BaseGeometry

    Args:
        BaseGeometry (class): parent class
    """
    def __init__(self, width, height):
        """initialise object variables

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)
