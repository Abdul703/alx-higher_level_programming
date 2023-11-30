#!/usr/bin/python3
import sys

if __name__ == '__main__':
    sum = 0
    args = sys.argv
    for i in range(1, len(args)):
        sum += int(args[i])
    print(sum)
