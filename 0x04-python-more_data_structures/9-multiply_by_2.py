#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    function that returns a new dictionary with all values multiplied by 2
    """
    new_dict = {}
    for i in a_dictionary:
        new_dict.update({i: a_dictionary[i]*2})
    return new_dict
