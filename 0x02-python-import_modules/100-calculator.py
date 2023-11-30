#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    args = sys.argv

    # check if the number of arguments is not 3
    if len(args) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    # check if the operator is not valid
    if args[2] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    a = int(args[1])
    b = int(args[3])

    if args[2] == '+':
        print(f'{a:d} {args[2]} {b:d} = {add(a, b)}')
    elif args[2] == '-':
        print(f'{a:d} {args[2]} {b:d} = {sub(a, b)}')
    elif args[2] == '*':
        print(f'{a:d} {args[2]} {b:d} = {mul(a, b)}')
    elif args[2] == '/':
        print(f'{a:d} {args[2]} {b:d} = {div(a, b)}')


if __name__ == '__main__':
    main()
