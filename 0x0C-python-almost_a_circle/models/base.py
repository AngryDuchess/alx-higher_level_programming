#!/usr/bin/python3
"""this module contains the Base class"""
import json


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing object and arguments"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a json string to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dictionaries.append(
                    list_objs[i].to_dictionary()
                )
            json_string = cls.to_json_string(list_dictionaries)
            with open(filename, "w") as f:
                f.write(json_string)
