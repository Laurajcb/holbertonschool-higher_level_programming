#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ord_str = ord(c)
        if ord_str > 97 and ord_str < 122:
            ord_str -= 32
    print("{}".format(ord_str), end='')
    print(end='\n')