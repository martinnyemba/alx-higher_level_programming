#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    function that prints all integers of a list, in reverse order.

    Parameters:
    my_list (list, optional): the list of integers to be printed in reverse order.
    If no list is provided, an empty list is used by default.

    Returns:
    None

    Raises:
    ValueError: if the list contains non-integer elements
    """
    if my_list:
        my_list.reverse()
        for item in my_list:
            print("{:d}".format(item))
