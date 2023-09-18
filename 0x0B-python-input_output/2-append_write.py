#!/usr/bin/python3
"""this module contains the function append_write(filename="", text="")"""


def append_write(filename="", text=""):
    """this function appends a string to a file and
    returns the number of characters added

    Args:
        filename: file name
        text: characters to be appended into file
    """
    with open(filename, "a", encoding="utf-8") as f:
        append_file = f.write(text)
        return append_file
