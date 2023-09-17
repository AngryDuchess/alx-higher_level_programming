#!/usr/bin/python3
"""this module contains the inherits_from(obj, a_class) function"""


def inherits_from(obj, a_class):
    """this function checks if an object is an instance of a class's
    subclasses

    Args:
    obj: the object to be checked
    a_class: the class to be look into

    Returns:
    True:if object is found
    """
    return (isinstance(obj, a_class)) and (type(obj) is not a_class)
