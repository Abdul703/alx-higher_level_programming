#!/usr/bin/python3
"""
This module provides a simple calculator with basic arithmetic functions.

Functions:
- add_numbers(a, b): Adds two numbers.
"""


def add_numbers(a, b=98):
    """
    Adds two numbers.

    Parameters:
    - a (int): The first number.
    - b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
