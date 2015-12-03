#!/usr/bin/python

def partition(plist, pstart, pend):
    '''
    partitions the list into 2 sublist and return the partion index
    '''
    # create the pivot - lend
    # iterate through all elements - compare each element to the pivot. Swap any value less
    # than the pivot value
    pivot_idx = pend
    part_idx = pstart
    for i in range(pstart, pend-1):
        if plist[i] < plist[pend]:
            tmp = plist[i]
            plist[i] = plist[part_idx]
            plist[part_idx] = tmp
            part_idx += 1

    if plist[pivot_idx] <  plist[part_idx]:
        tmp = plist[pivot_idx]
        plist[pivot_idx] = plist[part_idx]
        plist[part_idx] = tmp
        part_idx += 1

    print "%s, %s" % (plist, part_idx)
    return part_idx


def qsort(qlist, lstart, lend):
    # if not lstart < lend then exit
    if lstart < lend:
        # pivot - get pivot index
        pindex = partition(qlist, lstart, lend)
        # partition into 2 lists
        # qsort left list
        qsort(qlist, lstart, pindex-1)
        # qsort right list
        qsort(qlist, pindex + 1, lend)

    return 0

a = [4, 5, 1, 6, 8, 9, 3]
print a
qsort(a, 0, len(a) - 1)
print a
