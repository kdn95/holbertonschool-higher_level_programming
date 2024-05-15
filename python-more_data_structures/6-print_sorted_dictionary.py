#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary.items())
    sorted_dict = {}
    for a, b in sorted_list:
        sorted_dict[a] = b
        print("{}: {}".format(a, b))
