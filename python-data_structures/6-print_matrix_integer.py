#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for in_mat in matrix:
        for num in in_mat:
            print("{}".format(num), end="\t")
        print("")
