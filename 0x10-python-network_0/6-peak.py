#!/usr/bin/python3
"""
looks for the peak in a list of unsorted integers
"""
def find_peak(list_of_integers):
    """function to find the peak"""
    if list_of_integers:
        peak = list_of_integers[0]
        for integer in list_of_integers:
            if integer > peak:
                peak = integer
        return peak
    return None
