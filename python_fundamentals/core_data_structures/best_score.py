#!/usr/bin/env python3

def best_score(a_dictionary):
    best = None
    if (not bool(a_dictionary) or a_dictionary == None):
        return (None)

    for i, (key, val) in enumerate(a_dictionary.items()):
        if (best == None):
            best = val
            winner = key
        if (int(val) > best):
            winner = key
            best = val
    return (winner)
