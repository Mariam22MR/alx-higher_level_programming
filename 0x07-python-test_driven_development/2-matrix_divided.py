#!/usr/bin/python3
"""
script that defines function for matrix division.
"""


def matrix_divided(matrix, div):
    """Divides elements of matrix.
    Args:
        matrix: list of lists of int or float.
        div: number to divides matrix.
    Raises:
        TypeError: if matrix is not list of lists containing int or float.
        TypeError: if sublists are different sizes.
        TypeError: if div is not int or float.
        ZeroDivisionError: if div is 0.
    Returns:
        new matrix representing result of division.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
