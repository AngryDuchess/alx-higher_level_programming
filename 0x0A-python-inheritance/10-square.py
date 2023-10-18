#!/usr/bin/python3
"""
    This module contains a class square that inherits from Rectangle

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square"""

    def __init__(self, size):
        """initializing objects and arguments
        Args:
            size: size of the square
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
