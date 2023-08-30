#!/usr/bin/python3
"""initializing script"""


class Square:
    """ This class defines a square"""
    def __init__(self, size=0):
        """initializing object

        Args:
            size: a private instance attribute
        """
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """a getter to privatyly get the size valu"""
        return self.__size

    @size.setter
    def size(self, size):
        "a setter to change and set size value"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
