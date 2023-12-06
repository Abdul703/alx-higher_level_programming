#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    func = lambda x: x**2
    return [list(map(func, row)) for row in matrix]
