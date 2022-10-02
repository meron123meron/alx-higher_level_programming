#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)
        
        @property
        def size(self):
            """getter"""
            return self.__size
        @size.setter
        def size(self, value):
            """setter"""
            self.__size = value
            self.width = value
            self.height = value
