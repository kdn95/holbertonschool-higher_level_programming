#!/usr/bin/python3
if __name__ == "__main__":
    import sys
n = len(sys.argv) - 1
if (n == 0):
    print("{} arguments.".format(n))
elif (n == 1):
    print("{} argument:".format(n))
    print("{}: {}".format(n, str(sys.argv[n])))
else:
    print("{} arguments:".format(n))
    for index, word in enumerate(sys.argv[1:]):
        print("{}: {}".format((index + 1), word))
