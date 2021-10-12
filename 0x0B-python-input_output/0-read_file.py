#!/usr/bin/python3
"""Function that reads a text file (UTF8) & prints it to stdout"""


def read_file(filename=""):
    """" Method to read a file"""
    with open(filename, mode="r", encoding="utf-8") as read_file:
        text = read_file.read()
        print(text, end="")
