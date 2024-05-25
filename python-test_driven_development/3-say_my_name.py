#!/usr/bin/python3
"""
This function prints first name and last name
to the sentence "My name is ..."
"""


def say_my_name(first_name, last_name=""):
    """
    This function returns a new string from the strings provided.

    Args:
    first_name : first string
    last_name : second string

    Return:
        new string : "My name is [first_name] [last_name]
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    new_string = print("My name is {} {}".format(first_name, last_name))
    return new_string


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
