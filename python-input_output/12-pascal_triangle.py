#!/usr/bin/python3
"""Triangle function"""


def pascal_triangle(n):
    """ Return list of pascal triangle of n size"""

    if (n <= 0):
        return []

    triangle = [[1]]

    for row in range(n - 1):
        prev_row = [0] + triangle[-1] + [0]
        tmp = []
        for i in range(len(triangle[-1]) + 1):
            tmp.append(prev_row[i] + prev_row[i + 1])
        triangle.append(tmp)

    return triangle
