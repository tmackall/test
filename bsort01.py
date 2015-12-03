#!/usr/bin/python


def bsort(unsorted_list):
    ret_list = list(unsorted_list)
    for outer in ret_list:
        flag_change = False
        for inner in range(len(ret_list) - 1):
            if ret_list[inner] > ret_list[inner+1]:
                tmp = ret_list[inner]
                ret_list[inner] = ret_list[inner+1]
                ret_list[inner+1] = tmp
                flag_change = True
        if flag_change is False:
            break
    return ret_list

test_list = [1, 3, 2, 10, 7, 11]

slist = bsort(test_list)
print test_list
print slist
