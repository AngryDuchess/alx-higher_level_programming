#!/usr/bin/python3
"""this script adds all argument to a python list and saves it into a json"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    """check if file exists"""
    filename = "add_item.json"

    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    arguments = sys.argv[1:]
    my_list.extend(arguments)

    """save file"""
    save_to_json_file(my_list, filename)
