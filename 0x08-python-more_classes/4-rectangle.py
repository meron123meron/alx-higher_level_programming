#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:

    """is a class"""
    def __init__(self, width=0, height=0):
        """Initializes the class"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of the rect"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        new = []
        for i in range(self.__height):
            for j in range(self.__width):
                new.append("#")
            if i != self.__height - 1:
                new.append("\n")
        return ("".join(new))
    def __repr__(self):
        """returns a string representation of the rectangle
        to recreate a new instance"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
