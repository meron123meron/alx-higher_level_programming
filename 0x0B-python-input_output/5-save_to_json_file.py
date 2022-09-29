#!/usr/bin/python3
"""Defines a function"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a
    text file, using a JSON representation
    Args:
    my_obj - is the object
    filwname - is the file
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        json.dump(my_obj, myfile)
