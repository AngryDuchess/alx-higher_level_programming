#!/usr/bin/python3
"""this module contains the function is_same_class(obj, a_class)"""


def is_same_class(obj, a_class):
    """this function checks if an object is an instance of a class or not

    Args:
    obj: object to be looked for
    a_class: class to search for object from

    Returns:
    True: if obj is found in the sepcified class
    False: if obj is not found in the specified class
    """
    return (type(obj) == a_class)
