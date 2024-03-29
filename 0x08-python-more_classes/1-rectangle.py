#!/usr/bin/python3
"""
This moudule provide Rectangle class
"""


class Rectangle:
    """
    Rectangle Class
    """

    def __init__(self, width=0, height=0):
        """initialise Rectangle instance

        Args:
            height (int): height of the rectangle
            width (int): width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Getter for the height

        Returns:
            int: rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
            value (int): value of the height

        Raises:
            TypeError: value is not integer
            ValueError: value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """Getter for the width

        Returns:
            int: rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value (int): value of the width

        Raises:
            TypeError: value is not integer
            ValueError: value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
