#!/usr/bin/python3
"""
Module that provides a geometry classes
"""


class BaseGeometry:
    """A geometry base class"""

    def area(self):
        """area of the provided shape"""
        raise Exception("area() is not implemented")

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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate the area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"


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
