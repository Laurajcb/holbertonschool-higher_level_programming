#!/usr/bin/python3
def islower(c):
    ord_char = ord(c)
    if ord_char < 97 and ord_char < 123:
        return True
    return False
