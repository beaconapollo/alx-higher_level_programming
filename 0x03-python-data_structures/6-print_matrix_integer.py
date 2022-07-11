#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for row in matrix:
            for val in row:
                if val != row[-1]:
                    print("{:d}".format(val), end = " ")
                else:
                    print("{:d}".format(val), end = "\n")
