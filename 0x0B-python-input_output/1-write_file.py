#!/usr/bin/python3
"""this module contains the function write_file(filename="", text="")"""


def write_file(filename="", text=""):
    """this function writes to a file and
    returns the number of characters written

    Args:
        filename: file name
        text: characters to be written into file
    """
    with open(filename, "w", encoding="utf-8") as f:
        write_file = f.write(text)
        return write_file
