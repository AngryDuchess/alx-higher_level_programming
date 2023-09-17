#!/usr/bin/python3
"""
    This module contains a class MyList

"""


class MyList(list):
    """this class inherits form list"""
    def print_sorted(self):
        """this function prints a sorted list"""
        print(sorted(self))
