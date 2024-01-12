#!/usr/bin/python3
"""Base class for all subsequent classes"""


class Base:
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialise the object id

        Args:
            id (int, optional): an id number of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
