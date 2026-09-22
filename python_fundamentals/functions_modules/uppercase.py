#!/usr/bin/env python3

def uppercase(string):
    for i in range(len(string)):
        if (97 <= ord(string[i]) <= 122):
            print("{}".format(chr(ord(string[i]) - 32)), end='')
        else:
            print("{}".format(string[i]), end='')
