import random

list_nums = random.sample(xrange(100), 5)

print list_nums

list_tots = []
for i in xrange(len(list_nums)):
    tmp = list_nums.pop(i)
    tot = 1
    for j in list_nums:
        tot *= j
    list_tots.append(tot)
    list_nums.insert(i, tmp)

print list_tots
