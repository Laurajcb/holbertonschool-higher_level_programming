#!/usr/bin/python3
"""
    Function to divide the elements
    of a matrix, elements of the matrix
    must be integers or floats
"""


def matrix_divided(matrix, div):
    """Divide each and all the elements in a matrix
    wih div. The elements and div should be int or
    float type.
    return new matrix with the results of the division
    """

    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    if size == 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) is not size:
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(b / div, 2) for b in i] for i in matrix]
