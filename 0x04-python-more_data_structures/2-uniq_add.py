#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    result = 0
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
            count += item
    result = sum(new_list)
    return result
