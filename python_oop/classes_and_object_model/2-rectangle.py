#!/usr/bin/env python3

"""
module
"""

class Rectangle:
    """rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return (self.__width)
    
    @width.setter
    def width(self, width):
        self.validate("width", width)
        self.__width = width
    
    @property
    def height(self):
        return (self.__height)
    
    @height.setter
    def height(self, height):
        self.validate("height", height)
        self.__height = height
    
    def validate(self, name, input):
        if (type(input) is not int):
            raise TypeError("{} must be an integer".format(name))
        elif (input < 0):
            raise ValueError("{} must be >= 0".format(name))
    
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        if (self.width != 0 or self.height != 0):
            return (2 * self.width + 2 * self.height)
        else:
            return (0)
