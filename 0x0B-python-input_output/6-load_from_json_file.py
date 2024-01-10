#!/usr/bin/python3
"""JSON serialize/deserialize"""
import json


def load_from_json_file(filename):
    """import json object from json file

    Args:
        filename (str): name of the file.

    Returns:
        deserialise json object
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
