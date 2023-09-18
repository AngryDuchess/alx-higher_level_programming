#!/usr/bin/python3
"""this module contains the function from_json_string(my_str)"""

import json


def from_json_string(my_str):
    """this function returns the object(python data structure)
    represented by a JSON string
    Args:
        my_str: str to be deserialized
    """
    obj = json.loads(my_str)
    return obj
