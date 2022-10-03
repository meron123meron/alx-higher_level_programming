#!/usr/bin/python3
"""base"""
import json
import turtle


class Base:
    """This class will be the “base” of all
    other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor(initializer)
        Args:
        id - integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as jsonfile:
            if list_objs is not None:
                for i in list_objs:
                    list_dictionary = i.to_dictionary()
                jsonfile.write(Base.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        by changing it to python
        Args:
            json_string - a string
        """
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as jsonfile:
                list_dictionary = Base.from_json_string(jsonfile.read())
                for i in list_dictionary:
                    return [cls.create(**i)]
        except IOError:
            return []

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """draw the figure
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares
        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
