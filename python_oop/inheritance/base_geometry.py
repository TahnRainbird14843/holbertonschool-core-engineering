#!/usr/bin/env python3

"""
this defines a base geometry class
"""


class BaseGeometry:
    """this defines basic behaviour for geometric shapes"""

    def area(self):
        pass

    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
        else:
            pass
