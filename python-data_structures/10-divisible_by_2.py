#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for t in my_list:
        if (t % 2 == 0):
            t = True
            new_list.append(t)
        else:
            t = False
            new_list.append(t)
    return new_list
