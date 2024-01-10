#!/usr/bin/python3
"""Python file I/O module"""


def append_write(filename="", text=""):
    """append or write to a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): text to append. Defaults to "".
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
