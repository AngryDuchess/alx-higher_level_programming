#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_length = len(matrix)
    for row in range(row_length):
        for i in matrix[row]:
            print("{:d}".format(i), end=' ')
        print()
