#!/usr/bin/python3
"""this module contains the Base class"""
import json
import os
import csv


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
        if list_objs is None or list_objs == []:
            json_string = "[]"
        else:
            for i in range(len(list_objs)):
                list_dictionaries.append(
                    list_objs[i].to_dictionary()
                )
            json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """takes a json string and returns a list of
        json string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes
        already set
        Args:
            dictionary: a double pointer to a dictionary
        """
        if cls.__name__ == 'Rectangle':
            dummy_attr = cls(2, 3)
        elif cls.__name__ == 'Square':
            dummy_attr = cls(2)
        dummy_attr.update(**dictionary)
        return dummy_attr

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        list_of_instances = []
        if os.path.exists(filename) is False:
            return []
        with open(filename, "r") as f:
            s = f.read()
            list_of_dictionaries = cls.from_json_string(s)
        for i in list_of_dictionaries:
            list_of_instances.append(cls.create(**i))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save a csv file"""
        filename = "{}.csv".format(cls.__name__)
        list_dictionaries = []

        if list_objs:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        with open(filename, "w", newline="") as csvfile:
            fields = []
            if cls.__name__ == 'Rectangle':
                fields = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                fields = ['id', 'size', 'x', 'y']

            writer = csv.DictWriter(
                csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(list_dictionaries)

    @classmethod
    def load_from_file_csv(cls):
        """deserializing csv"""
        filename = "{}.csv".format(cls.__name__)
        list_of_instances = []

        if not os.path.exists(filename):
            return []

        with open(filename, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for csv_obj in reader:
                n_dict = {}
                for key, value in csv_obj.items():
                    n_dict[key] = int(value)
                list_of_instances.append(cls.create(**n_dict))
        return list_of_instances
