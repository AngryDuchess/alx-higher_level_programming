#!/usr/bin/python3
"""
    This module contains the class of a rectangle
"""


class Rectangle:
    """this class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
           this method initializes objects

           Args:
           width: width of the rectangle
           height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """a getter to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """a setter to set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a getter to retrieve the height"""
        return self.__height

    @height.setter
    """a setter to set the height"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
