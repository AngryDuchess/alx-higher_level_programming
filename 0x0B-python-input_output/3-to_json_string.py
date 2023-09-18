#!/usr/bin/python3
"""this module contains the function to_json_string(my_obj)"""

import json


def to_json_string(my_obj):
    """this function returns the JSON representation
    of an object(string)
    Args:
        my_obj: obj to be serialized
    """
    json_str = json.dumps(my_obj)
    return json_str
