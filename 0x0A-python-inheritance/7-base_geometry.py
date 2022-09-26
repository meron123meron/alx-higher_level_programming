#!/usr/bin/python3
"""
Defines a class
"""


class BaseGeometry:
    """A class"""
    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """public instance method
        Validates value to be an int grater than 0.
        Args:
        name (str): name of the value
        value (unknown): to be validated.
        Raises:
        TypeError: if value is not an int.
        ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
