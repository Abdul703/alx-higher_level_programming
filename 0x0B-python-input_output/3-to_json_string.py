#!/usr/bin/python3
"""JSON serialize/deserialize"""
import json


def to_json_string(my_obj):
    """serialiase

    Args:
        my_obj (obj): object to serialise "".

    Returns:
        the serialize object string
    """
    return json.dumps(my_obj)
