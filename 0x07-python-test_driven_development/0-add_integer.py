#!/usr/bin/python3
"""This module adds two integers"""


def add_integer(a, b=98):
    """this function adds two integers
        Args:
        a: first integer
        b: second integer

        Returns:
        int: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)

    return a + b
