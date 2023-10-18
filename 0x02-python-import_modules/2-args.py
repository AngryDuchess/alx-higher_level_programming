#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_length = len(sys.argv) - 1
    arguments = sys.argv[1:]

    if arg_length == 0:
        print("{} arguments.".format(arg_length))
    elif arg_length == 1:
        print("{} argument:".format(arg_length))
    else:
        print("{} arguments:".format(arg_length))

    for i in range(arg_length):
        print("{}: {}".format(i + 1, arguments[i]))
