#!/usr/bin/python3
"""
Module that provides a geometry class
"""


class BaseGeometry:
    """A geometry class"""

    def area(self):
        """area of the provided shape"""
        raise Exception('area() is not implemented')
