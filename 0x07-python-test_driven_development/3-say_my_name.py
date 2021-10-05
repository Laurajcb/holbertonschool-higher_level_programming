#!/usr/bin/python3
"""
Write a function that prints My name is <first name> <last name>
my name must be an string othewise 
raise TypeError message
"""
def say_my_name(first_name, last_name=""):
    """Print the name conformed by first name and
    lasta name altogheter
    """
    if type(first_name)is not str:
        raise TypeError("first_name must be a string")
    if type(last_name)is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
