#!/usr/bin/python
import sys


if __name__ == '__main__':

    # set rows and cols based on the size of the table
    try:
        rows = sys.argv[1]
        cols = sys.argv[2]
    except IndexError:
        print 'Usage %s <rows> <cols>' % sys.argv[0]
        exit(1)
    print rows, cols
    # initialize array based on the size of the board
    # assign +1 for player 1 and -1 for player 2
    # traverse each row and see if the sum of each row = cols*1 or cols*-1
    # traverse each col and see if the sum of each col = rows*1 or rows*-1
