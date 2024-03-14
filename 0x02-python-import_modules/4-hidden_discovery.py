#!/usr/bin/python3
"""
# program that prints all the names defined by the compiled module
# print one name per line, in alpha order
#  print only names that do not start with __
"""
import sys

if __name__ == "__main__":
    import hidden_4 as hidden

    names = dir(hidden)
    names = [n for n in names if not n.startswith("__")]
    names.sort()
    for name in names:
        print(name)
