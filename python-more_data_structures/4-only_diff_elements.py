#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list_1_a = list(set_1)
    list_2_a = list(set_2)
    uniq_list = []
    for unique in list_1_a:
        if unique not in list_2_a:
            uniq_list.append(unique)
        else:
            continue
    for unique in list_2_a:
        if unique not in list_1_a:
            uniq_list.append(unique)
        else:
            continue
    return set(uniq_list)
