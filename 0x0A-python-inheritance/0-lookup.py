#!/usr/bin/python3
"""
Module that provide function to returns attributes and methods of an object
"""


def lookup(obj):
    """returns attributes and methods of an object

    Args:
        obj (object): object to list its attributes and methods

    Returns:
        list: ttributes and methods of an object
    """
    return dir(obj)
