#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for row in matrix:
            if len(row) == 0:
                print(" ")
            else:
                for num in row:
                    print("{:d}".format(num), end=" " if num != row[-1] else "\n")
