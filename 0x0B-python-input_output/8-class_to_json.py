#!/usr/bin/python3
"""Returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """
    Returns the dictionary description with
    simple data structure,serialization of an object
    """
    return obj.__dict__
