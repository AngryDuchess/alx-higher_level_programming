#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    arg_length = len(sys.argv) - 1
    arguments = sys.argv[1:]

    if arg_length > 1:
        print("{} arguments:".format(arg_length))
    elif arg_length == 1:
        print("{} argumet:".format(arg_length))
    else:
        print(".")

    #print()

    for i in range(arg_length):
        print("{}: {}".format(i, arguments[i]))
        i+=1
