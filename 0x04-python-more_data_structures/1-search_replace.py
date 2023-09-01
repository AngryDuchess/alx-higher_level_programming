#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in my_list:
        if my_list[i] == search:
            my_list[i] = replace
        new_list = my_list
    return new_list
