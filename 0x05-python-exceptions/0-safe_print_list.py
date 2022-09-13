#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            if i == x - 1:
                print("")
        except IndexError:
            break
    return (i + 1)
