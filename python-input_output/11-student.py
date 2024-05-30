#!/usr/bin/python3
"""Student Class"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dict rep if attr is list of strings"""
        if isinstance(attrs, list) and all([isinstance(x, str) for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attrs"""
        for k, v in json.items():
            self.__dict__[k] = v
