#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max([(y, x) for x, y in a_dictionary.items()])[1]
