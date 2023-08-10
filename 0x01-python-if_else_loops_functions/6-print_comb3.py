#!/usr/bin/python3
j = 0
while j < 9:
    i = j + 1
    while i <= 9:
        print("{:d}{:d}".format(j, i), end=", " if j < 8 else "\n")
        i += 1
    j += 1
