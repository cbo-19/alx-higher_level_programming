#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        maptr = 't'.join(map(str, i))
        print("{}".format(maptr))
