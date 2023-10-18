#!/usr/bin/python3
"""this function adds a new attribute to an object if possible"""


def add_attribute(attr, name, value):
    """this function checks if it is possible to add
    a new attribute to an object
    Args:
        attr: attribute to be added
        name: name string
        value: string value"""

    if hasattr(attr, '__dict__') is False:
        raise TypeError("can't add new attribute")

    setattr(attr, name, value)
