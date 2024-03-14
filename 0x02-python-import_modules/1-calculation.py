#!/usr/bin/python3

if __name__ == "__main__":
    #  import the functions
    from calculator_1 import add, sub, mul, div

    """ Define and assign variables:
    - the value 10 to a variable a
    - the value 5 to a variable b
    - use those two variables only, as arguments when calling functions
    """
    a = 10
    b = 5

    #  print (with string format to display integers)
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
