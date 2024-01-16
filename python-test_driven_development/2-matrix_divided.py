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

    for row in matrix:
        if not isinstance(matrix, list) or not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    rows = len(matrix)
    cols = len(matrix[0])
    for row in matrix:
        if not len(row) == cols:
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

        new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
        
        return new_matrix
