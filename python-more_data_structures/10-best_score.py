#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        sorted_d = sorted(a_dictionary.items(), key=lambda x:x[1], reverse=False)
        to_dict = dict(sorted_d)
    return list(to_dict)[-1]
