#!/usr/bin/python3
"""
A class called MyList that inherits from list
"""


class MyList(list):
    """
    Subclass of built-in list
    """
    def print_sorted(self):
        """
        Prints list of elements in ascending order
        """
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList([3, 1, 4, 5, 2])
    my_list.print_sorted()
