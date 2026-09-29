#!/usr/bin/env python3

"""
This demonstrates extending builtin classes
in python
"""


class VerboseList(list):
    """verbose list class"""
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        print("Popped [{}] from the list.".format(self[index]))
        super().pop(index)
