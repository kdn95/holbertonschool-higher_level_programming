#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for in_mat in matrix:
        for num in in_mat:
            print("{:d}".format(num), end=" ")
        print("{}".format(""))
