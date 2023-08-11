#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            alpha = 32
        else:
            alpha = 0
        print("{:c}".format(ord(str[i]) - alpha), end='')
    print()      
