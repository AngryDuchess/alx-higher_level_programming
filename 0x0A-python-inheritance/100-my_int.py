#!/usr/bin/python3
"""
    This module contains a class MyInt

"""


class MyInt(int):
    """class that inherits from int"""
    def __eq__(self, num):
        """function for equivalence"""
        return (int(self) != int(num))

    def __ne__(self, num):
        """function for not equal"""
        return (int(self) == int(num))
