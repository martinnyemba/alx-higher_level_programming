#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    """
    This function performs a magic calculation based on the given inputs

    Parameters
    ----------
    a : int
        The first input.
    b : int
        The second input.

    Returns
    -------
    int
        The result of the magic calculation.
    """
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
