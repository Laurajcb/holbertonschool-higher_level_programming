#!/usr/bin/python3
"""
Write a function that prints a text with 2 new
lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    for deli in ['.', '?', ':']:
        text = str(deli + "\n\n").join(ch.strip() for ch in text.split(deli))
    print("{}".format(text))
