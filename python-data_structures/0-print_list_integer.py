#!/usr/bin/python3
def print_list_integer(my_list=[]):
     for digit in my_list:
        if isinstance(digit, int):
            print("{:d}".format(digit))
        else:
            break
