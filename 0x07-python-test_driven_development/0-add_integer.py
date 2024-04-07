#!/bin/usr/python3

def add_integer(a, b=98):
    """
    A a function that adds 2 integers

    Args:
        a: int or float - postional argument
        b: int or flaot

    Return: addition of (a + b)
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    else:
        a = int(a)
        b = int(b)
        return (a + b)


if __name__ == "__main__":
    import doctest
    docktest.testmod()
