#!/usr/bin/python
import random
import sys


if __name__ == '__main__':

    # set rows and cols based on the size of the table
    try:
        rows = int(sys.argv[1])
        cols = rows
    except IndexError:
        print 'Usage %s <rows/cols>' % sys.argv[0]
        exit(1)
    num_squares = rows*cols

    val = random.sample([1, -1], 1)
    val = val.pop()

    if val == -1:
        valp = 1
    else:
        valp = -1

    lin_board = [[val]*rows for _ in xrange(cols)]
    print '{}\n'.format(lin_board[0][0])
    mid = num_squares/2
    rlist = random.sample(range(num_squares), mid)
    for i in rlist:
        r = i/rows
        c = i % cols
        lin_board[r][c] = valp
    print lin_board

    for row in range(rows):
        tot = sum(lin_board[row])


    # initialize array based on the size of the board
    # assign +1 for player 1 and -1 for player 2
    # traverse each row and see if the sum of each row = cols*1 or cols*-1
    # traverse each col and see if the sum of each col = rows*1 or rows*-1
