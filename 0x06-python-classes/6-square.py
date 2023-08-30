#!/usr/bin/python3
"""initializing script"""


class Square:
    """ This class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializing object

        Args:
            size: a private instance attribute
        """
        self.__size = size
        self.position = position

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """a getter to privately get the size value"""
        return self.__size

    @property
    def position(self):
        """a getter to privately retrieve position value"""
        return self.__position

    @size.setter
    def size(self, size):
        "a setter to change and set size value"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, value):
        """a setter to set position"""
        if ((len(value) != 2) or (type(value) is not tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if ((type(value[1]) is not int)) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the square with #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
