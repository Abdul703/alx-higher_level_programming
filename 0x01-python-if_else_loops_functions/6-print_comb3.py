#!/usr/bin/python3

for num in range(99):

    if num <= int(str(num)[::-1]) and num % 10 != num // 10:
        if num != 1:
            print(', ', end='')
        print("{:02d}".format(num), end='')
print()
