#!/usr/bin/python3
"""this module contains the function class_to_json(obj)"""


def class_to_json(obj):
    """this function serializes an object which is an instance of a class
    and returns the dictionary description
    Args:
    obj: object to be serialized
    """
    return obj.__dict__
