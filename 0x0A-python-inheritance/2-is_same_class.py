#!/usr/bin/python3
"""
Module that provide function that check if object is an instance of a class
"""


def is_same_class(obj, a_class):
    """check if object is an instance of a class

    Args:
        obj (object): object to check
        a_class (class): class to check on

    Returns:
        True if is instance otherwise False
    """
    return type(obj) == a_class
