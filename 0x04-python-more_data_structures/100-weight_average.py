#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    function that returns the weighted average of all
    integers tuple (<score>, <weight>)
    """
    if (my_list):
        return (sum(x*y for x, y in my_list) / sum(y for x, y in my_list))
    else:
        return (0)
