#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    arg_length = len(sys.argv) - 1

    if arg_length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    operators = ['+', '-', '*', '/']

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
