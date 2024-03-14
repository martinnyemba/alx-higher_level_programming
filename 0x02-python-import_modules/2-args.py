#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    args_length = len(argv)

    if (args_length > 0):
        if (args_length == 2):
            print(f"{args_length - 1} argument:")
        else:
            print(f"{args_length - 1} arguments:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
    else:
        print(f"{args_length - 1} arguments.")
