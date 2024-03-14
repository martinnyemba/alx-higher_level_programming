#!/usr/bin/python3

#  import the functions
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    """ Define and assign variables:
    - the value 10 to a variable a
    - the value 5 to a variable b
    - use those two variables only, as arguments when calling functions
    """
    a = 10
    b = 5

    sum = add(a, b)
    sub = sub(a, b)
    mul = mul(a, b)
    div = div(a, b)

    #  print (with string format to display integers)
    print(f"{a} + {b} = {sum}")
    print(f"{a} - {b} = {sub}")
    print(f"{a} * {b} = {mul}")
    print(f"{a} / {b} = {div}")
