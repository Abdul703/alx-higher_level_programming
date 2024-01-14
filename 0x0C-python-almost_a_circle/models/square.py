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
        self.size = size
    
    def __str__(self):
        """print the Square information

        Returns:
            str: Square data
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
    