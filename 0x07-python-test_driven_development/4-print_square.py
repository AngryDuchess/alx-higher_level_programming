#!/usr/bin/python3
"""

    This module prints a square with the character #

"""


def print_square(size):
    """this function take the size of a square and prints it using #

        Args:
        size: size of the square

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is negative
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
