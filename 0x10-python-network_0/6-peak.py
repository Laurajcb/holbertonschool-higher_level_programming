#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    peak = None
    for i in range(len(list_of_integers)):
        if peak is None:
            peak = list_of_integers[i]
            continue

        if list_of_integers[i] >= peak:
            peak = list_of_integers[i]
        else:
            break

    return peak


list_of_integers = [4, 2, 3, 1, 9]
print(find_peak(list_of_integers))
print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2, 4, 3]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
