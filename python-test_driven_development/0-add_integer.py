#!/usr/bin/python3
"""
This function will add 2 integers together
"""


def add_integer(a, b=98):
    """
    Thsi function returns the sum of the args provided.

    Args:
    a (int/float) : first
    b (int/float) : second (default at an int 98)

    Return:
        int: sum of a & b
    """
    if isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")

    if isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer")

    return a + b
