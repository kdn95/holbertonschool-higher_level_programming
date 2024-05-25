#!/usr/bin/python3
"""
This function will divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    The function returns a new matrix based on the args provided.

    Args:
    matrix : a matrix
    div (int/float) : number used to divide all elements in matrix

    Return:
        new matrix (array): newly divided matrix
    """
    error_mes = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_mes)
    for row in matrix:
        if not row or not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(error_mes)
    if any(len(i) != len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_mat = [[round(num / div, 2) for num in row] for row in matrix]

    return new_mat


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
