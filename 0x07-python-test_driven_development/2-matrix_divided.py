#!/usr/bin/python3
"""

    This module contains a function that divides each number in a matrix
    by an integer called div

"""


def matrix_divided(matrix, div):
    """This function divides each element in a matrix by an integer passed
        Arguments:
        matrix: matrix whose elements are to be divided
        div: number used to divide each element in the matrix

        Returns:
        new_matrix: a new matrix without changing the old one
        """
    if div is None:
        raise TypeError("div must be a number")
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None:
        raise TypeError(msg)
    if not matrix:
        raise TypeError(msg)
    if not isinstance(matrix, list):
        raise TypeError(msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError(msg)

    first_row_length = len(matrix[0])
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            try:
                element = round(i / div, 2)
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")
            new_row.append(element)
        new_matrix.append(new_row)
    return new_matrix
