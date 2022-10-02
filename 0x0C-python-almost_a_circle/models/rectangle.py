#!/usr/bin/python3
"""a class"""
from models.base import Base


class Rectangle(Base):
    """inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization
        Args:
        width - width of the rectangle
        height - height of the rectangle
        x - x
        y - y
        id - int
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    @property
    def width(self):
        """getter"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter"""
        self.__width = value
    @property
    def height(self):
        """getter"""
        return self.height
    @height.setter
    def height(self, value):
        """setter"""
        self.__height = value
    @property
    def x(self):
        """getter"""
        return self.__x
    @x.setter
    def x(self, value):
        """setter"""
        self.__x = value
    @property
    def y(self):
        """getter"""
        return self.__y
    @y.setter
    def y(self, value):
        """setter"""
        self.__y = value
