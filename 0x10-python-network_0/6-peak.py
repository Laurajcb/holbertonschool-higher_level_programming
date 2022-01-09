#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    if type(list_of_integers) is not list:
        return None

    if len(list_of_integers) == 0:
        return None

    peak = list_of_integers[0]
    for i in range(1, len(list_of_integers)):

        if list_of_integers[i] >= peak:
            peak = list_of_integers[i]
        elif list_of_integers[i] >= 0:
            break

    return peak
