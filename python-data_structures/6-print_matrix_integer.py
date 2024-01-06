#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if row in matrix == 0:
        print(" ")
    else:
        for row in matrix:
            for num in row:
                print("{:d}".format(num), end=" " if num != row[-1] else "\n")
