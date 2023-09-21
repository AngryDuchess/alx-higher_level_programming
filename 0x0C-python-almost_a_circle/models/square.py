#!/usr/bin/python3
"""this module contains the class Square and all its fields"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """the class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing objects and attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """retrieves the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of the size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns arguments to each attribute"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation"""
        return {
            "id": self.id, "size": self.width,
            "x": self.x, "y": self.y
        }
