#!/usr/bin/python3
""" Nameless module for extending the List built-in class """


class VerboseList(list):
    """VerboseList

    Args:
        list

    Returns:
        Nothing

    """

    # def __init__(self, items):
    #     super().__init__(items)

    def append(self, item):
        super().append(item)
        print("Added {0} to the list.".format(item))

    def extend(self, items):
        super().extend(items)
        count = sum(1 for _ in items)
        print("Extended the list with {0} items.".format(count))

    def remove(self, item):
        try:
            super().remove(item)
            print("Removed {0} from the list.".format(item))
        except ValueError as exc:
            print("Attempted to remove value {0} from the list.".format(item))
            print("Specified value does not exist. Nothing changed. Raising ValueError")
            raise ValueError() from exc

    def pop(self, index = None):
        if index is None:
            index = len(self) - 1

        try:
            print("Popped {0} from the list.".format(self[index]))
            item = super().pop(index)
        except IndexError as exc:
            print("Attempted to pop index {0} from the list.".format(index))
            print("Specified index is out of range. Nothing changed. Raising IndexError")
            raise IndexError() from exc

        return item
