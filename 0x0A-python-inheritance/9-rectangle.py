#!/usr/bin/python3
"""
Module that provides a geometry classes
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """calculate the area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'
