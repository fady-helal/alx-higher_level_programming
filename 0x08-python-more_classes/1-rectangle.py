#!/usr/bin/python3
"""Define a Rectangle class"""

class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
    Args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
    """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        elif(self.__height < 0):
            raise ValueError("height must be >= 0")
        self.__height = value