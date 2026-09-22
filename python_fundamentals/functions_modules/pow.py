#!/usr/bin/env python3

def pow(a, b):
    out = 1
    while (b > 0):
        out *= a
        b -= 1
    return (out)
