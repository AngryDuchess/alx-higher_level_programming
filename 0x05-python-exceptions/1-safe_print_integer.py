#!/usr/bin/python3
def safe_print_integer(value):
    int_val = str(value)
    try:
        if (int_val.isdigit() or (int_val[0] == '-' and int_val[1:].isdigit())):
            print("{:d}".format(int(int_val)))
            return True
    except ValueError:
        print(int_val)
        return False
