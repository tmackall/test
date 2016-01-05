#!/usr/bin/python

import sys


if __name__ == '__main__':

    #
    # check the cmd line args
    if len(sys.argv) < 3:
        print '{} <file1> <file2>'.format(sys.argv[0])
        exit(1)
    else:
        #
        # open the files
        try:
            f1 = open(sys.argv[1], 'r')
        except (IOError, NameError):
            print '{} could not be opened'.format(sys.argv[1])
            exit(2)
        try:
            f2 = open(sys.argv[2], 'r')
        except (IOError, NameError):
            print '{} could not be opened'.format(sys.argv[2])
            exit(3)

    #
    # files -- read
    f1list = f1.read().splitlines()
    f2list = f2.read().splitlines()
    cmp = set(f1list) & set(f2list)
    print 'in common: {}'.format(cmp)

    #
    # files - compare, store common words
    for i in cmp:
        print 'Num occurrences of \"{}\" in file {}: {}'.format(
            i, sys.argv[1], f1list.count(i))
        print 'Num occurrences of \"{}\" in file {}: {}'.format(
            i, sys.argv[2], f2list.count(i))

    f1.close()
    f2.close()
