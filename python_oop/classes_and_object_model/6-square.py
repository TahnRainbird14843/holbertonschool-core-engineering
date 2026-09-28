#!/usr/bin/env python3

"""
module
"""


class Square:
    """square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        self.validate(size)
        self.__size = size

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, position):
        self.val_position(position)
        self.__position = position

    def val_position(self, position):
        if (type(position) is not tuple or len(position) != 2 or type(position[1]) is not int
        or type(position[0]) is not int or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def validate(self, size):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            pass

    def area(self):
        return (self.size ** 2)

    def get_print(self):
        side = self.size
        position = self.position
        row = ""
        if (side == 0):
            print(row)
            return (row)
        for i in range(position[1]):
            row += "\n"
        for i in range(side):
            for j in range(max(0, position[0] - 1)):
                row += "_"
            for j in range(side):
                row += "#"
            if (i != side - 1):
                row += "\n"
        return (row)

    def my_print(self):
        print(self.get_print())

    def __str__(self):
        return (self.get_print())
