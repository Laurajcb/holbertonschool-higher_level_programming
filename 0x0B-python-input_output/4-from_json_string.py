#!/usr/bin/python3
"""
Function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns an object py represented by a JSON string:
    Decode(loads)
    """
    return json.loads(my_str)
