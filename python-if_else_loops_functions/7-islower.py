#!/usr/bin/python3
def islower(c):
    if c >= chr(97) and c <= chr(123):
        return True
    elif c <= chr(90):
        return False
    else:
        return False
