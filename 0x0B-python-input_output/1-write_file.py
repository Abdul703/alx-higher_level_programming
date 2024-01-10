#!/usr/bin/python3
"""Python I/O module"""


def write_file(filename="", text=""):
    """write to a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): text to write. Defaults to "".

    Returns:
        number of bytes write
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
