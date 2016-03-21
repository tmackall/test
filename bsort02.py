#!/usr/bin/python

import random


def bsort(unsorted_list):
    '''
    bsort() - bubble sort n**2
    '''

    # outer loop - loop on all elements
    for o in range(len(unsorted_list)):
        # inner loop - loop on elements
        for i in range(len(unsorted_list) - 1):
            # if N > N + 1 - swap them
            if unsorted_list[i] > unsorted_list[i+1]:
                tmp = unsorted_list[i+1]
                unsorted_list[i+1] = unsorted_list[i]
                unsorted_list[i] = tmp


size = 100
n = []

for j in range(size):
    n.append(random.randint(1, size))

bsort(n)


print n
print len(n)
