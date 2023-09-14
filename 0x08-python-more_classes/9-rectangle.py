#!/usr/bin/python3
"""

    This module contains the class of a rectangle

"""


class Rectangle:
    """this class defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """this method initializes objects

           Args:
               width: width of the rectangle
               height: height of the rectangle


        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            rect += (str(self.print_symbol) * self.width) + "\n"
        return rect[:-1]

    def __repr__(self):
        """this method prints the string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """this method deletes a rectangle object"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """this method returns the rectangle with the biggest area
        Args:
        rect_1: first rectangle
        rect_2: second rectangle

        Raises:
        TypeError: if rect_1 or rect_2 is not an instance of the
                   class Rectangle

        Returns:
        rect_1: if area of rect_1 = area of rect_2
        or rectangle with biggest area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """this method returns a new Rectangle instance with
        width == height == size

        Args:
        cls: rectangle class
        size: rectangle width and height

        Returns:
        a new instance of Rectangle class
        """
        return cls(size, size)
