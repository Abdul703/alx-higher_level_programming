#!/usr/bin/python3
"""
This module provide function that print square

Functions:
- print_square(size): Print square with character #.
"""


def print_square(size):
    """
    Print square with character #

    Parameters:
    - size (int): the size of square
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
