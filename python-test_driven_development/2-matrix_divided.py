#!/usr/bin/python3
"""
A module that divides a matrix.
"""


def matrix_divided(matrix, div):
    """
    A function that divides each element of a matrix
    by a specified divisor.

    Args:
        matrix: the matrix to be divided.
        div: the divisor to divide each element by.
    """

    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(matrix_error)
    elif not all(isinstance(i, (int, float))
                    for row in matrix for i in row):
        raise TypeError(matrix_error)

    rows = len(matrix)
    cols = len(matrix[0])
    if not all(len(row) == cols for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
