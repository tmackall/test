#!/usr/bin/python
import sys

def find_min(list):

    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]

    return min


if __name__ == "__main__":
    t = [38, 40, 55, 89, 6, 13, 20, 23, 36.]
    print sys.argv
    print find_min(t)
