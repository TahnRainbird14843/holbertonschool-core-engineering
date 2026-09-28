#!/usr/bin/env python3

"""
module
"""


class Square:
    """square"""
    def __init__(self, size):
        self.set_size(size)
    
    def set_size(self, size):
        self.validate(size)
        self.__size = size
    
    def get_size(self):
        return (self.__size)

    def validate(self, size):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            pass
    
    def area(self):
        return (self.get_size() ** 2)
    
    def my_print(self):
        side = self.get_size()
        row = ""
        for i in range(side):
            row += "#"
        for i in range(side):
            print(row)
        if (side == 0):
            print(row)
