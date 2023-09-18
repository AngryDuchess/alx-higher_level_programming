#!/usr/bin/python3
"""this module contains the function read_file(filename="")"""


def read_file(filename=""):
    """this function reads a file
    Args:
    filename: name of the file
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")
