#!/usr/bin/python3
"""this module contains the Base class"""


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing object and arguments"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
