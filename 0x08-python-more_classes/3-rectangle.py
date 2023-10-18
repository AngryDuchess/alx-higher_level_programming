#!/usr/bin/python3
"""

    This module contains the class of a rectangle

"""


class Rectangle:
    """this class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """this method initializes objects

           Args:
               width: width of the rectangle
               height: height of the rectangle


        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """a getter to retrieve the width

        Return:
            width of the rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """a setter to set the width of the rectangle

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if with is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a getter to retrieve the height

        Returns:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """a setter that sets the height

        Args:
            value: height of the rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zer

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        this method that returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """this method returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """this method prints the rectangle with the # character"""
        if self.width == 0 or self.height == 0:
            return ("")

        rect = ""
        for i in range(self.height):
            rect += ("#" * self.width) + "\n"
        return rect[:-1]
