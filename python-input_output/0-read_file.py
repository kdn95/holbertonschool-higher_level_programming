#!/usr/bin/python3
"""Function to read a text file"""
def read_file(filename=""):
    with open('my_file_0.txt', encoding='UTF8') as a_file:
        for line in a_file:
            print("{}".format(line), end='')
