#!/usr/bin/env python3

def common_elements(set_1, set_2):
    common_set = set()
    for elt in set_1:
        if elt in set_2:
            common_set.add(elt)
    return (common_set)
