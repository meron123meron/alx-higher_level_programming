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
