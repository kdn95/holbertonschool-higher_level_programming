#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """func to print squared values in matrix"""
    return [[x ** 2 for x in row] for row in matrix]
