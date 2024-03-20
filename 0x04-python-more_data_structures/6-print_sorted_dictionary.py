#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
        a_dictionary (dict): The dictionary to be printed.

    Returns:
        None

    Notes:
        - Keys should be sorted in alphabetical order.
        - Only the keys of the first level should be sorted;
        keys of nested dictionaries should not be sorted.
        - The dictionary values can have any type.
        - No external modules are allowed to be imported.
    """
    for k in sorted(a_dictionary):
        print(k, a_dictionary[k], sep=': ')
