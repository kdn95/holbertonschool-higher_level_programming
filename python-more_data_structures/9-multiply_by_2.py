#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul = {}
    for k, v in a_dictionary.items():
        mul[k] = v * 2
        a_dictionary = mul
    return a_dictionary
