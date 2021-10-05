#!/usr/bin/python3
"""
Function that adds 2 integers a and b,
these must be integers or floats, otherwise
raise a TypeError exception
"""


def add_integer(a, b=98):
    """ Add two integers (a and b)
    a and b should be int or float type
    return int addition """

    if type(a) is int or type(a) is float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return int(a + b)
