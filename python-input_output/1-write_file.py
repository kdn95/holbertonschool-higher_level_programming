#!/usr/bin/python3
"""Function that writes a str to text file"""

def write_file(filename="", text=""):
    """Function write_file"""

    with open(filename, "w", encoding='UTF8') as b_file:
        return b_file.write(text)
