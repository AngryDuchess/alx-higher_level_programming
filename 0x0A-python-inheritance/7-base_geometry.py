#!/usr/bin/python3
"""

    This module contains a class BaseGeometry

"""


class BaseGeometry:
    """a class BaseGeometry"""

    def area(self):
        """function to implement area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate value
        Args:
            name: name of parameter which is a string
            value: value to be validated

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
