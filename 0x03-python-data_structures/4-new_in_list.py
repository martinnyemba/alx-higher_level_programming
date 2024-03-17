#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    This function takes a list, an index, and an element, and returns a
    new list with the element inserted at the specified index.
    
    Args:
    my_list (list): The list to which the element will be added.
    idx (int): The index at which the element will be inserted.
    element: The element to be inserted into the list.

    Returns:
    list: A new list with the element inserted at the specified index.
    """

    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
