#!/usr/bin/python3
n = 100
for i in range(0, n):
    if i == 99:
        print("{:0>2d}, ".format(i))
    else:
        print("{:0>2d}, ".format(i), end="")