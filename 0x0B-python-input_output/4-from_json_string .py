#!/usr/bin/python3
"""JSON serialize/deserialize"""
import json


def from_json_string(my_str):
    """deserialiase a string to json object

    Args:
        my_str (str): string to deserialise "".

    Returns:
        the deserialize object
    """
    return json.loads(my_str)
