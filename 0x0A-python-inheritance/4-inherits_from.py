#!/usr/bin/python3
"""
Module that provides a function to check if object is an instance of a class
    that inherited specified class.
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class
    that inherited specified class.

    Args:
        obj (object): Object to check.
        a_class (class): Class to check against.

    Returns:
        bool: True if the object is an instance of the class inherited class,
        otherwise False.
    """
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    return False
