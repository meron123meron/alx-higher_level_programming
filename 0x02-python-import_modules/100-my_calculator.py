#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    num_arg = len(sys.argv) - 1
    oper = {"+": add, "-": sub, "*": mul, "/": div}
    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in list(oper.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} = {}"
              .format(a, sys.argv[2], b, oper[sys.argv[2]](a, b)))
        exit(0)
