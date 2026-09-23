#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    val_list = [0, 0]
    for i in range(min(len(tuple_a), 2)):
        val_list[i] += tuple_a[i]
    for i in range(min(len(tuple_b), 2)):
        val_list[i] += tuple_b[i]
    return ((val_list[0], val_list[1]))
