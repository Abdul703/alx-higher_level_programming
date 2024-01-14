#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that performs some rectangle operations

    Args:
        Base (class): Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise Rectangle instance

        Args:
            height (int): height of the rectangle
            width (int): width of the rectangle
            x (int, optional): . Defaults to 0.
            y (int, optional): . Defaults to 0.
            id (int, optional): id of the rectangle. Defaults to None.
        """
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

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
        if value <= 0:
            raise ValueError("height must be > 0")

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
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def x(self):
        """Getter for the x coordinate

        Returns:
            int: x cordinate
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate

        Args:
            value (int): value of the x

        Raises:
            TypeError: value is not integer
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter for the y coordinate

        Returns:
            int: y coordinate
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate

        Args:
            value (int): value of the y

        Raises:
            TypeError: value is not integer
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """compute the area of rectangle

        Returns:
            int: area of rectangle
        """
        return self.width * self.height

    def display(self):
        """display the rectangle in #"""

        for k in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """print the Rectangle information

        Returns:
            str: Rectangle data
        """
        x, y = self.x, self.y
        return f"[Rectangle] ({self.id}) {x}/{y} - {self.width}/{self.height}"
    
    def update(self, *args, **kwargs):
        """Update Rectangle Attributes"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)

        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """object representation of the rectangle

        Returns:
            dict: rectangle data in dict form
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }
