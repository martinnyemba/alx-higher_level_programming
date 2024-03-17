#!/usr/bin/python3

def element_at(my_list, idx):
    """
    function that retrieves an element from a list like in C
    .
    Prototype: def element_at(my_list, idx):
    If idx is negative, return None
    If idx is out of range, return None
    """
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
