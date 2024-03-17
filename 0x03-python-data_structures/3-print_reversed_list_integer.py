#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    function that prints all integers of a list, in reverse order.
    Prototype: def print_reversed_list_integer(my_list=[]):
    """
    my_list.reverse()
    for items in my_list:
        print("{}".format(items))
