#!/usr/bin/env python3

"""
This read a file
"""

def read_file(filename=""):
    """This reads a file to stdout"""
    with open(filename, 'r') as f:
        print(f.read())