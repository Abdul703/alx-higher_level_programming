#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherit from Rectangle class

    Args:
        Rectangle (class): Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialise Rectangle instance

        Args:
            size (int): size of the rectangle
            x (int, optional): . Defaults to 0.
            y (int, optional): . Defaults to 0.
            id (int, optional): id of the rectangle. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print the Square information

        Returns:
            str: Square data
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Getter for the size

        Returns:
            int: rectangle size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the rectangle

        Args:
            value (int): value of the size

        Raises:
            TypeError: value is not integer
            ValueError: value is less than or equal to 0
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square Attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
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
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }
