#!/usr/bin/env python3

def pow(a, b):
    out = 1
    if (b > 0):
        while (b > 0):
            out *= a
            b -= 1
    elif (b < 0):
        while (b < 0):
            out /= a
            b += 1

    return (round(out, 15))
