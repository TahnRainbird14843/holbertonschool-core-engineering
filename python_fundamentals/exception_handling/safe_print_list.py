#!/usr/bin/env python3

def safe_print_list(mylist=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(mylist[i]))
            count += 1
        except:
            pass
    
    return (count)