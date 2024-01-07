#!/usr/bin/python3
"""
Defines matrix multiplication function using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix that given

    Args:
        m_a: input first matrix
        m_b: input second matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
