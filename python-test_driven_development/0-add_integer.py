#!/usr/bin/python3
"""
This function will add 2 integers together
"""


def add_integer(a, b=98):
    """
    This function returns the sum of the args provided.

    Args:
    a (int/float) : first
    b (int/float) : second (default at an int 98)

    Return:
        int: sum of a & b
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
