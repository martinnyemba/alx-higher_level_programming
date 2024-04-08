#!/usr/bin/python3

"""Print Square Module"""


def print_square(size):
    """
    function that prints a square with the character #

    Args:
        size: is the size length of the square

    Return:
        print square usingnthe size
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size < 0 and isinstance(size, float):
        raise TypeError('size must be an integer')
    i = 0
    while (i < size):
        for j in range(size):
            print("#", end="")
        print("")
        i += 1
