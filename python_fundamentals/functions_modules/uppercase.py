#!/usr/bin/env python3

def uppercase(string):
    new_string = ""
    for i in range(len(string)):
        if (97 <= ord(string[i]) <= 122):
            new_string += chr(ord(string[i]) - 32)
        else:
            new_string += string[i]
    print("{}".format(new_string))
