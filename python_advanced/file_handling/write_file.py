#!/usr/bin/env python3

"""
write to a file
"""


def write_file(filename="", text=""):
    """write to file"""
    with open(filename, 'w') as f:
        return f.write(text)
