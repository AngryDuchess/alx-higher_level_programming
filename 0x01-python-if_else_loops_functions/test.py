#!/usr/bin/python3

j = 0
while j < 9:
    i = j + 1  # Start i from j + 1 to ensure i > j
    while i <= 9:
        print("{:d}{:d}".format(j, i), end=", " if j < 8 else "\n")
        i += 1
    j += 1

