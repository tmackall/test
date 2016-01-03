#!/usr/bin/python
from random import randint

the_list = []
nums = 100
for i in range(nums):
    the_list.append(randint(1, nums))

print the_list
print the_list.count(1)

#
# set - turn list into a set
s = set(the_list)
print s
print len(s)

#
# set elements will print nums in order
for i in s:
    print i
