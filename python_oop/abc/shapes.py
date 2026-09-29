#!/usr/bin/env python3

from abc import ABC, abstractmethod
from math import pi

"""
this creates shapes from an abstract base class
"""


class Shape(ABC):
    """abstract base class shape"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class, inherits from shape"""

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return (pi * self.__radius ** 2)

    def perimeter(self):
        return (2 * pi * self.__radius)


class Rectangle(Shape):
    """Rectangle class, inherits form shape"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (2 * self.__width + 2 * self.__height)


def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
