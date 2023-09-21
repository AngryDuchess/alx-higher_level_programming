#!/usr/bin/python3
"""this module contains the class Square and all its fields"""
from models.rectangle import Rectangle


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
