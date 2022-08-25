#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_arg = len(sys.argv) - 1
    sum = 0

    for i in range(num_arg):
        sum = sum + int(sys.argv[i + 1])
    print(sum)
