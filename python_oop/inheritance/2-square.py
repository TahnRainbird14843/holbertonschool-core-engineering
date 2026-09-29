#!/usr/bin/env python3

"""
This implements a square class which
is a subclass of rectangle
"""


Rectangle = __import__('2-rectangle').Rectangle

class Square(Rectangle):
    """this is the square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
