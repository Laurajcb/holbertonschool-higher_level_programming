#!/usr/bin/python3
"""function that returns the JSON"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object(string)
    Encode(dumps)
    """
    return json.dumps(my_obj)
