#!/usr/bin/env python3

from calculator_1 import add, sub, mult, div


if __name__ == "__main__":
    a = 10
    b = 5
    print("{}".format(add(a, b)))
    print("{}".format(sub(a, b)))
    print("{}".format(mult(a, b)))
    print("{}".format(div(a, b)))
