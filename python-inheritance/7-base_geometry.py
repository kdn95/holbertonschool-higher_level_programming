#!/usr/bin/python3
""" Module for Class BaseGeometry"""


class BaseGeometry:
    """
    BaseGeometry Class
    """
    def area(self):
        """ Method calculating the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Method that validates the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
