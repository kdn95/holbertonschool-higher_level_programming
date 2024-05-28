#!/usr/bin/python3
""" Module Class Square inheriting Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Subclass Square with parent class Rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Method to return area of Square"""
        return self.__size * self.__size

    def __str__(self):
        """ string rep method replaced"""
        return "[Square] " + \
            str(self.__size) + "/" + str(self.__size)
