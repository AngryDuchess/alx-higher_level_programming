#!/usr/bin/python3
"""
    this module contains class Rectangle which inherits from the Base class

"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """a getter to retriece the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """a setter to set the value of the width
        Args:
            value: value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """a getter to retriece the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """a setter to set the value of the height
        Args:
            value: value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """a getter to retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """a setter to set the value of x
        Args:
            value: value of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """a getter to retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """a setter to set the value of y
        Args:
            value: value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle using #"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
