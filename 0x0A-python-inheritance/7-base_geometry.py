#!/usr/bin/python3
"""
Empty class BaseGeometry
"""


class BaseGeometry:
    """Define class BaseGeometry
    """
    def area(self):
        """Define an exception for area method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Define an exception for value method
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
