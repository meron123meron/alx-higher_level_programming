#!/usr/bin/python3
"""Defines a function"""
import json


def from_json_string(my_str):
    """a function with
    Args:
    my_str - a string
    returns an (Python data structure)
    """
    return (json.loads(my_str))
