#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element at a specific index in a given list.

    Args:
        my_list (list): The list in which the element needs to be replaced.
        idx (int): The index at which the element needs to be replaced.
        element: The new element to be placed at the specified index.

    Returns:
        None. The function modifies the original list in-place.
    """
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    elif my_list == []:
        return None
    else:
        my_list[idx] = element
        return my_list
