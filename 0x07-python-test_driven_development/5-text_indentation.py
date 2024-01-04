#!/usr/bin/python3
"""
This module provide function that print manipulated text

Functions:
- text_indentation(text): Prints a text with 2 new lines after
                          each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
    - text (str): the text to print
    """

    text = text.replace(".", "\n\n").\
        replace("?", "\n\n").\
        replace(":", "\n\n")
    print(text, end="")
