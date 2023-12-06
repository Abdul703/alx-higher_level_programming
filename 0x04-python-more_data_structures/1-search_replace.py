#!/usr/bin/python3

def search_replace(my_list, search, replace):
    func = lambda x: replace if x == search else x
    return list(map(func, my_list))
