#!/usr/bin/python3
list = []
str = ""
for i in range(97, 123):
    list.append(chr(i))
alphabet = str.join(list)
print("{}".format(alphabet))
