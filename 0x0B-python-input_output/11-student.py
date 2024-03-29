#!/usr/bin/python3
"""this module contains the class Student"""


class Student:
    """class for a student"""

    def __init__(self, first_name, last_name, age):
        """initializes object and other arguments
        Args:
        first_name: first name
        last_name: last name
        age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        Args:
            attrs(list): attributes

        Returns:
        only attribute names if attrs is a list of strings
        otherwise all attributes
        """
        if ((type(attrs)) == list and
                all(type(item) is str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Args:
        json(dictionary): json file
        """
        for key, value in json.items():
            setattr(self, key, value)
