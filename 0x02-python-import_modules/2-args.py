#!/usr/bin/python3
import sys

if __name__ == '__main__':
    len_args = len(sys.argv) - 1
    if len_args == 0:
        print('0 arguments.')
    else:
        print('{:d} argument{}:'.format(len_args, 's' if len_args > 1 else ''))
        for i in range(1, len_args + 1):
            print(f"{i:d}: {sys.argv[i]}")
