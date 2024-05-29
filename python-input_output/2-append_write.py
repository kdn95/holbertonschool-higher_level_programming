#!/usr/bin/python3
"""Function that appends string to txt file"""


def append_write(filename="", text=""):
    """Appending txt file"""

    with open(filename, "a", encoding='UTF8') as app_file:
        return app_file.write(text)
