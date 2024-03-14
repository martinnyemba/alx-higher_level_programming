#!/usr/bin/python3

import sys

if __name__ == "__main__":
    
    argv = sys.argv
    args_length = len(argv)
    list = str(argv)

    if args_length == 1:
        print("0 arguments.")
    elif args_length == 2:
        print(f"{args_length - 1} argument:")
        for i in range(1, args_length):
            print(f"{i}: {argv[i]}")
    elif args_length > 2:
        print(f"{args_length - 1} arguments:")

        for i in range(1, args_length):
            print(f"{i}: {argv[i]}")
