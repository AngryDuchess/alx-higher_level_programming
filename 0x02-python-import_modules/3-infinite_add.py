#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_length = len(sys.argv) - 1
    arguments = sys.argv[1:]

    if arg_length == 0:
        print("0")
    else:
        count = 0
        for arg in arguments:
            count += int(arg)

        print(count)
