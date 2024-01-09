#!/usr/bin/python3
"""Python I/O module"""


def read_file(filename=""):
    """read a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as f:
        file_data = f.read()
    print(file_data)
