#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    This function replaces all occurrences of an element by another
    in a new list.

    Args:
        my_list (list): The initial list.
        search: The element to replace in the list.
        replace: The new element.
    Returns:
        list: A new list with the specified replacements.
    """

    return list(map(lambda a: replace if a == search else a, my_list))
