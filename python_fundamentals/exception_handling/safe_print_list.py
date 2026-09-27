#!/usr/bin/env python3

def safe_print_list(mylist=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(mylist[i]),end='')
            count += 1
        except:
            count += 0
    print("")
    
    return (count)
    