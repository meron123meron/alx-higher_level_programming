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
            return self.width

        @size.setter
        def size(self, value):
            """setter"""
            self.width = value
            self.height = value

        def update(self, *args, **kwargs):
            """args - assigns attributes
            kwargs - pass the variable length of keyword arguments
            """
            order = (self.id, self.width, self.height, self.x, self.y)
            if args is not None:
                for a in args:
                    self.id = a
            elif kwargs:
                for (name, value) in kwargs.items():
                    setattr(self, name, value)
