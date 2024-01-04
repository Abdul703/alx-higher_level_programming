#!/usr/bin/python3
"""
This module provide function that print name

Functions:
- say_my_name(first_name, last_name=""): Print full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print fullname

    Parameters:
    - first_name (str): the first name
    - last_name (str): the last name
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f"My name is {first_name} {last_name}")
