#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    This function takes two tuples as input and returns the
    sum of corresponding elements in the tuples.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        tuple: A new tuple containing the sum of corresponding
        elements from tuple_a and tuple_b.
    """

    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
