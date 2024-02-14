#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base model."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, 'w') as file:
            file.write(
                cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ Decode From JSON """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instance from a dictionary of attributes.

        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ Loads the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as Ofile:
                j_data = Ofile.read()
                dict_obj = cls.from_json_string(j_data)
                instances = [cls.create(**data) for data in dict_obj]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save CSV Data """
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        with open(filename, mode="w", newline='') as Ofile:
            writer = csv.writer(Ofile)
            for obj in list_objs:
                writer.writerow(obj.to_csv())

    @classmethod
    def load_from_file_csv(cls):
        """ Load CSV Data """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as Ofile:
                aha = csv.reader(Ofile)
                obj = []
                for row in aha:
                    obj.append(cls.from_csv(row))
                return obj
        except FileNotFoundError:
            return []

    def to_csv(self):
        """ Convert To CSV """
        pass

    @classmethod
    def from_csv(cls, row):
        """ Decode From CSV """
        pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw Shapes """
        pen = turtle.Turtle()

        def draw_rectangle(x, y, width, height):
            """ Draw Rectangle """
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            for _ in range(2):
                pen.forward(width)
                pen.left(90)
                pen.forward(height)
                pen.left(90)

        def draw_square(x, y, size):
            """ Draw Square """
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            for _ in range(4):
                pen.forward(size)
                pen.left(90)

        pen.color("blue")
        for rectangle in list_rectangles:
            x, y, width, height = rectangle.x,
            rectangle.y, rectangle.width, rectangle.height
            draw_rectangle(x, y, width, height)

        pen.color("blue")
        for square in list_squares:
            x, y, size = square.x, square.y, square.size
            draw_square(x, y, size)
