#!/usr/bin/env python3

class Rectangle:
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

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)