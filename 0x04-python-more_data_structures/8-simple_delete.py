#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
        """
    Delete a key-value pair from a dictionary.

    Args:
        a_dictionary (dict): The dictionary to delete the key-value pair from
        key (str, optional): The key of the key-value pair to delete.
            Defaults to "".

    Returns:
        dict: The modified dictionary.

    Raises:
        KeyError: If the key is not present in the dictionary.
    """
    if key not in a_dictionary:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
