#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """for i in range(my_list):
        i < x
        if (my_list[i].isdigit() or my_list[0] == '-'):
            print("{:d}".format(my_list[i]))
            i += 1
        return i"""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i], end=""))
            count += 1
        
        except (TypeError, ValueError):
            pass
    print("")
    return count    
