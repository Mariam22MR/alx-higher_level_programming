#!/usr/bin/python3
"""Defination of pascal's triangle function."""


def pascal_triangle(n):
    """represent pascal's triangle.

    Returns  list of lists of integers representing triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for n in range(len(tri) - 1):
            tmp.append(tri[n] + tri[n + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
