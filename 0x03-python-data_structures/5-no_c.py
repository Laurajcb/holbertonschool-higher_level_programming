#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for char in my_string:
        if char != 67 and char != 97:
            new_str += char
    return new_str
