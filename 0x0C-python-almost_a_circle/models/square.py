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
            if args is not None:
                i = 0
                for a in args:
                    if i == 0:
                        self.id = a
                    elif i == 1:
                        self.size = a
                    elif i == 2:
                        self.x = a
                    elif i == 3:
                        self.y = a
                    i = i + 1
            elif kwargs:
                for (key, value) in kwargs.items():
                    setattr(self, key, value)

        def to_dictionary(self):
            """dictionary representation of a Square"""
            d = {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
            return d
