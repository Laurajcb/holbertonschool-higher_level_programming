#!/usr/bin/python3
"""Class Student that defines a student"""


class Student():
    """
    Only attribute names contained in this
    list must be retrieved.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            dict_student = {}
            for i in vars(self):
                if i in attrs:
                    dict_student[i] = vars(self)[i]
            return dict_student
        else:
            return vars(self)
