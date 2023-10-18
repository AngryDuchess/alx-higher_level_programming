#!/usr/bin/python3
"""

    This module contains a class Rectangle that inherits from BaseGeometry

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class instantiates the width and height"""
    def __init__(self, width, height):
        """initialize objects and argument
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return string"""
        return ("[{}] {}/{}".format(
            self.__class__.__name__, self.__width, self.__height))
