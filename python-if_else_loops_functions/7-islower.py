#!/usr/bin/python3
def islower(c):
    a = ord(c)
    if a >= ord('a') and a <= ord('z'):
        return True
    elif a >= ord('A') and a <= ord('Z'):
        return False
    else:
        pass
