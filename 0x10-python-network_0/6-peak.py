#!/usr/bin/python3
"""
a function that finds a peak in a list of integers.
"""


def find_peak(list_of_integers):
    """
    Finds the peak
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        peak = max(list_of_integers)
        return peak

    mid = len(list_of_integers) // 2
    peak = list_of_integers[mid]
    if list_of_integers[mid - 1] < peak and list_of_integers[mid + 1] < peak:
        return peak
    elif list_of_integers[mid - 1] > peak:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
