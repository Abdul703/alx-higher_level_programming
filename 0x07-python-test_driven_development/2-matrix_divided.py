#!/usr/bin/python3
"""
This module provide function that manipulate matrix

Functions:
- matrix_divided(matrix, div): divides element of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides elements of a matrix

    Parameters:
    - matrix (list): the matrix
    - div (int): number to divide with

    Return:
    list: new list with elements been divided
    """

    new_matrix = []
    row_size = len(matrix[0])

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for n in row:
            if type(n) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
of integers/floats"
                )
            new_row.append(round(n / div, 2))
        new_matrix.append(new_row)
    return new_matrix
