#!/usr/bin/python3
"""class_to_json function"""


def class_to_json(obj):
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
