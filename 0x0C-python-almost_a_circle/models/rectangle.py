#!/usr/bin/python3
"""rectangle"""
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area"""
        return (self.width * self.height)

    def display(self):
        """prints to stdout the rectangle in # character"""
        print("\n"*self.y, end="")
        for i in range(self.height):
            for j in range(self.width):
                if j == 0:
                    print(" "*self.x, end="")
                print("#", end="")
            print("")

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format
        (self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attributes
        """
        if args is not None:
            i = 0
            for a in args:
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x == a
                elif i == 4:
                    self.y = a
                i = i + 1

        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        d = {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
             'width': self.width}
        return d
