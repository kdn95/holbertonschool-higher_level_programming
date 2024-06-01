#!/usr/bin/python3
"""Basic serialization Module"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding='utf-8') as w_file:
        json.dump(data, w_file)


def load_and_deserialize(filename):
    with open(filename, "r", encoding='utf-8') as r_file:
        return json.load(r_file)
