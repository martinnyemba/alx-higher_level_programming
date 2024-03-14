#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arguments = len(sys.argv)

    if arguments > 1:
        args = 1
        total = 0
        while(args <  arguments):
            total += int(sys.argv[args])
            args = args + 1
        print(total)
    else:
        print(0)
