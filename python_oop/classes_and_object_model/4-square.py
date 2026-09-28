#!/usr/bin/env python3

"""
module
"""


class Square:
    """square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self, size):
        return (self.__size)

    @size.setter
    def size(self, size):
        self.validate(size)
        self.__size = size

    def validate(self, size):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            pass

    def area(self):
        return (self.size ** 2)
