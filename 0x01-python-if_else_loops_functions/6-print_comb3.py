#!/usr/bin/python3

for num in range(99):

    if num <= int(str(num)[::-1]):
        if num != 0:
            print(', ', end='')
        print("{:02d}".format(num), end='')
print()
