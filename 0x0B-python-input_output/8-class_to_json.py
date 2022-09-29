#!/usr/bin/python3
"""Defines a function"""


def class_to_json(obj):
    """
    class to json
    Args:
    obj - is an instance of a class
    returns the dictionary description
    """
    return obj.__dict__
