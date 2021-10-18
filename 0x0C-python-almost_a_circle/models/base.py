#!/usr/bin/python3
"""
Declaration of a super Class Base of all other classes in this project.
The goal of it is to manage id attribute in all your future classes and
to avoid duplicating the same code (by extension, same bugs)
"""
import json
from os.path import exists


class Base:
    """
    Class Base has a private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor assign the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs to a file:"""
        json_file = cls.__name__ + ".json"
        empty_list = []

        if list_objs is not None:
            for run in list_objs:
                empty_list.append(run.to_dictionary())

        with open(json_file, "w") as f:
            f.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """That returns the list of the JSON string
        representation json_string"""
        empty_list = []
        if json_string is None:
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes
        already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        json_file = cls.__name__ + ".json"
        if not exists(json_file):
            return []

        json_str = ""
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                json_str = f.read()
        except FileNotFoundError:
            return list()

        obj_list = []
        dict_json = cls.from_json_string(json_str)
        for current_dict in dict_json:
            new_obj = cls.create(**current_dict)
            obj_list.append(new_obj)

        return obj_list
