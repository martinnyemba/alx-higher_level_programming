#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The list from which to delete the item.
        idx (int): The index of the item to delete.

    Returns:
        list: The updated list with the item deleted.

    Notes:
        - If idx is negative or out of range, nothing changes
        (returns the same list).
        - This function does not use the pop() method.
        - No external modules are imported.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
