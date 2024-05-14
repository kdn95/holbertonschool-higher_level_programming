#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) < 2 or len(tuple_b) < 2):
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
        res_a = []
        for i in range(0, len(tuple_a)):
            res_a.append(tuple_a[i] + tuple_b[i])
        res_a = tuple(res_a)
        return str(res_a)
    elif (len(tuple_a) > 2 or len(tuple_b) > 2):
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]
        res_b = []
        for t in range(0, len(tuple_a)):
            res_b.append(tuple_a[t] + tuple_b[t])
        res_b = tuple(res_b)
        return str(res_b)
    elif (len(tuple_a) and len(tuple_b) == 2):
        res_c = []
        for d in range(0, len(tuple_a)):
            res_c.append(tuple_a[d] + tuple_b[d])
        res_c = tuple(res_c)
        return str(res_c)
