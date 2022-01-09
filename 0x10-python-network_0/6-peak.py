#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    peak = None if len(list_of_integers) == 0 else list_of_integers[0]
    
    for i in range(len(list_of_integers)):

        if list_of_integers[i] >= peak:
            peak = list_of_integers[i]
        else:
            break

    return peak
