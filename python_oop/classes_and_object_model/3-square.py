#!/usr/bin/env python3

class Square:
    def __init__(self, size):
        self.validate(size)
        self.__size = size

    def validate(self, size):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            pass
    
    def area(size):
        return (self.__size ** 2)
