#!/usr/bin/python3
str = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(str)):
    str[i]
first = str[0:4]
mid = str[5:-10]
end = str[-9:]
new_str = first + mid + end
print("{}".format(new_str), end="")
