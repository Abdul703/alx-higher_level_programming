#!/usr/bin/python3
"""Module that manipulate list"""


class MyList(list):
    """Inherit from list and add additional methods

    Args:
        list (object): built-in list object
    """

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
