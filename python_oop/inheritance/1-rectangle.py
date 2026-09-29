#!/usr/bin/env python3

"""
This defines the rectangle class,
which inherits from base geometry
"""


BaseGeometry = __import__('base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """This is the rectangle class"""
    def __init__(self, width, height):
        integer_validator("width", width)
        self.__width = width
        integer_validator("height", height)
        self.__height = height
