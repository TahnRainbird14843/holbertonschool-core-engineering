#!/usr/bin/env python3

def best_score(a_dictionary):
    best = None
    if (not bool(a_dictionary) or a_dictionary is None):
        return (None)

    for i, (key, val) in enumerate(a_dictionary.items()):
        if (best is None):
            best = val
            winner = key
        elif (int(val) > best):
            winner = key
            best = val
    return (winner)
