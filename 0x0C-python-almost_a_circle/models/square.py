#!/usr/bin/python3
"""this module contains the class Square and all its fields"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
