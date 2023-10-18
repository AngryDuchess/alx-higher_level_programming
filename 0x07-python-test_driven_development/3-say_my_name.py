#!/usr/bin/python3
"""
    This module contains a function that prints a full name.

"""


def say_my_name(first_name, last_name=""):
    """this function prints the first and last names.
       Args:
       first_name: your first name.
       last_name: your last_name.

       Returns:
       full_name: first_name + last_name

       Raises:
       TypeError: if first name or last name are not strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
