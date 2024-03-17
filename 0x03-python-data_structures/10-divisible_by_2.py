#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Returns a new list with True or False, depending on whether the
    integer at the same position in the original list is a multiple of 2
    Args:
        my_list (list): The original list of integers.

    Returns:
        list: A new list with True or False values, indicating
        whether each integer in the original list is divisible by 2.
    """
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
