#!/usr/bin/python3
"""
This Module Contains :
    - Square Class That Inherits <--- Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Convert Attributes To Dictionary """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return Dictionary """
        dic = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return dic

    def __str__(self):
        """ return representation of square class."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
