#!/usr/bin/python3
"""Base class for all subsequent classes"""
import json


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

    def to_json_string(list_dictionaries):
        """serialize an object

        Args:
            list_dictionaries (dict): an object to serialize

        Returns:
            str: serialized object
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)
