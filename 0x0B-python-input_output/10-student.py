#!/usr/bin/python3
"""Defines a class"""


class Student:
    """
    Defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Args:
        first_name
        last_name
        age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation
        of a Student instance
        Args:
            attrs - is a list of strings
        """
        if attrs is not None:
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
