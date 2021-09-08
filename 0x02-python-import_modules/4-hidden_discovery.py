#!/usr/bin/python
if __name__ == "__main__":
    import hidden_4

    module = dir(hidden_4)
    for i in module:
        if i[0] != "_":
            print("{}".format(i))
    
