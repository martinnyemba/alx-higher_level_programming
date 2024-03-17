#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    function that replaces an element of a list at a specific position
    Prototype: def replace_in_list(my_list, idx, element):

    If idx is negative, and returns the original list
    If idx is out of range  returns the original list
    """
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
