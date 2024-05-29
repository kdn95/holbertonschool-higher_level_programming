#!/usr/bin/python3
"""Function to read a text file"""


def read_file(filename=""):
    """Function read_file"""

    with open(filename, encoding='UTF8') as a_file:
        for line in a_file:
            print("{}".format(line), end='')
