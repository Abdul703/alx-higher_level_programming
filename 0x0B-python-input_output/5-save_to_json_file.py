#!/usr/bin/python3
"""JSON serialize/deserialize"""
import json


def save_to_json_file(my_obj, filename):
    """save json serialiase object to a file

    Args:
        my_obj (obj): object to serialise "".
        filename (str): name of the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
