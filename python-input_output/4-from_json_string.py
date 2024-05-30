#!/usr/bin/python3
"""From JSON function"""
import json


def from_json_string(my_str):
    """Return obj from JSON str"""
    return json.loads(my_str)
