#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    This function adds all unique integers in a list,
    considering each integer only once.

    Prototype: def uniq_add(my_list=[]):
    You are not allowed to import any module

    Example Usage:
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
    """

    uniq_num = []
    for x in my_list:
        if x not in uniq_num:
            uniq_num.append(x)
    result = 0
    for x in uniq_num:
        result += x
    return result
