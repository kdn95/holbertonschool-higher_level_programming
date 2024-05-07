#!/usr/bin/python3
n = 99
for i in range(0, n):
    hex_num = "{0:x}".format(i)
    print("{} = 0x{}".format(i, hex_num))
