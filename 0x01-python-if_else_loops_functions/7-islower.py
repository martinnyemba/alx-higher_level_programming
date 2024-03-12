#!/usr/bin/python3

def islower(c):
    """function that checks for lowercase character."""
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
