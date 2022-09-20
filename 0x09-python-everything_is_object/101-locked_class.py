#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """dynamically creates new instance attributes
    only if the new instance attribute is first_name"""
    __slots__ = ["first_name"]
