#!/usr/bin/env python3
import sys

def test ():
    i = 0
    with open("numbers.txt") as fic:
        for l in fic:
            if sys.argv[1] == "+":
                i = i + int(l)
                print("+", l, " =", i)
            if sys.argv[1] == "*":
                i = i * int(l)
                print("*", l, " =", i)

    return i

if __name__ == '__main__':
    print(test())
