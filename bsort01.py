#!/usr/bin/python
'''
bubble sort - N**2 algorithm
'''

import random


def bsort(unsorted_list):
    ret_list = list(unsorted_list)
    for outer in ret_list:
        flag_change = False
        for inner in range(len(ret_list) - 1):
            if ret_list[inner] > ret_list[inner+1]:
                ret_list[inner], ret_list[inner+1] = \
                    ret_list[inner+1], ret_list[inner]
                flag_change = True
        if flag_change is False:
            break
    return ret_list

test_list = random.sample(xrange(1000), 20)

slist = bsort(test_list)
print 'before list: %s' % test_list
print 'sorted list: %s' % slist
