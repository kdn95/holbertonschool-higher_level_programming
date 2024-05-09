#!/usr/bin/python3
if __name__ == "__main__":
    import sys
n = len(sys.argv) - 1
sum = 0
if (n == 0):
    print("{}".format(n))
elif (n == 1):
    print("{}".format(sys.argv[n]))
else:
    for number in range(1, len(sys.argv)):
        sum += int(sys.argv[number])
    print("{}".format(sum))
