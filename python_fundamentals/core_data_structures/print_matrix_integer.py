#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    width = len(matrix[0])

    for i in range(length):
        for j in range(width):
            if (j == width - 1):
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=' ')
