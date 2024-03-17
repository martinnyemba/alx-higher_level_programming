#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Args:
        sentence (str): The input sentence.

    Returns:
        tuple: A tuple containing the length of the sentence
        and its first character.
    If the sentence is empty, the first character will be None.
    """
    str_length = len(sentence)
    if sentence == "":
        return None
    else:
        return str_length, sentence[0]
