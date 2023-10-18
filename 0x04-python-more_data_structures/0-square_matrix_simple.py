#!/usr/bin/python3
"""initializing script"""


def square_matrix_simple(matrix=[]):
    """this function squares each element in a matrix
    Args:
    matrix = matrix to be squared
    """

    new_matrix = [[i**2 for i in row] for row in matrix]
    """create new matrix using nested list comprehension"""
    return new_matrix
