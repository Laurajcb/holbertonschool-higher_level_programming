#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Method to write in a file and returns the
    number of characters written:
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
