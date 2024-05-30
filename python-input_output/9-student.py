#!/usr/bin/python3
"""Module for student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dict rep of student instance"""
        return self.__dict__.copy()
