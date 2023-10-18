#!/usr/bin/python3
"""this module contains the is_kind_of_class(obj, a_class) function"""


def is_kind_of_class(obj, a_class):
    """this function checks if an object is an instance of a class
    and its subclasses

    Args:
    obj: the object to be checked
    a_class: the class to be look into

    Returns:
    True:if object is found
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
