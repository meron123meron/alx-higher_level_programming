#!/usr/bin/python3
"""base"""
import json


class Base:
    """This class will be the “base” of all
    other classes in this project"""
    __nb_objects = 0
    def __init__(self, id=None):
        """class constructor(initializer)
        Args:
        id - integer
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as jsonfile:
            if list_objs is not None:
                for i in list_objs:
                    list_dictionary = i.to_dictionary()
                jsonfile.write(Base.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        by changing it to python
        Args:
            json_string - a string
        """
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []
