#!/usr/bin/python3
n = 100
for i in range(0, n):
    if i == 89:
        print("{:0>2d}".format(i))
    elif (i // 10) < (i % 10):
        print("{:0>2d}, ".format(i), end="")
    elif (i // 10) == (i % 10):
        continue
