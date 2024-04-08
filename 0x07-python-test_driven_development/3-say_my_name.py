#!/usr/bin/python3

"""Say my nem module"""


def say_my_name(first_name, last_name=""):
    """Say my name function"""
    if not isinstance(first_name, str):
        raise TypeError('firstname must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('lastname must be a string')
    print("My name is {} {}" .format(first_name, last_name))
