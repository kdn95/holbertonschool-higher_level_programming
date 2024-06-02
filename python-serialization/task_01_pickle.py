#!/usr/bin/python3
"""
Module for serialization and deserialization
using Pickle
"""
import pickle
import sys


class CustomObject:
    """CustomObject Class"""

    name = ""
    age = 0
    is_student = False

    def __init__(self, name="", age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """To print obj attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """To serialize current instance of obj"""
        if not filename:
            print("Invalid filename specified!")
            sys.exit()
        try:
            with open(filename, "wb") as w_file:
                pickle.dump(self, w_file)
        except FileNotFoundError:
            print("File not found")

    @classmethod
    def deserialize(cls, filename):
        """To load and return instance of CustomObject"""
        if not filename:
            print("Invalid filename specified!")
            sys.exit()
        try:
            with open(filename, "rb") as r_file:
                return pickle.load(r_file)
        except FileNotFoundError:
            print("File not found")
