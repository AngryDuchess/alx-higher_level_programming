#!/usr/bin/python3
"""this module contains the function save_to_json_file(my_obj, filename)"""
import json


def save_to_json_file(my_obj, filename):
    """this function writes an object to a text file using
    JSON representation
    Args:
        my_obj: object to be serialized
        filename: name of file where string will be stored
        """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
