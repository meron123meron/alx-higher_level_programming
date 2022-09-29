#!/usr/bin/python3
"""Defines a function"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    Args:
    filename - is the file
    """
    with open(filename, encoding="utf-8") as myfile:
        return json.load(myfile)
