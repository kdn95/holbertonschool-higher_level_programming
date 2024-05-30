#!/usr/bin/python3
"""JSON write function to txt file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes obj to txt file using JSON"""
    with open(filename, "w", encoding='utf-8') as w_file:
        json.dump(my_obj, w_file)
