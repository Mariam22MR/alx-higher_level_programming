#!/usr/bin/python3
"""
Module for matrix_mul method
"""


def matrix_mul(m_a, m_b):
    """multiplies one matrix by another
    Args:
        m_a: first matrix
        m_b: second matrix
    Returns:
        matrix: product
    Raises:
        TypeError: if m_a or m_b not lists.
        TypeError: if m_a or m_b not lists of lists.
        ValueError: if m_a or m_b empty lists/matrices.
        TypeError: if m_a or m_b contain non int/float.
        TypeError: if m_a or m_b not rectangular.
        ValueError: if m_a or m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    m_a_empty = False
    m_b_empty = False
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_notnum = True

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnum = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_notnum:
        raise TypeError('m_a should contain only integers or floats')

    if m_b_notnum:
        raise TypeError('m_b should contain only integers or floats')

    if m_a_notrect:
        raise TypeError('each row of m_a must should be of the same size')

    if m_b_notrect:
        raise TypeError('each row of m_b must should be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[] for n in range(len(m_a))]

    for n in range(len(m_a)):
        for l in range(len(m_b[0])):
            c = 0
            for s in range(len(m_b)):
                c += m_a[n][s] * m_b[s]l]
            res[n].append(c)

    return res

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
