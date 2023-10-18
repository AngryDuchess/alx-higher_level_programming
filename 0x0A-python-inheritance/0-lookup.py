#!/usr/bin/python3
"""this module contains the lookup(obj) function"""


def lookup(obj):
    """
    this function returns a list of available attributes and methods
    of an object.

    Args:
    obj: object to be looked up

    Returns:
    list of available attributes and methods
    """
    return dir(obj)
