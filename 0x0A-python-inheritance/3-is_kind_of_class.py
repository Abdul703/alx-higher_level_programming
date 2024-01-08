#!/usr/bin/python3
"""
Module that provides a function to check if object is an instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class.

    Args:
        obj (object): Object to check.
        a_class (class): Class to check against.

    Returns:
        bool: True if the object is an instance of the class, otherwise False.
    """
    return isinstance(obj, a_class)
