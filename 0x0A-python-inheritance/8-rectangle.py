#!/usr/bin/python3
"""
Defines a class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """private instance method
        Args:
        width(positive integer): width of the rec
        height(positive integer): height of the rec
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
