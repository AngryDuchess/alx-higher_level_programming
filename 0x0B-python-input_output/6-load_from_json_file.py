#!/usr/bin/python3
"""this module contains the function load_from_json_file(filename)"""
import json


def load_from_json_file(filename):
    """this function creates an object from a JSON file
    Args:
        filename: name of JSON file
        """
    with open(filename) as f:
        return json.load(f)
