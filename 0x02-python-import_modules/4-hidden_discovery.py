#!/usr/bin/python
if __name__ == "__main__":
    import hidden_4

    module = dir(hidden_4.pyc)
    for i in len(module):
        if i[0] != "_":
            print("{}.format(i)")
