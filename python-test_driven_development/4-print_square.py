#!/usr/bin/python3
"""
This function prints a square with the character #
based on the number input
"""


def print_square(size):
    """
    This function returns a square made of character '#' based on
    the squared number of the size.

    Args:
    size (int) : size (squared)

    Return:
        prints # times the number of the size for the row and columns
    """
    float_size = isinstance(size, float)

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if float_size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("{}".format("#" * size))


if __name__ == "__main__":
    import doctest
    doctest.testmod("tests/4-print_square.txt")
