#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    common_list= []
    for duplicate in list_1:
        if duplicate in list_2:
            common_list.append(duplicate)
    return set(common_list)
