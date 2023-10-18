#!/usr/bin/python3
"""
    this module contains the pascal_triangle function
"""


def pascal_triangle(n):
    """this function returns a list of integers representing
    the pascal's triangle
    Args:
        n: number of rows to print
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(len(prev_row) - 1):
            next_value = prev_row[i] + prev_row[i+1]
            new_row.append(next_value)
        new_row.append(1)
        triangle.append(new_row)
    return triangle
