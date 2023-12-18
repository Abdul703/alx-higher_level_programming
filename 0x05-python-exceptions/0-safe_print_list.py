#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # if x == 0:
    #     return 0
    
    try:
        for i in range(x):
            print(my_list[i], end='')
    except IndexError:
        i -= 1

    print()
    return i + 1
