#!/usr/bin/python3

def uppercase(str):
    new_str = ''

    for c in str:
        char_value = ord(c)
        if char_value >= 97 and char_value <= 123:
            new_str += chr(char_value - 32)
        else:
            new_str += c
    print("{}".format(new_str))
