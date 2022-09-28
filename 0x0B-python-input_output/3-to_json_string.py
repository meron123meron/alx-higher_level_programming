#!/usr/bin/python3
"""Defines a function """
import json


def to_json_string(my_obj):
    """a function with
    Args:
    my_obj - an object(string)
    returns the JSON representation of an object
    """
    return (json.dumps(my_obj))
