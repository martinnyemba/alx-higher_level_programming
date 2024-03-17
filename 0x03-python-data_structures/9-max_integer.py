#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    This function finds the biggest integer in a list.

    Args:
        my_list (list): The list of integers to search for the maximum value.

    Returns:
        int: The maximum integer value in the list.

    Raises:
        None

    Notes:
        - If the list is empty, the function returns None.
        - The function assumes that the list only contains integers.
        - The function does not import any modules.
        - The function does not use the built-in max() function.
    """
    if my_list == []:
        return None
    else:
        my_list.sort()
        return my_list[-1]
