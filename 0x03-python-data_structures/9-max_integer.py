#!/c/Users/maham/AppData/Local/Microsoft/WindowsApps/python
def max_integer(my_list=[]):
    if my_list == []:
        return None
    new_list = sorted(my_list)
    return new_list.pop()
