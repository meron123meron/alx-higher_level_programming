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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rec"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns the rectangle description"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
