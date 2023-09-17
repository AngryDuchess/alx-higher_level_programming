#!/usr/bin/python3
"""this function adds a new attribute to an object if possible"""


def add_attribute(attr, name, value):
    if hasattr(attr, '__dict__') is False:
        raise TypeError("can't add new attribute")

    setattr(attr, name, value)
