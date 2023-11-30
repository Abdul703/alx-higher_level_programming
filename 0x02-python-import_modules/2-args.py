#!/usr/bin/python3
import sys

if __name__ == '__main__':
    len_args = len(sys.argv)
    if len_args == 1:
        print('0 arguments.')
    else:
        print('{:d} argument{}:'.format(len_args - 1,
            's' if len_args > 2 else ''))
        for i in range(1, len_args):
            print(f"{i:d}: {sys.argv[i]}")
