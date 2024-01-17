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

    def area(self):
        """compute the area of rectangle

        Returns:
            int: area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """compute the perimeter of rectangle

        Returns:
            int: perimeter of rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """print the rectangle with the character #"""

        if self.height == 0 or self.width == 0:
            return ""
        s = ("#" * self.width + "\n") * self.height
        return s[:-1]

    def __repr__(self):
        """duplicate of the class object

        Returns:
            object: duplicate of the object
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """message to print when an object is deleted"""
        print("Bye rectangle...")
