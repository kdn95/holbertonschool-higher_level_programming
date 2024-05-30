#!/usr/bin/python3
"""Object creation from JSON"""
import json


def load_from_json_file(filename):
    """Creates obj from JSON"""
    with open(filename, "r", encoding='utf-8') as r_file:
        return json.load(r_file)
