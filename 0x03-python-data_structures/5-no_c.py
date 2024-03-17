#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters 'c' and 'C' (case-insensitive) from the input string.
    Args:
        my_string: The input string.
    Returns:
        A new string without characters 'c' and 'C'.
    """
    return ''.join(char for char in my_string if char not in "cC")

