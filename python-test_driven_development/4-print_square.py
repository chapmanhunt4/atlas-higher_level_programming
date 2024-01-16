#!/usr/bin/python3
"""
A module that prints a square.
"""


def print_square(size):
    """
    A function that prints a square using '#'.

    Args:
        size: size of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print("")
