#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    function that replaces an element of a list at a specific position
    Prototype: def replace_in_list(my_list, idx, element):

    """
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
