#!/usr/bin/env python3

"""
append to file
"""


def append_write(filename="", text=""):
    """append text to file"""
    with open(filename, 'a') as f:
        return f.write(text)